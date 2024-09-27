#Crição de classes

class Veiculo:

    def __init__(self, placa, marca, modelo, ano, diaria):

        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__diaria = diaria

    def getPlaca(self):
        return self.__placa  
    
    def getMarca(self):
        return self.__marca  

    def getModel(self):
        return self.__modelo  

    def getAno(self):
        return self.__ano
    
    def getDiaria(self):
        return self.__diaria

    def setPlaca(self, placa):
        self.__placa = placa

    def setDiaria(self, diaria):
        self.__diaria = diaria

    def ligar(self):
        print("DARAMRAMRAMRAMRAMRMARMAMRAM")
    
    def andar(self):
        print("VRUUUUUUUUUUMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    
    def desligar(self):
        print("PLOP")

        

class Carro(Veiculo):
    def cantar_pneu(self):
        print("cantando pneu")

class moto(Veiculo):
    def dar_grau(self):
        print("randandandan")
        
class Usuario:

    def __init__(self, nome, rg, cpf, cep, email, telefone):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__cep = cep
        self.__email = email
        self.__telefone = telefone
        