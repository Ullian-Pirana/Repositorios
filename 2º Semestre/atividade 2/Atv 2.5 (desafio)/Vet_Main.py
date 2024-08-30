from Vet_Classes import *
from Vet_Lists import *
import os

escolha = 0

while escolha != None:

    print("""\t \t \t ~~~viVETerinaria~~~
          \t \t     ~BEM VINDO!~""")
    
    escolha = int(input("O que veio fazer hoje? \n 1 - cadastrar um Pet \n 2 - verificar um pet \n 3 - sair \n ---> "))
    os.system("cls")

    if escolha == 1:
        
        QPet = int(input("O pet é um gato ou um cachorro? \n 1 - Gato \n 2 - Cachorro \n ---> "))
        os.system("cls")

        if QPet == 1:
            
            CN = input("Qual o nome do Gato? \n --> ")
            CR = input("Qual a raça do Gato? \n --> ")
            CD = input("Qual o nome do dono do Gato? \n --> ")
            CI = input("Qual a idade do Gato? \n --> ")

            Cat = CN

            gatos.append(Cat)

        elif QPet == 2:
            
            DN = input("Qual o nome do Cachorro? \n --> ")
            DR = input("Qual a raça do Cachorro? \n --> ")
            DD = input("Qual o nome do dono do Cachorro? \n --> ")
            DI = input("Qual a idade do Cachorro? \n --> ")

            DOG = DN

            dog.append(DOG)

            cat = ()

        else:
            
            print("Opção invalida...")
            os.system("pause")
            os.system("cls")    


    elif escolha == 2:
        pass

    elif escolha == 3:
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