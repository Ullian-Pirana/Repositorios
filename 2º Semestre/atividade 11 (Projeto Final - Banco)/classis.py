from abc import *

class Conta(ABC):
    def __init__(self, saldo: float):
        self.__saldo = saldo

    @abstractmethod
    def depositar(self, valor : float):
        self.__saldo += valor
    
    def sacar(self, valor : float):
        self.__saldo -= valor

    def transferir(self, conta_destino, valor: float):
        conta_destino += valor
        self.__saldo -= valor

    def consultar_saldo (self):
        return self.__saldo