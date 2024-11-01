import os
from classis import *
from Defis import *

Ull = Banco()

while True:
    escolha = menu () 

    match escolha: 
        case 1:
            usuario = login(Ull)
            conta = tela_banco(usuario)

            while True:
                match conta:
                    case 1:
                        conta_corrente(usuario, Ull)
                    case 2:
                        conta_poupanca(usuario)
                    case 3:
                        verExtratos(usuario)
                    case 4:
                        print("Saindo...")
                        os.system("pause")
                        os.system("cls")
                        break
                    case _:
                            print("opção invalida...")
                            os.system("pause")
                            os.system("cls")
        case 2:
            cadastro(Ull)

        case 3:
            excluir(Ull)

        case 4:
            print("Saindo...")
            os.system("pause")
            os.system("cls")
            break

        case _:
            print("opção invalida...")
            os.system("pause")
            os.system("cls")