import os

def menu():
    print("---CALCULADORA--- \n")
    calc = int(input("O que gostaria de fazer? \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair \n --> "))
    
    return calc 

def soma(x,y):
    valor_soma = x + y

    return valor_soma

def sub(x,y):
    valor_sub = x - y

    return valor_sub

def mult(x,y):
    valor_mult = x * y

    return valor_mult

def div(x,y):
    valor_div = x / y

    return valor_div

repit = 1

while repit == 1:

    escolha = menu()

    os.system("cls")

    if escolha == 1:
        while escolha == 1:
            print("---SOMA--- \n")
            x = int(input("insira o numero inicial: "))
            y = int(input("insira o valor a ser atribuido: "))
            print(" ")
            print("Resultado =", soma(x,y))

            os.system ("pause")
            os.system("cls")

            escolha2 = int(input("O que gostaria de fazer agora? \n 1 - Repetir \n 2 - Voltar ao menu \n 3 - Encerrar \n ---> "))
            print(" ")

            if escolha2 == 1:
                x = None
                y = None 
                os.system("cls") 

            elif escolha2 == 2:
                x = None
                y = None
                escolha = None
                os.system("cls")

            elif escolha2 == 3:
                os.system("cls")
                sair = int(input("Gostaria de encerrar o programa? \n 1 - Sim \n 2 - Não \n ---> "))

                if sair == 1:
                    print("SAINDO...")
                    escolha = None
                    os.system("pause")
                    os.system("cls")

                elif sair == 2:
                    os.system("pause")
                    os.system("cls")
                    
                else:
                    print("Opção invalida...")
                    os.system("pause")
                    os.system("cls")

    elif escolha == 2:
        while escolha == 2:
            print("---SUBTRAÇÃO--- \n")
            x = int(input("insira o numero inicial: "))
            y = int(input("insira o valor a ser subtraido: "))
            print(" ")
            print("Resultado =", sub(x,y))

            os.system ("pause")
            os.system("cls")

            escolha2 = int(input("O que gostaria de fazer agora? \n 1 - Repetir \n 2 - Voltar ao menu \n 3 - Encerrar \n ---> "))
            print(" ")
            
            if escolha2 == 1:
                x = None
                y = None 
                os.system("cls") 

            elif escolha2 == 2:
                x = None
                y = None
                escolha = None
                os.system("cls")

            elif escolha2 == 3:
                os.system("cls")
                sair = int(input("Gostaria de encerrar o programa? \n 1 - Sim \n 2 - Não \n ---> "))

                if sair == 1:
                    print("SAINDO...")
                    escolha = None
                    os.system("pause")
                    os.system("cls")

                elif sair == 2:
                    os.system("pause")
                    os.system("cls")
                    
                else:
                    print("Opção invalida...")
                    os.system("pause")
                    os.system("cls")

    elif escolha == 3:
        while escolha == 3:
            print("---MULTIPLICAÇÃO--- \n")
            x = int(input("insira o numero inicial: "))
            y = int(input("insira o valor pelo qual será multiplicado: "))
            print(" ")
            print("Resultado =", mult(x,y))

            os.system ("pause")
            os.system("cls")

            escolha2 = int(input("O que gostaria de fazer agora? \n 1 - Repetir \n 2 - Voltar ao menu \n 3 - Encerrar \n ---> "))
            print(" ")
            
            if escolha2 == 1:
                x = None
                y = None 
                os.system("cls") 

            elif escolha2 == 2:
                x = None
                y = None
                escolha = None
                os.system("cls")

            elif escolha2 == 3:
                os.system("cls")
                sair = int(input("Gostaria de encerrar o programa? \n 1 - Sim \n 2 - Não \n ---> "))

                if sair == 1:
                    print("SAINDO...")
                    escolha = None
                    os.system("pause")
                    os.system("cls")

                elif sair == 2:
                    os.system("pause")
                    os.system("cls")
                    
                else:
                    print("Opção invalida...")
                    os.system("pause")
                    os.system("cls")
         
    elif escolha == 4:
        while escolha == 4:
            print("---DIVISÃO--- \n")
            x = int(input("insira o numero inicial: "))
            y = int(input("insira o valor pelo qual sera dividido: "))
            print(" ")
            print("Resultado =", div(x,y))

            os.system ("pause")
            os.system("cls")

            escolha2 = int(input("O que gostaria de fazer agora? \n 1 - Repetir \n 2 - Voltar ao menu \n 3 - Encerrar \n ---> "))
            print(" ")
            
            if escolha2 == 1:
                x = None
                y = None 
                os.system("cls") 

            elif escolha2 == 2:
                x = None
                y = None
                escolha = None
                os.system("cls")

            elif escolha2 == 3:
                os.system("cls")
                sair = int(input("Gostaria de encerrar o programa? \n 1 - Sim \n 2 - Não \n ---> "))

                if sair == 1:
                    print("SAINDO...")
                    escolha = None
                    os.system("pause")
                    os.system("cls")

                elif sair == 2:
                    os.system("pause")
                    os.system("cls")
                    
                else:
                    print("Opção invalida...")
                    os.system("pause")
                    os.system("cls")
         
    elif escolha == 5:
        sair = int(input("Gostaria de encerrar o programa? \n 1 - Sim \n 2 - Não \n ---> "))

        if sair == 1:
            print("SAINDO...")
            escolha = None
            os.system("pause")
            os.system("cls")

        elif sair == 2:
            os.system("pause")
            os.system("cls")
            
        else:
            print("Opção invalida...")
            os.system("pause")
            os.system("cls")
os.system("pause")