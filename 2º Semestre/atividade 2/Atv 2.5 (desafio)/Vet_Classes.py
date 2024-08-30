from Vet_Lists import *
import os


class Gato:
    
    def __init__(self, nome, raca, dono, idade):

        self.nome = nome
        self.raca = raca
        self.dono = dono
        self.idade = idade

    def diagnostico(self, escrever):
        
        escrever = input("qual o Diagnostico do animal?\n \t --> ")

        self.diag = escrever
        os.system("cls")

        print("Diagnostico realizado!")
        os.system("pause")
        os.system("cls")

    def getName(self):
        return self.nome

class Cachorro:
    
    def __init__(self, nome, raca, dono, idade):

        self.nome = nome
        self.raca = raca
        self.dono = dono
        self.idade = idade

    def diagnostico(self, escrever):
        
        escrever = input("qual o Diagnostico do animal?\n \t --> ")

        self.diag = escrever
        os.system("cls")

        print("Diagnostico realizado!")
        os.system("pause")
        os.system("cls")

    def getName(self):
        return self.nome