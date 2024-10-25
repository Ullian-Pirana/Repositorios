from abc import *

class Conta(ABC):
    def __init__(self):
        self.__saldo = 0.00
        self.__extrato = Extrato()

    @abstractmethod
    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            self.__extrato.add_transacao("Depósito", valor)
    
    def sacar(self, valor : float):
        self.__saldo -= valor

    def transferir(self, conta_destino, valor: float):
        if valor > 0 and valor <= self.__saldo:
            self.sacar(valor)
            self.__extrato.add_transacao(f"Transferência para {conta_destino} no valor de R${valor}")
        else:
            print("Valor inválido para transferência.")

    def consultar_saldo (self):
        return self.__saldo
    
    def consultar_extrato(self):
        return self.__extrato.consultar_extratos()
    
class ContaCorrente(Conta):
    def __init__(self):
        super().__init__()

    def sacar (self, valor: float):
        saque = self.__saldo - valor

        if valor > 0.00 and saque > 0.00:
            self.__saldo = saque
            self.__extrato.add_transacao("saque realizado na conta corrente", valor)

        else:
            print("Saldo insuficiente...")
            
class ContaPoupanca(Conta):
    def __init__(self, saldo: float):
        super().__init__(saldo)

    def sacar (self, valor: float):
        saque = self.__saldo - valor

        if valor > 0.00 and self.__saldo > 100.00:
            if saque > 0.00:
                self.__saldo = saque
                self.__extrato.add_transacao("saque realizado na conta poupança", valor)

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
        transacao = f"Descrição: {descricao} \n Valor: R${valor:.2f}"

        self.__trasacoes.append(transacao)

    def consultar_extratos(self):
        return self.__trasacoes 

class Banco:
    def __init__(self):
        self.__clientes = []

    def add_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def rmv_cliente(self, cliente: Cliente):
        if cliente in self.__clientes:
            self.__clientes.remove(cliente)

        else:
            print("Cliente não encontrada...")