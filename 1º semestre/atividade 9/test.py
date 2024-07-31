usuarios = []
senhas = []

def cadastrar_usuario(usuario, senha):
    usuarios.append(usuario)
    senhas.append(senha)
    print("Usuário cadastrado com sucesso!")

cadastrar_usuario()

def login(usuario, senha):
    for i in range(len(usuarios)):
        if usuarios[i] == usuario and senhas[i] == senha:
            print("Login bem sucedido!")
            return True
    print("Falha no login. Usuário ou senha incorretos.")
    return False

cadastrar_usuario("user1", "senha1")
login("user1", "senha1")
