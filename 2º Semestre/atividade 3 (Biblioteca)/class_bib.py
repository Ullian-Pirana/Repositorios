from listas import *
import os

#Classe de emprestimo
class Cliente:
    #Construtor
    def __init__(self, NC, livro, DDE, DDD, Contato):
        
        self.NC = NC #Nome cliente
        self.livro = livro #livro emprestado
        self.DDE = DDE #Data de empréstimo
        self.DDD = DDD #Data de devolução
        self.Contato = Contato #Contanto do usuário

    def getLivro(self): #Retornar o  valor 
        return self.livro 
        
    def setLivro(self, livro): #Adicionar um valor
        self.livro = livro

    def getDDE(self): #Retornar o  valor 
        return self.DDE
    
    def setDDE(self, DDE):#Adicionar um valor
        self.DDE = DDE
        
    def getDDD(self): #Retornar o  valor 
        return self.DDD
    
    def setDDD(self,DDD): #Adicionar um valor
        self.DDD = DDD

    def getNC(self):   #Retornar o  valor 
        return self.NC

    def setNC(self, NC): #Adicionar um valor
        self.NC = NC   

    def getContato(self):  #Retornar o  valor 
        return self.Contato
    
    def setContato(self, contato): #Adicionar um valor
        self.contato = contato
        
