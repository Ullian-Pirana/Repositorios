import os
from Listas import *

def clean():
    os.system("pause")
    os.system("cls")

def menu():

    print("\t \t Tarefas To-Do \n")

    escolha = (int(input("O que gostaria de fazer? \n 1 - Verificar Tarefas \n 2 - Adicionar tarefa \n 3 - Excluir tarefa \n 4 - Encerrar Programa \n \t ---> ")))

    return escolha

