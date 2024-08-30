from pet_classes import *
import os

pet = int(input("qual animal gostaria de adotar? \n 1 - gato \n 2 - cachorro \n --> "))
os.system("cls")

if pet == 1:
    
    cat = input("qual o nome do seu gato? \n -> ")
    os.system("cls")

    nomeG = cat
    nomeG = gato(f"{nomeG}")

    acao = int(input("o que um gato faz? \n 1 - se move \n 2 - se alimenta \n 3 - muda de nome \n 4 - diz o proprio nome \n --> "))
    os.system("cls")

    if acao == 1:
        nomeG.parkour()
        os.system("pause")

    elif acao == 2:
        nomeG.alimento
        os.system("pause")

    elif acao == 3:
        nomeG.mudar_nome
        os.system("pause")

    elif acao == 4:
        nomeG.pegar_nome
        os.system("pause")

    else:
        print("opção invalida...")
        os.system("cls")

elif pet == 2:

    dog = input("qual o nome do seu cachorro? \n -> ")
    os.system("cls")

    nomeC = dog
    nomeC = cachorro(f"{nomeC}")

    acao = int(input("o que o cachorro faz? \n 1 - late \n 2 - defeca \n 3 - se alimenta \n 4 - muda de nome \n 5 - fala o proprio nome \n --> "))

    if acao == 1:
        nomeC.latir()
        os.system("pause")

    elif acao == 2:
        nomeC.cagar()
        os.system("pause")

    elif acao == 3:
        nomeC.alimento()
        os.system("pause")

    elif acao == 4:
        nomeC.mudar_nome()
        os.system("pause")

    elif acao == 5:
        nomeC.pegar_nome()
        os.system("cls")

    else:
        print("opção invalida...")
        os.system("cls")

else:

    print("opção invalida...")
    os.system("cls")