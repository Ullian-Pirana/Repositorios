import os

sair = 1

num = []

while sair == 1:
    print("---CALCULADORA CIÊNTIFICA--- \n")
    escolha = int(input("O que gostaria de fazer? \n 1 - SOMA \n 2 - SUBTRAÇÃO \n 3 - DIVISÃO \n 4 - MULTIPLICAÇÃO \n 5 - EXPONENCIAÇÃO \n 6 - FATORAÇÃO \n 7 - SAIR \n ---> "))
    print(" ")
    
    os.system("cls")
    
    if escolha == 1:
        print("---SOMA---")

    elif escolha == 2:
        print("---SUBTRAÇÃO---")

    elif escolha == 3:
        while escolha == 3:
            print("---DIVISÃO--- \n")
            
            dividendo = float(input("Numero a ser dividido: "))
            divisor = float(input("Quantidade a ser dividido:"))
            print(" ")
            print(dividendo, "÷", divisor, "=", dividendo/divisor)
            print(" ")

            laço = 0

            while laço == 0:

                repetir = int(input("Gostaria de realizar a divisão novamente? \n 1 - SIM \n 2 - NÃO \n --> "))
                print(" ")
                
                if repetir == 1:
                    laço = 1
                    os.system("cls")

                elif repetir == 2:
                    escolha = None
                    laço = 1
                    os.system("cls")

                else:
                    print("Opção invalida...")
                    os.system("pause")
                    os.system("cls")

    elif escolha == 4:
        print("---MULTIPLICAÇÃO---")

    elif escolha == 5:
        while escolha == 5:
            print("---EXPONENCIAÇÃO--- \n")

            exponencial = float(input("Insira um numero: "))
            elevação = int(input("Valor a ser elevado: "))
            print(" ")
            print(exponencial, "^", elevação, "=", exponencial**elevação)
            print(" ")

            laço = 0

            while laço == 0:

                repetir = int(input("Gostaria de realizar a exponenciação novamente? \n 1 - SIM \n 2 - NÃO \n --> "))
                print(" ")
                    
                if repetir == 1:
                    laço = 1
                    os.system("cls")

                elif repetir == 2:
                    escolha = None
                    laço = 1
                    os.system("cls")

                else:
                    print("Opção invalida...")
                    os.system("pause")
                    os.system("cls")

    elif escolha == 6:
        print("---FATORAÇÃO--- \n")
        fatoração = int(input("Insira o numero a ser fatorado: "))


    elif escolha == 7:
        encerrar = int(input("Gostaria de encerrar o programa? \n 1 - SIM \n 2 - NÃO \n ---> "))
        print(" ")

        if encerrar == 1:
            print("Encerrando...")
            sair = 0
        else:
            print(" ")
            os.system("pause")
            os.system("cls")
    else:
        print("Opção invalida... \n")



os.system("pause")