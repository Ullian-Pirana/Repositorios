class pessoa:

    def __init__(self, nome):
        self.nome = nome
        
    def andar(self):
        print("andando")

    def falar(self):
        print("bla bla bla")

    def setname(self, novo_nome):
        self.nome = novo_nome

        print(self.nome)

    def getname(self):
        return self.nome