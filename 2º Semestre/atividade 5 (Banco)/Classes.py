class Cadastro:

    def __init__(self, nome, senha, email, cpf, rg, cep):

        self.__nome = nome
        self.__senha = senha
        self.__email = email
        self.__cpf = cpf
        self.__rg = rg
        self.__cep = cep

    def __str__(self):
        return self.__nome
    
    #DEF'S para VERIFICAR informações
    
    def verNome(self):
        return self.__nome
    
    def verSenha (self):
        return self.__senha
    
    def verEmail (self):
        return self.__email
    
    def verCpf (self):
        return self.__cpf
    
    def verRg (self):
        return self.__rg
    
    def verCep (self):
        return self.__cep
    
    #DEF'S para Mudar as informações
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setSenha (self, senha):
        self.__senha = senha
    
    def setEmail (self, email):
        self.__email = email
    
    def setCpf (self, cpf):
        self.__cpf = cpf
    
    def setRg (self, rg):
        self.__rg = rg
    
    def setCep (self, cep):
        self.__cep = cep


class Cliente(Cadastro):
    
    def __init__(self, nome, senha, email, cpf, rg, cep, saldo, poupanca):
        super().__init__(nome, senha, email, cpf, rg, cep)
        self.__saldo = saldo
        self.__poupanca = 0.0

    def verSaldo(self):
        return self.__saldo
    
    def setSaldo(self, saldo):
        self.__saldo = saldo

    def verPou(self):
        return self.__poupanca
    
    def setPou(self, poupanca):
        self.__poupanca = poupanca