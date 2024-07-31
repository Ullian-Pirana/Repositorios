import os

sair = 1

while sair == 1:

    print("Imprimindo numeros de 1 a 10: ")
    print(" ")

    for num in range(1,11,1):
        print(num)
    
    print(" ")
    sai = int(input("gostaria de encerrar o programa? \n 1 pra sim \n 2 pra não \n --> "))
    print(" ")

    if sai == 1:
        sair = 0
        print("ENCERRANDO...")
os.system("pause")