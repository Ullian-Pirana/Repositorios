import os

sair = 1

while sair == 1:
    
    print("Bem vindo a tabuada em python")
    print(" ")

    numero = int(input("De qual numero você gostaria de ver a tabuada? \n --> "))
    print(" ")
    multi = int(input("Até qual multiplo você gostaria de ir? \n --> "))

    for tabu in range(1, multi + 1):
        print(tabu, "*", numero, "=", tabu*numero)

    print(" ")
    sai = int(input("Gostaria de encerrar o programa? \n 1 pra sim \n 2 pra não \n --> "))
    print(" ")

    if sai == 1:
        sair = 0
        print("ENCERRANDO...")

os.system("pause")