from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def homepage():
    context = {}
    context["img"] = "img/logo.png"
    context["Titulo"] = "VENDINHA C13"
    context["Texto"] = "Seja Bem Vindo"
    return render_template("homepage.html", context=context) #Página a ser renderizada. 


@app.route('/add_produto')
def produto():
    context = {}
   
    return render_template("add_produto.html", context=context) #Página a ser renderizada. 

@app.route('/del_produto')
def del_produto():
    context = {}
   
    return render_template("del_produto.html", context=context) #Página a ser renderizada. 

@app.route('/up_produto')
def up_produto():
    context = {}
   
    return render_template("up_produto.html", context=context) #Página a ser renderizada. 

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
