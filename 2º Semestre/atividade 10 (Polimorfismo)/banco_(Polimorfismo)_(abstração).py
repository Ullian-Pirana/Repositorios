from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self):
        self.__tipo = None
        self.__saldo = 0.0  

    @abstractmethod #Abstração

    def tipo(self):
        pass 

    def getTipo(self):
        return self.__tipo

    def setSaldo(self, saldo: float):
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo

class Corrente(Conta):
    def tipo(self):
        self._Conta__tipo = "Conta Corrente" 

class Poupança(Conta):
    def tipo(self):
        self._Conta__tipo = "Conta Poupança"

pou = Poupança()
pou.tipo()  
corrente = Corrente()
corrente.tipo() 

print(pou.getTipo())
print(corrente.getTipo())