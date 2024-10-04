#Crição de classes

class Veiculo: #Classe veículo 

    def __init__(self, placa, marca, modelo, ano, diaria):

        self.__placa = placa  #(__) os dados não podem ser acessados diretamente fora da classe
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__diaria = diaria

    def getPlaca(self):      #Retornar um valor
        return self.__placa  
    
    def getMarca(self):
        return self.__marca  

    def getModel(self):
        return self.__modelo  

    def getAno(self):
        return self.__ano
    
    def getDiaria(self):
        return self.__diaria

    def setPlaca(self, placa):  #Modificar os valores
        self.__placa = placa

    def setDiaria(self, diaria): 
        self.__diaria = diaria

    #Ações do veículo
    def ligar(self):
        print("DARAMRAMRAMRAMRAMRMARMAMRAM")
    
    def andar(self):
        print("VRUUUUUUUUUUMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    
    def desligar(self):
        print("PLOP")

#Classe que herda da classe pai "Veiculo"
class Carro(Veiculo):   
    def __init__(self, placa, marca, modelo, ano, diaria):
        super().__init__(placa, marca, modelo, ano, diaria)

    def cantar_pneu(self):  #Ação do carro
        print("cantando pneu")

#Classe que herda da classe pai "Veiculo"
class moto(Veiculo): 
    def __init__(self, placa, marca, modelo, ano, diaria):
        super().__init__(placa, marca, modelo, ano, diaria)

    def dar_grau(self):  #Ação da moto
        print("randandandan")
        
#Herda da classe "Veiculo"
class Usuario(Veiculo): 

    #Informações de usuário
    def __init__(self, nome, rg, cpf, cep, email, telefone):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__cep = cep
        self.__email = email
        self.__telefone = telefone


    def getNome(self):         #Retornar um valor
        return self.__nome
        
    def getRg(self):
        return self.__rg
    
    def getCpf(self):
        return self.__cpf
    
    def getCep(self):
        return self.__cep
    
    def getEmail(self):
        return self.__email
    
    def getTel(self):
        return self.__telefone
    
    def setCep(self, cep):  #Modifica os valores
        self.__cep = cep
    
    def setEmail(self, email):
        self.__email = email
    
    def setTel(self, telefone):
        self.__telefone = telefone

#Herda da classe "usuario"
class Cliente(Usuario): 
    def __init__(self, nome, rg, cpf, cep, email, telefone):
        super().__init__(self, nome, rg, cpf, cep, email, telefone) 
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__cep = cep
        self.__email = email
        self.__telefone = telefone

            
    def getNome(self):       #Retornar um valor
        return self.__nome
        
    def getRg(self):
        return self.__rg
    
    def getCpf(self):
        return self.__cpf
    
    def getCep(self):
        return self.__cep
    
    def getEmail(self):
        return self.__email
    
    def getTel(self):
        return self.__telefone
        
    def setNome(self, nome):  #Modifica os valores
        self.__nome = nome

    def setRg(self, rg):
        self.__rg = rg
        
    def setCpf(self, cpf):
        self.__cpf = cpf
    
    def setCep(self, cep):
        self.__cep = cep
    
    def setEmail(self, email):
        self.__email = email
    
    def setTel(self, telefone):
        self.__telefone = telefone

        
        

