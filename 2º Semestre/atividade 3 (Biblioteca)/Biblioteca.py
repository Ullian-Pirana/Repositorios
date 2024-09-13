from class_bib import * #Importação Pagina das Classes "class_bib"
from defs_bib import * #Importação Pagina dos defs "defs_bib"
from listas import * #Importação Pagina das listas "listas"
import os

sair = None


while sair != 1: 
    
    escolha = menu()

    if escolha == 1:

        ver_livro()

    elif escolha == 2:
        
        emprestar()

    elif escolha == 3:
        livros.append(cadastro())
        autores.append(cadastro2())
        genero.append(cadastro3())
        escolha = menu()
    elif escolha == 4:
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