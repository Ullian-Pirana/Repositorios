from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/") #Rota para a página inicial do nosso To-do
def homepage():
    return render_template("homepage.html") #Renderizaçaõ da pagina inicial, pelo arquivo 'homepage.html'

@app.route("/tarefas") #Rota para a página onde visualizamos as tarefes já adicionadas: '/tarefas'
def tarefas():
    return render_template("tarefas.html") #Renderizaçaõ da pagina para visualização de tarefas, pelo arquivo 'tarefas.html'

@app.route("/add_tarefa") #Rota para a página onde adicionamos as tarefas: '/add_tarefa'
def tarefas():
    return render_template("add_tarefa.html") #Renderização da página para adicionar tarefas:  'add_tarefa.html'





















if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
