from funcoes_calc import *
import os

sair = 1

while sair == 1:

    escolha = menu()
    os.system("cls")

    if escolha == 5:
        print("SAINDO....")
        sair = None

    else:

        x = float(input("valor 1: "))
        y = float(input("valor 2: "))

        if escolha == 1:
            print(f"O resultado da Soma é: {soma(x,y)}")
            pshipshi()

        elif escolha == 2:
            print(f"O resultado da Subtração é: {sub(x,y)}")
            pshipshi()

        elif escolha == 3:
            print(f"O resultado da Multiplicação é: {mult(x,y)}")
            pshipshi()

        elif escolha == 4:
            print(f"O resultado da Divisão é: {div(x,y)}")
            pshipshi()
os.system("pause")