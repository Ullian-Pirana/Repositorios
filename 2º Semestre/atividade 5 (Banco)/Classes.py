class Cadastro:

    def __init__(self, usuario, senha, saldo, email, cpf, rg, idade, cep):

        self.__usuario = usuario
        self.__senha = senha
        self.__saldo = saldo
        self.__email = email
        self.__cpf = cpf
        self.__rg = rg
        self.__idade = idade
        self.__cep = cep

    def __str__(self):
        return self.__usuario
    
    #DEF'S para VERIFICAR informações
    
    def verSaldo(self):
        return self.__saldo
    
    def verUsuario(self):
        return self.__usuario
    
    def verSenha (self):
        return self.__senha
    
    def verEmail (self):
        return self.__email
    
    def verCpf (self):
        return self.__cpf
    
    def verRg (self):
        return self.__rg
    
    def verIdade (self):
        return self.__idade
    
    def verCep (self):
        return self.__cep
    
    #DEF'S para Mudar as informações

    def setSaldo(self, saldo):
        self.__saldo = saldo
    
    def setUsuario(self, usuario):
        self.__usuario = usuario
    
    def setSenha (self, senha):
        self.__senha = senha
    
    def setEmail (self, email):
        self.__email = email
    
    def setCpf (self, cpf):
        self.__cpf = cpf
    
    def setRg (self, rg):
        self.__rg = rg
    
    def setIdade (self, idade):
        self.__idade = idade
    
    def setCep (self, cep):
        self.__cep = cep

