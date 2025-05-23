from abc import *

#Classe pai, classe abstrata onde se herda os atributos e metodos 
class Conta(ABC):
    @abstractmethod #Decorator: Associar uma nova função a tudo que se tem na classe
    def __init__(self): #Construtor
        self.__saldo = 0.00        # O atributo saldo incia com o valor 0
        self.__extrato = Extrato()  # É criado um objeto para as transações feitas

    #Método que deposita um valor a conta
    def depositar(self, valor: float):
        if valor > 0:
            depositado = self.__saldo + valor   #Acrescenta um valor ao saldo
            self.__saldo = depositado #Novo valor atribuito ao saldo
            self.__extrato.add_transacao("Depósito", valor) #Mostra o depósito feito 
    
     #Sacar é um método polimorfico que apresenta diferente comportamentos nas outras classes.
    def sacar(self, valor : float):
        self.__saldo -= valor   #Retira um valor do saldo 

    #Método de transferência
    def transferir(self, conta_destino, valor: float):
        if valor > 0 and valor <= self.__saldo:  #Verifica se  o valor é maior e se o saldo é menor ou igual para validar a transferência
            self.sacar(valor) # Faz a transferência
            conta_destino.depositar(valor) # Deposita o valor transferido na conta desejada
            #Vai adicionar no extrato a transferência de ambas contas 
            self.__extrato.add_transacao(f"PIX para {conta_destino.getTipo()} no valor de R${valor:.2f}") #
            conta_destino.consultar_extrato().add_transacao(f"PIX recebido de {self.getTipo()} no valor de R${valor:.2f}")
            print(f"Transferência PIX de R${valor:.2f} realizada com sucesso para {conta_destino.getTipo()}.")
        else:
            print("Valor inválido para transferência PIX.")

    #Método que retorna o saldo da conta
    def consultar_saldo (self):
        return self.__saldo  
    
    #Método que retorna o extrato das contas 
    def consultar_extrato(self):
        return self.__extrato.consultar_extratos()  

# Herda de conta
class ContaCorrente(Conta):
    def __init__(self):
        super().__init__()
        self.__tipo = "Conta Corrente"

    #Retorna o valor "Conta Corrente"
    def __str__(self):
        return self.__tipo
    
    #Imprime o print "Conta Corrente"
    def getTipo(self):
        return self.__tipo

    #Saca um valor do saldo
    def sacar(self, valor: float):
        saque = self.__saldo - valor

        #Sacar um valor maior que zero
        if valor > 0.00 and saque > 0.00:
            self.__saldo = saque
            self.__extrato.add_transacao("saque realizado na conta corrente, no valor de R$:", valor)

        else:
            print("Saldo insuficiente...")


#Classe que herda da classe pai Conta     
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

        #Saque que só pode ser realizado a se o saldo for igual ou maior que 100
        if valor > 0.00 and self.__saldo > 100.00:
            if saque > 0.00:
                self.__saldo = saque
                self.__extrato.add_transacao("saque realizado na conta poupança , no valor de R$:", valor)

            else:
                print("Saldo insuficiente...")
        else:
            print("Requisitos de saque não atendidos...")


#classe cliente que está associado a classe Conta, no entanto não estão relacionados
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
#Define a classe Extrato que está se relacionando a classe Conta
class Extrato:
    def __init__(self):
        self.__trasacoes = []

    def add_transacao(self,descricao: str,valor: float):
        transacao = f"Descrição: {descricao} \n Valor: R${valor:.2f}"

        self.__trasacoes.append(transacao)

    def consultar_extratos(self):
        return self.__trasacoes 
#Classe banco que está associado a classe Cliente
class Banco:
    def __init__(self):
        self.__clientes = []

    def __str__(self):
        return "Ull Bank"
    #Adicionar os clientes
    def add_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)
    #remover clientes
    def rmv_cliente(self, cliente: Cliente):
        if cliente in self.__clientes:
            self.__clientes.remove(cliente)

        else:
            print("Cliente não encontrada...")

    def getClientes(self):
        return self.__clientes