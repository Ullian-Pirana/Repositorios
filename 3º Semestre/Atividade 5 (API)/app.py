from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# Caminhos para os arquivos CSV
clientes_file = 'clientes.csv'
produtos_file = 'produtos.csv'
ordens_file = 'ordens.csv'

# Função para ler CSV e retornar uma lista de dicionários
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Função para escrever no CSV
def write_csv(file_path, data, fieldnames):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# ========================================
# Endpoints para Clientes
# ========================================

@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = read_csv(clientes_file)
    return jsonify(clientes)

@app.route('/clientes', methods=['POST'])
def add_cliente():
    data = request.get_json()
    clientes = read_csv(clientes_file)
    new_id = max([int(cliente['ID']) for cliente in clientes]) + 1 if clientes else 1
    data['ID'] = new_id
    clientes.append(data)
    write_csv(clientes_file, clientes, fieldnames=["ID", "Nome", "Sobrenome", "Data de Nascimento", "CPF"])
    return jsonify(data), 201

@app.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.get_json()
    clientes = read_csv(clientes_file)
    for cliente in clientes:
        if int(cliente['ID']) == id:
            cliente.update(data)
            write_csv(clientes_file, clientes, fieldnames=["ID", "Nome", "Sobrenome", "Data de Nascimento", "CPF"])
            return jsonify(cliente)
    return jsonify({"message": "Cliente não encontrado"}), 404

@app.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    clientes = read_csv(clientes_file)
    clientes = [cliente for cliente in clientes if int(cliente['ID']) != id]
    write_csv(clientes_file, clientes, fieldnames=["ID", "Nome", "Sobrenome", "Data de Nascimento", "CPF"])
    return jsonify({"message": "Cliente removido com sucesso"}), 200

# ========================================
# Endpoints para Produtos
# ========================================

@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = read_csv(produtos_file)
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def add_produto():
    data = request.get_json()
    produtos = read_csv(produtos_file)
    new_id = max([int(produto['ID']) for produto in produtos]) + 1 if produtos else 1
    data['ID'] = new_id
    produtos.append(data)
    write_csv(produtos_file, produtos, fieldnames=["ID", "Nome", "Fornecedor", "Quantidade"])
    return jsonify(data), 201

@app.route('/produtos', methods=['PUT'])
def update_produto():
    data = request.get_json()
    produtos = read_csv(produtos_file)
    for produto in produtos:
        if int(produto['ID']) == data['ID']:
            produto.update(data)
            write_csv(produtos_file, produtos, fieldnames=["ID", "Nome", "Fornecedor", "Quantidade"])
            return jsonify(produto)
    return jsonify({"message": "Produto não encontrado"}), 404

@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    produtos = read_csv(produtos_file)
    produtos = [produto for produto in produtos if int(produto['ID']) != id]
    write_csv(produtos_file, produtos, fieldnames=["ID", "Nome", "Fornecedor", "Quantidade"])
    return jsonify({"message": "Produto removido com sucesso"}), 200

# ========================================
# Endpoints para Ordens de Venda
# ========================================

@app.route('/ordens', methods=['GET'])
def get_ordens():
    ordens = read_csv(ordens_file)
    return jsonify(ordens)

@app.route('/ordens', methods=['POST'])
def add_ordem():
    data = request.get_json()
    ordens = read_csv(ordens_file)
    new_id = max([int(ordem['ID']) for ordem in ordens]) + 1 if ordens else 1
    data['ID'] = new_id
    ordens.append(data)
    write_csv(ordens_file, ordens, fieldnames=["ID", "Cliente", "Produto"])
    return jsonify(data), 201

@app.route('/ordens', methods=['PUT'])
def update_ordem():
    data = request.get_json()
    ordens = read_csv(ordens_file)
    for ordem in ordens:
        if int(ordem['ID']) == data['ID']:
            ordem.update(data)
            write_csv(ordens_file, ordens, fieldnames=["ID", "Cliente", "Produto"])
            return jsonify(ordem)
    return jsonify({"message": "Ordem de venda não encontrada"}), 404

@app.route('/ordens/<int:id>', methods=['DELETE'])
def delete_ordem(id):
    ordens = read_csv(ordens_file)
    ordens = [ordem for ordem in ordens if int(ordem['ID']) != id]
    write_csv(ordens_file, ordens, fieldnames=["ID", "Cliente", "Produto"])
    return jsonify({"message": "Ordem de venda removida com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
