import os

sair = 1

while sair == 1:
    print("---É DIVISIVEL (3/5)? \n")
    num =  int(input("Porfavor insira um numero inteiro: "))
    print(" ")
    os.system("pause")
    os.system("cls")

    print("Obs: Uma palavra especifica aparecerá caso seja possivel divir pelos seguintes numeros: \n 3 --> SENAI \n 5 --> JUNDIAÍ \n 3 e 5 --> SenaiJundiaí \n ")
    
    os.system("pause")
    os.system("cls")

    for D in range (1, num +1):

        if D%3 == 0 and D%5 == 0:
            print("SenaiJundiaí")

        elif D%5 == 0:
            print("JUNDIAÍ")

        elif D%3 == 0:
            print("SENAI")

        else:
            print(D)

    os.system("pause")
    os.system("cls")
    repet = 1

    while repet == 1:
        print(" ")
        F4 = int(input("Gostaria de sair? \n 1 - Sim \n 2 - Não \n --> "))
        print(" ")

        if F4 == 1: 
            print("Saindo...")
            repet = 0
            sair = 0
            os.system("pause")
            os.system("cls")

        elif F4 == 2: 
            repet = 0
            os.system("pause")
            os.system("cls")

        else:
            print("Opção invalida...")
            os.system("pause")
            os.system("cls")