import os

sair = 1

while sair == 1:
    
    print("Bem vindo a Contagem regressiva.exe")
    print(" ")

    inicio = int(input("Porfavor insira o numero inicial \n --> "))
    print(" ")
    fim = int(input("Porfavor insira o ultimo numero \n --> "))
    print(" ")
    inter = int(input("Porfavor insira o intervalo de tempo \n --> "))
    print(" ")

    for contagem in range(inicio, fim , inter):
        print(contagem)
    print(" ")

    sai = int(input("Gostaria de encerrar o programa? \n 1 pra sim \n 2 pra não \n --> "))
    print(" ")

    if sai == 1:
        sair = 0
        print("ENCERRANDO...")

os.system("pause")