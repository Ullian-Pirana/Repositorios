import os
def menu():
    print("---CALCULADORA--- \n")
    print("O que gostaria de fazer? \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair")
    calc = int(input("\n --> "))
    
    return calc 

escolha = menu

os.system ("pause")
os.system("cls")

if escolha == 1:
    def soma(x,y):

        print("---SOMA--- \n")
        x = int(input("insira o numero inicial \n ---> "))
        print(" ")
        y = int(input("insira o valor a ser atribuido \n ---> "))

        valor_soma = x + y

        return valor_soma
    
    print("Resultado = ", soma)
