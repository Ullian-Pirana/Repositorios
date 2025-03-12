from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", Variavel="Senai 2025, TI é eleito como melhor curso", idade=32)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")