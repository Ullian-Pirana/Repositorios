import os 

Usuarios = []
Senhas = []

def clean():
    os.system("pause")
    os.system("cls")

def Menu():
    print("---INÍCIO--- \n")
    L_C = int(input("O que gostaria de fazer? \n 1 - Login \n 2 - Cadastro \n 3 - Mudar senha \n 4 - Excluir cadastro \n 5 - Sair \n --> "))

    return L_C

def cadastro():
    print("---CADASTRO--- \n")
    log = input("Login/Usuario: ")
    senha = input("Senha: ")
    print(" ")

    Usuarios.append(log)
    Senhas.append(senha)
    print("Cadastro Realizado...")

def Login():
    usuario = input("Usuario: ")
    senha2 = input("Senha: ")
    
    v = -1

    for L in Usuarios:
        v += 1

        if usuario == L:
            if Senhas[v] == senha2:
                print("Login realizado com sucesso! \n")
                clean()

            else:
                print("Senha incorreta...")
                clean()
        else:
            print("Usuario não encontrado... ")
            clean()

def excluir():
    print("---EXCLUIR CADASTRO--- \n")
    delet = input("Usuario: ")
    delet2 = input("Senha: ")

    if delet in Usuarios and delet2 in Senhas:
        confirm = input("Deseja excluir esse cadastro? \n 1 - Sim \n 2 - Não \n --> ")
        print(" ")

        if confirm == 1:
            Usuarios.pop(delet)
            Senhas.pop(delet2)
            print("Usuario excluido...")
            clean()
            
        elif confirm == 2:
            clean()

        else:
            print("Opção invalida... \n ")
            clean()

def alt_senha():
    acess = input("Usuario: ")
    senha3 = input("Senha: ")
    clean()

    ve = -1

    for E in Usuarios:
        ve += 1

        if acess == E:
            if senha3 == Senhas[ve]:
                print("---MUDAR SENHA--- \n")

                nova = input("Nova senha: ")
                confirm = input("Confirme a senha: ")
                print(" ")

                if nova == confirm:
                    Senhas[ve] = nova
                    print("Senha alterada... ")
                    clean()
                else:
                    print("Senha não coincidem!")
                    clean()

            else:
                print("Senha incorreta...")
                clean()
        else:
            print("Usuario não encontrado... ")
            clean()