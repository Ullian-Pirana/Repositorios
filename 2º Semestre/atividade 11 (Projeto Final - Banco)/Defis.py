import os
from classis import *

def menu():

    print("O que gostaria de fazer?\n \t 1 - Login\n \t 2 - Cadastrar-se \n \t 3 - Excluir Conta ")

    while True:
        try:
            escolha =  int(input("--> "))

            os.system("cls")
            break

        except Exception as e:                      
            print(f"Impossivel concluir operação \n erro encontrado: {e}")

            os.system("pause")
            os.system("cls")
    
    return escolha












