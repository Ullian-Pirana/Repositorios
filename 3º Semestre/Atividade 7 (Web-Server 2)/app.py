from flask import Flask, render_template, request, redirect

app = Flask(__name__)

context = {}
produtos = {}
produtos[1] = {
    "nome" : "abacaxi",
    "Preco" : 15.50
}

produtos[2] = {
    "nome" : "Manga",
    'Preco' : 7.99
}

@app.route('/produtos')
def produto():
    context['produtos'] = produtos
    return render_template ("Produtos.html", **context)

@app.route('/form_produto')
def form_produto():
    return render_template ('add_produtos.html', **context)

@app.route('/add_produto', methods=['POST'])
def add_produto():
    nome = request.form['Nome']
    preco = request.form['Preco']

    produtos[len(produtos) + 1] = {
        'nome' : nome,
        'Preco' : preco
    }

    return redirect('/produtos')


if __name__ == "__main__":
    app.run(debug=True)