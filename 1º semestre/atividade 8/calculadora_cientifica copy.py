import os

sair = 1

num = []

while sair == 1:
    print("---CALCULADORA CIÊNTIFICA--- \n")
    escolha = int(input("O que gostaria de fazer? \n 1 - SOMA \n 2 - SUBTRAÇÃO \n 3 - DIVISÃO \n 4 - MULTIPLICAÇÃO \n 5 - EXPONENCIAÇÃO \n 6 - FATORAÇÃO \n 7 - SAIR \n ---> "))
    print(" ")
    
    os.system("cls")
    
    if escolha == 1:
        while escolha == 1:

            laço = 0

            while laço == 0:
                print("---SOMA--- \n ")

                soma = float(input("Insira um número: "))
                num.append(float(soma))
                print(" ")

                addsoma = int(input("gostaria de adicionar outro numero a soma? \n 1 - SIM \n 2 - NÃO \n --> "))
                print(" ")

                if addsoma == 1:
                    os.system("cls")
                elif addsoma == 2:
                    laço = 1
                    os.system("cls")
                else:
                    print("Opção invalida...")
                    os.system("pause")
                    os.system("cls")

            total = 0

            for soma2 in num:
                total += soma2
            
            print("---SOMA--- \n ")
            print("Valor total: ", total)
            print(" ")

            escolha2 = int(input("Gostaria de realizar a soma novamente? \n 1 - SIM \n 2 - NÃO \n --> "))
            print(" ")

            if escolha2 == 1:
                os.system("cls")
                num.clear()
                total = 0
            elif escolha2 == 2:
                escolha = None
                num.clear()
                os.system("cls")
            else:
                print("Opção invalida...")
                os.system("pause")
                os.system("cls")

    elif escolha == 2:

        while escolha == 2:

            print("---SUBTRAÇÃO--- \n")
            Vi = float(input("insira um valor inicial: "))
            print(" ")
            os.system("pause")
            os.system("cls")

            laço = 0

            while laço == 0:
                print("---SUBTRAÇÃO--- \n ")

                subtração = float(input("Valor da subtração: "))
                num.append(float(subtração))
                print(" ")

                retirar = int(input("gostaria de subtrair mais? \n 1 - SIM \n 2 - NÃO \n --> "))
                print(" ")

                if retirar == 1:
                    os.system("cls")
                elif retirar == 2:
                    laço = 1
                    os.system("cls")
                else:
                    print("Opção invalida...")
                    os.system("pause")
                    os.system("cls")

            for sub in num:
                Vi -= sub
            
            print("---SUBTRAÇÃO--- \n ")
            print("Valor total: ", Vi)
            print(" ")

            escolha2 = int(input("Gostaria de realizar a subtração novamente? \n 1 - SIM \n 2 - NÃO \n --> "))
            print(" ")

            if escolha2 == 1:
                os.system("cls")
                num.clear()
            elif escolha2 == 2:
                escolha = None
                num.clear()
                os.system("cls")
            else:
                print("Opção invalida...")
                os.system("pause")
                os.system("cls")
    
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
        while escolha == 4:
            print("---MULTIPLICAÇÃO--- \n")
            V1 = float(input("insira um valor inicial: "))
            print(" ")

            os.system("pause")
            os.system("cls")

            rept = 1

            while rept == 1:

                laço = 0

                while laço == 0:
                    print("---MULTIPLICAÇÃO--- \n ")

                    multi = float(input("Valor da Multiplicação: "))
                    num.append(float(multi))
                    print(" ")

                    Multiplicar = int(input("gostaria de Multiplicar mais? \n 1 - SIM \n 2 - NÃO \n --> "))
                    print(" ")

                    if Multiplicar == 1:
                        os.system("cls")
                    elif Multiplicar == 2:
                        laço = 1
                        os.system("cls")
                    else:
                        print("Opção invalida...")
                        os.system("pause")
                        os.system("cls")

                for mult in num:
                    V1 *= multi
                
                print("---MULTIPLICAÇÃO--- \n ")
                print("Valor total: ", V1)
                print(" ")

                escolha2 = int(input("Gostaria de realizar a multiplicação novamente? \n 1 - SIM \n 2 - NÃO \n --> "))
                print(" ")

                if escolha2 == 1:
                    os.system("cls")
                    num.clear()
                    V1 = None
                    rept = 0

                elif escolha2 == 2:
                    escolha = None
                    rept = 0
                    num.clear()
                    os.system("cls")
                else:
                    print("Opção invalida...")
                    os.system("pause")
                    os.system("cls")

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
        while escolha == 6:
            print("---FATORAÇÃO--- \n")
            fatoração = int(input("Insira o numero a ser fatorado: "))
            fato = fatoração
            print(" ")
            print("fatoração de: ", fatoração)
            print(" ")

            n = 0

            for fat in range (1, fatoração):
                n += 1
                calc = fato * fat
                RF = fato * fat
                print("o fatorail de:", fatoração, "*", n, "=", calc)

            print(" ")
            print("Resultado final: ", RF)

            Again = int(input("Gostaria de fatorar outro nomero? \n 1 - Sim \n 2 - Não \n --> "))
            print(" ")

            if Again == 1:
                os.system("pause")
                os.system("cls")
            elif Again == 2:
                escolha = None
                os.system("pause")
                os.system("cls")
            else:
                print("Opção Invalida...")
                os.system("pause")
                os.system("cls")

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