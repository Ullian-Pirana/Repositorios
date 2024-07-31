import os

sair = 1

while sair == 1:

    print("Imprimindo numeros pares de 0 a 20: ")
    print(" ")

    for num in range(0,21,2):
        print(num)
    
    print(" ")
    sai = int(input("gostaria de encerrar o programa? \n 1 pra sim \n 2 pra não \n --> "))
    print(" ")

    if sai == 1:
        sair = 0
        print("ENCERRANDO...")
os.system("pause")