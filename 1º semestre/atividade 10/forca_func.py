import os, random

palavras = []
acertos = []
erros = []

def stop():
    os.system("pause")
    os.system("cls")

def menu():
    print("---JOGO DA FORCA--- \n")
    jogar = int(input("Selecione uma das opções: \n 1 - Adicionar uma palavra ao jogo \n 2 - Jogar \n 3 - Sair \n ---> "))
    print(" ")
    print("(OBS: No jogo as palavras serão escolhidas aleatoriamente!)")

    return jogar

def add():
    print("---ADICIONAR PALAVRA--- \n")

    adicionar = input("Insira a palavra: ")
    palavras.append(adicionar)
    print(" ")
    print("Palavra adicionada! \n ")

def play():
    print("---JOGAR--- \n")

    vidas = 6
    palavra_escolha = random.choice(palavras)
    print(f"Dica: a palavra tem {len(palavra_escolha)} letras \n ")

    jogo = 1

    while jogo == 1:
        if vidas > 0:
        
            print(f"acertos: {acertos}")
            print(f"erros: {erros}")
            print(f"Vidas restantes: {vidas} \n")

            escol = int(input("O que gostaria de tantar? \n 1 - Palavra  \n 2 - Letra \n --> "))
            print(" ")

            if escol == 1:
                Palavra = input("Insira a palavra: ")
                print(" ")

                if Palavra == palavra_escolha:
                    print("~~~~VOCÊ GANHOU!!!~~~ \n")
                    print("você acertou a palavra!!! \n")
                    print(f"A palavra era {palavra_escolha}!!!")

                    jogo = 0

                    os.system("pause")
                    os.system("cls")

                else:
                    print("Palavra não coincide... \n vida -1 \n")
                    vidas -= 1
                    os.system("pause")
                    os.system("cls")


            elif escol == 2:

                letra = input("Insira uma letra: ")
                print(" ")

                if letra in palavra_escolha:
                    print("Você acertou uma letra!~ \n ")

                    acertos.append(letra)

                    os.system("pause")
                    os.system("cls")
                else:
                    print("A letra não está na palavra T-T \n vida -1")

                    erros.append(letra)
                    vidas -= 1

                    os.system("pause")
                    os.system("cls")

        else:
            print("Você perdeu! \n ")
            print(f"A palavra correta era: {palavra_escolha}")

            jogo = 0
            
            os.system("pause")
            os.system("cls")