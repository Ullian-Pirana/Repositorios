import os
from Listas import *

def clean():
    os.system("pause")
    os.system("cls")

def menu():

    print("\t \t Tarefas To-Do \n")

    escolha = (int(input("O que gostaria de fazer? \n 1 - Adicionar tarefa \n 2 - Verificar Tarefas  \n 3 - Excluir tarefa \n 4 - Encerrar Programa \n \t ---> ")))

    return escolha

def add():

    outra = 1

    while outra == 1:

        print("\t \t ADICIONAR TAREFAS \n")

        add = int(input(("O que gostaria de fazer? \n 1 - Adicionar uma tarefa \n 2 - sair \n ---> ")))

        os.system("pause")
        os.system("cls")

        
        if add == 1:
            while add == 1:

                print("\t \t Adionacar Tarefa: \n")

                titulo = input(" insira o Titulo da tarefa: ")
                desc = input("\n insira a Descrição da tarefa: ")
                date = input("\n insira a Data da tarefa: ")

                nome.append(titulo)
                descrição.append(desc)
                data.append(date)

                print("\n \t Tarefa adicionada...")

                os.system("pause")
                os.system("cls")

                outro = int(input("Gostaria de adicionar outra tarefa? \n 1 - Sim \n 2 - Não \n ---> "))

                if outro == 1:

                    os.system("pause")
                    os.system("cls")

                elif outro == 2:

                    print("\n \t Voltando ao menu... \n")

                    add = 0
                    outra = 0

                    os.system("pause")
                    os.system("cls")

                else:

                    print("\t Opção invalida... ")

                    os.system("pause")
                    os.system("cls")

        elif add == 2:
            print("\t Saindo...")

            outra = 0

            os.system("pause")
            os.system("cls")

        else:
            print("\t Opção invalida...")
            
            os.system("pause")
            os.system("cls")

def ver():

    lista = 1

    while lista == 1:

        print("\t \t Lista Das Tarefas: ")

        escolha = int(input("O que gostaria de fazer? \n 1 - ver as tarefas \n 2 - Sair \n ---> "))

        os.system("pause")
        os.system("cls")

        if escolha == 1:

            print("\t \t TAREFAS: \n ")

            for chave, valor in Tarefas.items():
                
                posição = 1

                print(f"\t {chave}: \n")

                for quantia in valor:
                    print(f"{posição}º -- {quantia} \n")
                    posição += 1

            os.system("pause")
            os.system("cls")

        elif escolha == 2:
            
            print("\t SAINDO... \n")

            lista = 0

            os.system("pause")
            os.system("cls")

        else:
            print("\t Opção invalida...")

            os.system("pause")
            os.system("cls")



