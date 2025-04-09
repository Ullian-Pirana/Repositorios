from flask import Flask, render_template, request, redirect, url_for
import csv
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/tarefas'
CSV_FILE = 'ToDo.csv'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def ler_tarefas():
    tarefas = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['id'] = int(row['id'])  # Convertemos para int
                tarefas.append(row)
    return tarefas

def salvar_tarefas(tarefas):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        campos = ['id', 'nome', 'descricao', 'prioridade', 'concluida', 'imagem']
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for tarefa in tarefas:
            writer.writerow(tarefa)

@app.route('/tarefas', methods=['GET', 'POST'])
def tarefas():
    tarefas = ler_tarefas()
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        prioridade = request.form.get('prioridade')
        concluida = 'sim' if request.form.get('concluida') else 'não'

        imagem = request.files.get('imagem')
        if imagem and imagem.filename:
            filename = secure_filename(imagem.filename)
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
            imagem.save(caminho_imagem)
            caminho_relativo = caminho_imagem.replace('static/', '')
        else:
            caminho_relativo = ''

        novo_id = max([t['id'] for t in tarefas], default=0) + 1
        nova_tarefa = {
            'id': novo_id,
            'nome': nome,
            'descricao': descricao,
            'prioridade': prioridade,
            'concluida': concluida,
            'imagem': caminho_relativo
        }

        tarefas.append(nova_tarefa)
        salvar_tarefas(tarefas)
        return redirect(url_for('tarefas'))

    return render_template('tarefas.html', tarefas=tarefas)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarefas = ler_tarefas()
    tarefa = next((t for t in tarefas if t['id'] == id), None)

    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        prioridade = request.form.get('prioridade')
        concluida = 'sim' if request.form.get('concluida') else 'não'

        imagem = request.files.get('imagem')
        if imagem and imagem.filename:
            filename = secure_filename(imagem.filename)
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
            imagem.save(caminho_imagem)
            caminho_relativo = caminho_imagem.replace('static/', '')
        else:
            caminho_relativo = tarefa['imagem']

        tarefa.update({
            'nome': nome,
            'descricao': descricao,
            'prioridade': prioridade,
            'concluida': concluida,
            'imagem': caminho_relativo
        })

        salvar_tarefas(tarefas)
        return redirect(url_for('tarefas'))

    return render_template('editar.html', tarefa=tarefa)

@app.route('/deletar/<int:id>', methods=['GET', 'POST'])
def deletar(id):
    tarefas = ler_tarefas()
    tarefa = next((t for t in tarefas if t['id'] == id), None)

    if request.method == 'GET':
        return render_template('confirmar_deletar.html', tarefa=tarefa)

    elif request.method == 'POST':
        tarefas = [t for t in tarefas if t['id'] != id]
        salvar_tarefas(tarefas)
        return redirect(url_for('tarefas'))

if __name__ == '__main__':
    app.run(debug=True)