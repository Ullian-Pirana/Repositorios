from abc import *

#Classe pai, classe abstrata onde se herda os atributos e metodos 
class Conta(ABC):
    @abstractmethod #Decorator: Associar uma nova função a tudo que se tem na classe
    def __init__(self): #Construtor
        self.__saldo = 0.00        # O atributo saldo incia com o valor 0
        self.__extrato = Extrato()  # É criado um objeto para as transações feitas

    #Método 
    def depositar(self, valor: float):
        if valor > 0:
            depositado = self.__saldo + valor   #Acrescenta um valor ao saldo
            self.__saldo = depositado #Novo valor atribuito ao saldo
            self.__extrato.add_transacao("Depósito", valor) #Mostra o depósito feito 
    
    #Método 
    def sacar(self, valor : float):
        self.__saldo -= valor   #Retira um valor do saldo 

    #Método
    def transferir(self, conta_destino, valor: float):
        if valor > 0 and valor <= self.__saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
            self.__extrato.add_transacao(f"PIX para {conta_destino.getTipo()} no valor de R${valor:.2f}")
            conta_destino.consultar_extrato().add_transacao(f"PIX recebido de {self.getTipo()} no valor de R${valor:.2f}")
            print(f"Transferência PIX de R${valor:.2f} realizada com sucesso para {conta_destino.getTipo()}.")
        else:
            print("Valor inválido para transferência PIX.")

    #Método
    def consultar_saldo (self):
        return self.__saldo
    
    #Método
    def consultar_extrato(self):
        return self.__extrato.consultar_extratos()
    
class ContaCorrente(Conta):
    def __init__(self):
        super().__init__()
        self.__tipo = "Conta Corrente"

    def __str__(self):
        return self.__tipo
    
    def getTipo(self):
        return self.__tipo

    def sacar(self, valor: float):
        saque = self.__saldo - valor

        if valor > 0.00 and saque > 0.00:
            self.__saldo = saque
            self.__extrato.add_transacao("saque realizado na conta corrente, no valor de R$:", valor)

        else:
            print("Saldo insuficiente...")
            
class ContaPoupanca(Conta):
    def __init__(self):
        super().__init__()
        self.__tipo = "Conta Poupança"

    def __str__(self):
        return self.__tipo
    
    def getTipo(self):
        return self.__tipo

    def sacar (self, valor: float):
        saque = self.__saldo - valor

        if valor > 0.00 and self.__saldo > 100.00:
            if saque > 0.00:
                self.__saldo = saque
                self.__extrato.add_transacao("saque realizado na conta poupança , no valor de R$:", valor)

            else:
                print("Saldo insuficiente...")
        else:
            print("Requisitos de saque não atendidos...")

class Cliente:
    def __init__(self,nome: str,cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []

    def __str__(self):
        return self.__nome

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf

    def addConta(self, conta: Conta):
        self.__contas.append(conta)

    def rmvConta(self, conta: Conta):
        if conta in self.__contas:
            self.__contas.remove(conta)
        else:
            print("Conta não encontrada...")

    def getContas(self):
        return self.__contas

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

    def __str__(self):
        return "Ull Bank"

    def add_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def rmv_cliente(self, cliente: Cliente):
        if cliente in self.__clientes:
            self.__clientes.remove(cliente)

        else:
            print("Cliente não encontrada...")

    def getClientes(self):
        return self.__clientes