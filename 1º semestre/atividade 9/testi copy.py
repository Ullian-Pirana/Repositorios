from Login_func import *

sair = 1

while sair == 1:
    escolha = Menu()
    os.system("cls")

    if escolha == 1:
        print("---LOGIN--- \n")
        if len(Usuarios) < 1:
            print("Nenhum cadastro encontrado...")
            clean()
        else:
            Login()
            clean()

    elif escolha == 2:
        cadastro()
        clean()

    elif escolha == 3:
        print("---MUDAR SENHA--- \n")

    elif escolha == 4:
        print("---ALTERAR LOGIN--- \n")

    elif escolha == 5:
        if len(Usuarios) < 1:
            print("Nenhum cadastro encontrado ")
            clean()
        else:
            excluir()

    elif escolha == 6:
        encerrar = int(input("Gostaria de encerrar o programa? \n 1 - Sim \n 2 - Não \n ---> "))

        if encerrar == 1:
            print("SAINDO...")
            escolha = None
            sair = None
            clean()

        elif encerrar == 2:
            clean()
            
        else:
            print("Opção invalida...")
            clean()

    else:
        print("Opção invalida...")
        clean()

os.system("pause")