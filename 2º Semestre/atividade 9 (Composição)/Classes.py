class Usuario:
    def __init__(self, nome, cpf, senha, email, tel, rg):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__email = email
        self.__tel = tel
        self.__rg = rg
        self.__end = None
        self.__conta = None

    def __str__(self):
        return self.__nome

    def getNome (self):
        return self.__nome

    def getCpf (self):
        return self.__cpf

    def getSenha (self):
        return self.__senha

    def getEmail (self):
        return self.__email

    def getTel (self):
        return self.__tel

    def getRg (self):
        return self.__rg

    def getEnd (self):
        return self.__end
    
    def setNome (self, nome):
        self.__nome = nome

    def setCpf (self, cpf):
        self.__cpf = cpf

    def setSenha (self, senha):
        self.__senha = senha

    def setEmail (self, email):
        self.__email = email

    def setTel (self, tel):
        self.__tel = tel

    def setRg (self, rg):
        self.__rg = rg

    def setEnd (self, cidade, bairro, rua, n, cep):
        self.__end = Endereco(cidade, bairro, rua, n, cep)

    def setConta(self, conta):
        self.__conta = conta
    
class Endereco:
    def __init__(self, cidade, bairro, rua, n, cep):
        self.__cidade = cidade
        self.__bairro = bairro
        self.__rua = rua
        self.__n = n
        self.__cep = cep

    def __str__(self):
        return self.__cep

    def getCity (self):
        return self.__cidade

    def getBairro (self):
        return self.__bairro

    def getRua (self):
        return self.__rua

    def getNumero (self):
        return self.__n

    def getCep (self):
        return self.__cep       

class conta:

    def __init__(self, saldo, poupanca):
        self.__saldo = saldo
        self.__pou = poupanca
        self.__contatos = []

    def getSaldo(self):
        return self.__saldo
    
    def getPoupanca(self):
        return self.__pou
    
    def getContatos(self):
        return self.__contatos
    
    def setSaldo(self, saldo):
        self.__saldo = saldo
    
    def setPoupanca(self, pou):
        self.__pou = pou
    
    def setContatos(self, contato):
        self.__contatos.append(contato)




