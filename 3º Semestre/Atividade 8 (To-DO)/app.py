from flask import Flask, request, render_template, redirect, jsonify
import os, csv

app = Flask(__name__)

# Caminhos dos arquivos CSV = Transformados em variáveis
ToDo_csv = "ToDo.csv"

#Executa leitura do arquivo
def ler_csv(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

#Executa escrita do arquivo
def escrever_csv(arquivo, dados, campos):
    with open(arquivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(dados)

#------------------#

# Clientes 

#Retorna as informações dos clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    return jsonify(ler_csv(ToDo_csv))

#Te permite adicionar um novo cliente
@app.route('/add_clientes', methods=['POST']) #ok
def adicionar_cliente():
    clientes = ler_csv(ToDo_csv)
    novo_id = max([int(c["ID"]) for c in clientes], default=0) + 1
    novo_cliente = {
        "ID": str(novo_id),
        "Nome": request.json["Nome"],
        "Sobrenome": request.json["Sobrenome"],
        "Data de nascimento": request.json["Data de nascimento"],
        "CPF": request.json["CPF"]
    }
    clientes.append(novo_cliente)
    escrever_csv(ToDo_csv, clientes, novo_cliente.keys())
    return jsonify(novo_cliente), 201

#Atualiza as infor
@app.route('/up_clientes/<id>', methods=['PUT']) #ok colocar na doc q deve passar up_clientes / o id
def atualizar_cliente(id):
    clientes = ler_csv(ToDo_csv)

    id_str = str(id)

    for cliente in clientes:
        if str(cliente["ID"]) == id_str:
            if not request.json:
                return jsonify({"error": "Nenhum dado enviado"}), 400
            
            cliente.update(request.json)
            escrever_csv(ToDo_csv, clientes, cliente.keys())
            return jsonify(cliente), 200

    return jsonify({"error": "Cliente não encontrado"}), 404

@app.route('/del_clientes/<id>', methods=['DELETE']) #ok colocar na doc q deve passar del_clientes / o id
def remover_cliente(id):
    clientes = ler_csv(ToDo_csv)
    clientes = [c for c in clientes if c["ID"] != id]
    escrever_csv(ToDo_csv, clientes, ["ID", "Nome", "Sobrenome", "Data de nascimento", "CPF"])
    return jsonify({"message": "Cliente removido"}), 200

#------------------#

# Tarefas 
@app.route('/tarefas', methods=['GET']) #ok
def listar_tarefas():
    return jsonify(ler_csv(ToDo_csv))

@app.route('/add_tarefas', methods=['POST']) #ok
def adicionar_tarefa():
    tarefas = ler_csv(ToDo_csv)
    novo_id = max([int(p["ID"]) for p in tarefas], default=0) + 1
    nova_tarefa = {
        "ID": str(novo_id),
        "Nome": request.json["Nome"],
        "Fornecedor": request.json["Fornecedor"],
        "Quantidade": int(request.json["Quantidade"])
    }
    tarefas.append(nova_tarefa)
    escrever_csv(ToDo_csv, tarefas, nova_tarefa.keys())
    return jsonify(nova_tarefa), 201

@app.route('/up_tarefas/<id>', methods=['PUT']) #ok
def atualizar_tarefa(id):
    tarefas = ler_csv(ToDo_csv)
    for tarefa in tarefas:
        if tarefa["ID"] == id:
            tarefas.update(request.json)
            escrever_csv(ToDo_csv, tarefas, tarefa.keys())
            return jsonify(tarefa), 200
    return jsonify({"error": "Tarefa não encontrado"}), 404

@app.route('/del_tarefas/<id>', methods=['DELETE']) #ok
def remover_tarefa(id):
    tarefas = ler_csv(ToDo_csv)
    tarefas = [p for p in tarefas if p["ID"] != id]
    escrever_csv(ToDo_csv, tarefas, ["ID", "Nome", "Fornecedor", "Quantidade"])
    return jsonify({"message": "Tarefa removida"}), 200

#------------------#

# Ordens de Venda 
@app.route('/ordens', methods=['GET']) #ok
def listar_ordens():
    return jsonify(ler_csv())

@app.route('/add_ordens', methods=['POST']) #ok
def criar_ordem():
    ordens = ler_csv()
    novo_id = max([int(o["ID_O"]) for o in ordens], default=0) + 1

    data = request.get_json()  # Obtém o JSON corretamente

    if not data:
        return jsonify({"erro": "Requisição não contém um JSON válido"}), 400

    cliente = data.get("Cliente")
    tarefa = data.get("tarefa")

    if not cliente or not tarefa:
        return jsonify({"erro": "Campos 'Cliente' e 'tarefa' são obrigatórios"}), 400

    nova_ordem = {
        "ID_O": novo_id,
        "Cliente": cliente,
        "Tarefa": tarefa
    }

    ordens.append(nova_ordem)
    escrever_csv(ToDo_csv, ordens, nova_ordem.keys())

    return jsonify(nova_ordem), 201


@app.route('/up_ordens/<id>', methods=['PUT']) #ok
def atualizar_ordem(id):
    ordens = ler_csv()
    for ordem in ordens:
        if ordem["ID_O"] == id:
            ordem.update(request.json)
            escrever_csv(ToDo_csv, ordens, ordem.keys())
            return jsonify(ordem), 200
    return jsonify({"error": "Ordem não encontrada"}), 404

@app.route('/del_ordens/<id>', methods=['DELETE']) #ok
def remover_ordem(id):
    ordens = ler_csv()

    # Filtra ordens e verifica se alguma foi removida
    novas_ordens = [o for o in ordens if str(o["ID_O"]) != str(id)]

    if len(novas_ordens) == len(ordens):  # Se nenhuma ordem foi removida
        return jsonify({"error": "Ordem não encontrada"}), 404

    escrever_csv(ToDo_csv, novas_ordens, ["ID_O", "Cliente", "Produto"])
    return jsonify({"message": "Ordem removida"}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)