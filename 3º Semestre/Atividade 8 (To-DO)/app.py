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

#Retorna as informações dos tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(ler_csv(ToDo_csv))

#Te permite adicionar um novo tarefa
@app.route('/add_tarefas', methods=['POST']) #ok
def adicionar_tarefas():
    tarefas = ler_csv(ToDo_csv)
    novo_id = max([int(c["ID"]) for c in tarefas], default=0) + 1
    nova_tarefa = {
        "ID": str(novo_id),
        "Nome": request.json["Nome"],
        "Sobrenome": request.json["Sobrenome"],
        "Data de nascimento": request.json["Data de nascimento"],
        "CPF": request.json["CPF"]
    }
    tarefas.append(nova_tarefa)
    escrever_csv(ToDo_csv, tarefas, nova_tarefa.keys())
    return jsonify(nova_tarefa), 201

#Atualiza as informações
@app.route('/up_tarefas/<id>', methods=['PUT']) #ok colocar na doc q deve passar up_tarefas / o id
def atualizar_tarefa(id):
    tarefas = ler_csv(ToDo_csv)

    id_str = str(id)

    for tarefa in tarefas:
        if str(tarefa["ID"]) == id_str:
            if not request.json:
                return jsonify({"error": "Nenhum dado enviado"}), 400
            
            tarefa.update(request.json)
            escrever_csv(ToDo_csv, tarefas, tarefa.keys())
            return jsonify(tarefa), 200

    return jsonify({"error": "Tarefa não encontrada"}), 404

@app.route('/del_tarefas/<id>', methods=['DELETE']) #ok colocar na doc q deve passar del_tarefas / o id
def remover_tarefa(id):
    tarefas = ler_csv(ToDo_csv)
    tarefas = [c for c in tarefas if c["ID"] != id]
    escrever_csv(ToDo_csv, tarefas, []) #Id, nome, descricao e emergenica
    return jsonify({"message": "Tarefa removido"}), 200

#------------------#


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)