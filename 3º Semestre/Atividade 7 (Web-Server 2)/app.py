from flask import Flask, render_template

app = Flask(__name__)

context =   {}
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

if __name__ == "__main__":
    app.run(debug=True)