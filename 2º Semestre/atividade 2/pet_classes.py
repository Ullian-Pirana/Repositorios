import os

class gato:

    def __init__(self, nome):
        self.nome = nome

    def parkour(self):
        print("frente, esquerda, pula, pula, zigzag, derrapa, corre...")

    def alimento(self):

        oque = int(input("vai comer ou beber? \n 1 - comer \n 2 - beber \n --> "))
        os.system("cls")

        if oque == 1:
            print("nham nham")

        elif oque == 2:
            print("glub glub")

        else:
            print("opção invalida")

    def mudar_nome(self, novo_nome):

        troca = input("qual o novo nome? \n -> ")

        novo_nome = troca

        self.nome = novo_nome

        print(self.nome)

    def pegar_nome(self):
        return self.nome

class cachorro:

    def __init__(self, nome2):
        self.nome = nome2        

    def latir(self):
        print("Au Au Au")

    def cagar(self):
        print("plop")

    def alimento(self):

        oque = int(input("vai comer ou beber? \n 1 - comer \n 2 - beber \n --> "))
        os.system("cls")

        if oque == 1:
            print("nham nham")

        elif oque == 2:
            print("glub glub")

        else:
            print("opção invalida")

    def mudar_nome(self, novo_nome2):

        troca = input("qual o novo nome? \n -> ")

        novo_nome2 = troca

        self.nome = novo_nome2

        print(self.nome)

    def pegar_nome(self):
        return self.nome