import os

sair = 1

while sair == 1:
    
    print("Bem vindo a Piramide Inversa")
    print(" ")

    baseT = int(input("Porfavor insira o valor da base \n --> "))
    print(" ")


    for triangulo in range(baseT, 0, -1):
        print("*" * triangulo)
    print(" ")

    sai = int(input("Gostaria de encerrar o programa? \n 1 pra sim \n 2 pra não \n --> "))
    print(" ")

    if sai == 1:
        sair = 0
        print("ENCERRANDO...")

os.system("pause")