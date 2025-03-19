from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def homepage():
    context = {}
    context["logo"] =   "img/Sernesto.jpeg"
    context["img"] =   "img/ernesto.jpg"
    context["Titulo"] = "El venta de Ernesto"
    context["Texto"] = "Bienvenido a la venta de Ernesto, Ernesto está orgulloso de usted, continúe con el buen trabajo, joven caballero. Recuerda nunca desviarte del camino del negocio, roba a tus clientes siempre que puedas."
    return render_template("homepage.html", **context) #Página a ser renderizada. 


@app.route('/add_produto')
def produto():
    context = {}
    produtos={}
    context["logo"] = "img/Sernesto.jpeg"
    produtos[1] = "Arroz"
    produtos[2] = "Macarrão"
    produtos[3] = "Leite"
    context["Titulo_add"] = "El Produtos de ERNESTO"
    context  ["produtos"] = produtos
    context["img_add1"] =   "img/arroz.jpg"
    context["img_add2"] =   "img/Macarrão.png"
    context["img_add3"] =   "img/leite.jpeg"
    return render_template("add_produto.html", **context) #Página a ser renderizada. 

@app.route('/del_produto')
def del_produto():
    context = {}
    context["logo"] = "img/Sernesto.jpeg"
  
   
    return render_template("del_produto.html", **context) #Página a ser renderizada. 

@app.route('/up_produto')
def up_produto():
    context = {}
    context["logo"] =   "img/Sernesto.jpeg"
    return render_template("up_produto.html", context=context) #Página a ser renderizada. 

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
