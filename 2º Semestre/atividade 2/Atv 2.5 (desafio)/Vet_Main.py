from Vet_Classes import *
import os

escolha = 0

while escolha != None:

    print("""\t \t \t ~~~viVETerinaria~~~
          \t \t     ~BEM VINDO!~""")
    
    escolha = int(input("O que veio fazer hoje? \n 1 - cadastrar um Pet \n 2 - verificar um pet \n 3 - retirar um pet \n 4 - sair \n ---> "))
    os.system("cls")

    if escolha == 1:
        
        QPet = int(input("O pet é um gato ou um cachorro? \n 1 - Gato \n 2 - Cachorro \n ---> "))

        if QPet == 1:
            pass

        elif QPet == 2:
            pass

        else:
            
            print("Opção invalida...")
            os.system("pause")
            os.system("cls")    


    elif escolha == 2:
        pass

    elif escolha == 3:
        pass

    elif escolha == 4:
        sair = int(input("realmente deseja encerrar o programa? \n 1 - Sim \n 2 - Não \n --> "))

        if sair == 1:

            print("Saindo...")

            escolha = None

            os.system("pause")
            os.system("cls")

        elif sair == 2:

            print("Retornando ao menu...")
            os.system("pause")
            os.system("cls")

        else:
            
            print("Opção invalida...")
            os.system("pause")
            os.system("cls")
    
    else:
        print("Opção invalida...")
        os.system("pause")
        os.system("cls")