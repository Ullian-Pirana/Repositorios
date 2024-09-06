from listas import *
import os

def menu():

    print("\t \t  ~~~BRIBRIOTECA DO ALEX~~~ \n")
    print("\t \t ~~BEM VINDO!~~")

    print("""
    \t O que gostaria de fazer?
          1 - Ver livros Disponiveis
          2 - Realizar um emprestimo
          3 - Sair
    """)
    
    escolha = int(input("--> "))

    os.system("cls")

    return escolha

def ver_livro():

    print(" \t Estante de livros: \n ")

    verificar = int(input("Como gostaria de verificar os livros? \n 1 - Ver todos \n 2 - Gênero \n 3 - Autores \t ---> "))

    if verificar == 1:

        posicao = 1

        for item, valor in Estante.itens():
            print(f"{posicao}º - {item}: {valor}")

            posicao += 1

    elif verificar == 2:
        
        print("""\t Gêneros disponiveis:
            Distopia
            Drama
            Fantasia
            Romance
            Fábula
            Mistério/Thriller
            Realismo Mágico
            Ficção Científica
            Aventura
            Existencialismo
            Não-Ficção""")
        
        escolha_gen = input("---> ")

        for chave, valor in Estante.itens():
            if chave == "genero":
                if valor == None:
                    pass



    elif verificar == 3:
        pass

    else:
        print("Opção invalida...")
        os.system("pause")
        os.system("cls")