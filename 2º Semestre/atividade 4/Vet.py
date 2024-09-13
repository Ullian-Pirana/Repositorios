from Defs import *
import os

sair = None
animais = []

while sair != 0:
    escolha = menu()
    os.system("cls")

    match escolha:

        case 1:

            animais.append(cadastro())

        case 2:

            listar(animais)

        case 3:

            consulta(animais)

        case 0:
            print("")
            os.system("pause")
            sair = 0

        case _:
            print("OPÇÃO INVALIDA")
            print("")
            os.system("pause")
            os.system("cls")