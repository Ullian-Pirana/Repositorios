import os
from Listas import *

def clean():
    os.system("pause")
    os.system("cls")

def menu():

    print("\t \t Tarefas To-Do \n")

    escolha = (int(input("O que gostaria de fazer? \n 1 - Verificar Tarefas \n 2 - Adicionar tarefa \n 3 - Excluir tarefa \n 4 - Encerrar Programa \n \t ---> ")))

    return escolha

def add():

    outra = 1

    while outra == 1:

        print("\t \t ADICIONAR TAREFAS \n")

        add = int(input(("O que gostaria de fazer? \n 1 - Adicionar uma tarefa \n 2 - sair \n ---> ")))

        os.system("pause")
        os.system("cls")

        if add == 1:
            pass    

        elif add == 2:
            print("\t Saindo...")

            os.system("pause")
            os.system("cls")

        else:
            print("\t Opção invalida...")
            
            os.system("pause")
            os.system("cls")