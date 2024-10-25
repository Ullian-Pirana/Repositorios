from abc import *

class Conta(ABC):
    def __init__(self):
        self.__saldo = 0.00

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
    def __init__(self):
        super().__init__()

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

class Cliente:
    def __init__(self,nome: str,cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []

    def addConta(self, conta: Conta):
        self.__contas.append(conta)

    def rmvConta(self, conta: Conta):
        if conta in self.__contas:
            self.__contas.remove(conta)
        else:
            print("Conta não encontrada...")

class Extrato:
    def __init__(self):
        self.__trasacoes = []

    def add_transacao(self,descricao: str,valor: float):
        transacao = f"Descrição: {descricao} \n Valor: {valor}"

        self.__trasacoes.append(transacao)

    def consultar_extratos(self):
        return self.__trasacoes 





