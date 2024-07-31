from forca_func import *

sair = 1

while sair == 1:
    escolha = menu()
    stop()

    if escolha == 1:
        add()
        stop()

    elif escolha == 2:
        if len(palavras) > 0:
            while escolha == 2:
                play()
                stop()
        else:
            print("Nenhuma palavra cadastrada... \n")
            stop()


    elif escolha == 3:
        while escolha == 3:
            print("---Sair da forca--- \n")
            sai = int(input("Gostaria de sair do jogo? \n 1 - SIM \n 2 - NÃO \n --->"))
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
        print("Opção invalida... ")
        stop()