import os 
from Classes import *
from Defs import *

while True:
    escolha = menu()

    match escolha:
        case 1:
            user = login()
            usar = tela_banco(user)

            match usar:
                case 1:
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

                case 2:
                    poupança(user)

                case _:
                    print("Opção invalida...")

                    os.system("pause")
                    os.system("cls")

        case 2:
            cadastro = cadastro()

        case 3:
            print("Saindo...")
            
            os.system("pause")
            os.system("cls")
            break

        case _:
            print("Opção invalida...")