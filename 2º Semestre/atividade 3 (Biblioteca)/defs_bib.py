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

    return escolha