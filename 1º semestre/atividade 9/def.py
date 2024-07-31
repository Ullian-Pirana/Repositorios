import os


def menu():
    print("--Menu--")
    print("1 - soma")
    print("2 - subtração")
    print("3 - sair")
    x = int(input("Qual opção deseja?\n--->"))
    return x

escolha = menu()

os.system("pause")