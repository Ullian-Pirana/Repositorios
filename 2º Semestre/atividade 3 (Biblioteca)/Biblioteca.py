from class_bib import *
from defs_bib import *
from listas import *
import os

sair = None

while sair != 1:
    
    escolha = menu()

    if escolha == 1:

        ver_livro()

    elif escolha == 2:
        pass

    elif escolha == 3:
        print("\ t Tem certeza que deseja sair? \n 1 - Sim \n 2 - Não")

        ctz = int(input("---> "))

        if ctz == 1:

            print("Saindo...")

            sair = 1

            os.system("pause")
            os.system("cls")

        elif ctz == 2:

            print(".....")

            os.system("pause")
            os.system("cls")

        else:
            print("Opção invalida...")

            os.system("pause")
            os.system("cls")

    else:
        
        print("Opção invalida...")

        os.system("pause")
        os.system("cls")