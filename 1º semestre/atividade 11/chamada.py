from chamada_def import *

sair = 1

while sair == 1:

    escolha = menu()
    stop()

    if escolha == 1:
       presença()
       stop()

    elif escolha == 2:

        while escolha == 2:

            sai = int(input("Gostaria de Encerrar o Programa? \n 1 - SIM \n 2 - NÃO \n --->"))
            print(" ")

            if sai == 1:
                escolha = None
                print("Saindo...")
                sair = 0
                stop()

            elif sai == 2:
                escolha = None
                stop()
                
            else:
                print("Opção invalida...")
                stop()

    else:
        print("Opção Invalida...")
        stop()