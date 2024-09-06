import os

#Classe de emprestimo
class emprestimo:
    #Construtor
    def __init__(self, livro, DDE, DDD, NC, Contato):
        self.livro = livro
        self.DDE = DDE #Data de empréstimo
        self.DDD = DDD #Data de devolução
        self.NC = NC #Nome completo
        self.Contato = Contato #Contanto do usuário

    def getLivro(self):
        return self.livro
        
    def setLivro(self, livro):
        self.livro = livro

    def getDDE(self):
        return self.DDE
    
    def setDDE(self, DDE):
        self.DDE = DDE
        
    def getDDD(self):
        return self.DDD
    
    def setDDD(self,DDD):
        self.DDD = DDD

    def getNC(self):
        return self.NC

    def setNC(self, NC):
        self.NC = NC   

    def getContato(self):
        return self.Contato
    
    def setContato(self, contato):
        self.contato = contato
        