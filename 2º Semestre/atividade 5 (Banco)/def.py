import os

def menu():
    while True:
        print("--- ULL Bank ---")
        print("Seja bem vindo ao ULL Bank, um banco especializado em resolver os seus problemas: \nO que deseja fazer? \n1- Fazer Login \n2- Fazer cadastro")
        while True:
            try:
                escolha = int(input("Qual opção deseja ? \n--> "))
                return escolha
                break
            except Exception as e:
                print(f"Impossivel concluir operação \n erro encontrado: {e}")
                os.system("pause")
                os.system("cls")
                return escolha