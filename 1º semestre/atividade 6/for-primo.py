import os

sair = 1

while sair == 1:
    
    print("""---Bem vindo ao verificador de numero primo---""")
    print(" ")

    escolha = int(input("Gostaria de verificar se um numero é primo? \n 1 pra sim \n 2 pra não \n --> "))
    print(" ")

    if escolha == 1:
     NumP = int(input("Porfavor insira um numero \n --> "))
     print(" ")

     verificar = 0

     for div in range(1, NumP + 1):

        calc = NumP%div
        if calc == 0:
            verificar += 1

     if verificar == 2:
        print("O numero é primo")
        print(" ")
     else:
        print("O numero não é primo")
        print(" ")

    elif escolha == 2:
       sair = 0
       print("ENCERRANDO...")

    else:
       print("Opção invalida...")
       print(" ")

    sai = int(input("Gostaria de encerrar o programa? \n 1 pra sim \n 2 pra não \n --> "))
    print(" ")

    if sai == 1:
        sair = 0
        print("ENCERRANDO...")


os.system("pause")