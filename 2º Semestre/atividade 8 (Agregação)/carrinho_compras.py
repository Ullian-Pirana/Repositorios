class Cliente:
    
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__carrinho = []

    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getCarrinho(self):
        return self.__carrinho
    
    def setNome(self, nome):
        self.__nome = nome

    def setCpf(self, cpf):
        self.__cpf = cpf

    def addProd(self, compra):
        self.__carrinho.append(compra)

class Produtos:
    
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    def getNome(self):
        return self.__nome
        
    def getValor(self):
        return self.__valor

    def setNome(self, nome):
        self.__nome = nome

    def setValor(self, valor):
        self.__valor = valor
