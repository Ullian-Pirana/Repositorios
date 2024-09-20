import os
from Listas import *

def menu():

    while True:
        print("--- ULL Bank ---")
        print("Seja bem vindo ao ULL Bank, um banco especializado em resolver os seus problemas: \nO que deseja fazer? \n 1- Fazer Login \n 2- Fazer cadastro \n 3 - sair")
        
        while True:
            try:
                escolha = int(input("Qual opção deseja ? \n ---> "))

                os.system("cls")

                return escolha
                break

            except Exception as e:
                print(f"Impossivel concluir operação \n erro encontrado: {e}")

                os.system("pause")
                os.system("cls")
                return escolha