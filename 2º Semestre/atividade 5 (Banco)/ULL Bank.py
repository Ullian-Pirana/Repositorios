import os 
from Listas import *
from Classes import *
from Defs import *

while True:
    escolha = menu()

    match escolha:
        case 1:
            user = login(cadastros)
            usar = tela_banco(user)



            match usar:
                case 1:
                    if cadastros.__len__() > 0:
                        while True:
                            escolha2 = corrente(user)

                            match escolha2:
                                case 1:
                                    deposito(user)

                                case 2:
                                    pix(user)

                                case 3:
                                    print("Saindo....")

                                    os.system("pause")
                                    os.system("cls")
                                    break

                                case _:
                                    print("Opção invalida...")

                                    os.system("pause")
                                    os.system("cls")

                    else:
                        print("Nenhum cadastro realizado")

                        os.system("cls")

                case 2:
                    poupança(user)

                case _:
                    print("Opção invalida...")

                    os.system("pause")
                    os.system("cls")

        case 2:
            cadastros.append(cadastro())

        case 3:
            print("Saindo...")
            
            os.system("pause")
            os.system("cls")
            break

        case _:
            print("Opção invalida...")