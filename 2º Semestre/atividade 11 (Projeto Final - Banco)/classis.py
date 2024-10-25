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
    
class ContaCorrente(Conta):
    def __init__(self, saldo: float):
        super().__init__(saldo)

    def sacar (self, valor: float):
        saque = self.__saldo - valor

        if saque > 0.00:
            self.__saldo = saque

        else:
            print("Saldo insuficiente...")
            
class ContaPoupanca(Conta):
    def __init__(self, saldo: float):
        super().__init__(saldo)

    def sacar (self, valor: float):
        saque = self.__saldo - valor

        if self.__saldo > 100.00:
            if saque > 0.00:
                self.__saldo = saque

            else:
                print("Saldo insuficiente...")
        else:
            print("Requisitos de saque não atendidos...")