class Motor:

    def __init__(self, potencia : float, marca: str):
        self.__potencia = potencia
        self.__marca = marca

    def getPotencia(self):
        return self.__potencia
    
    def setPotencia(self, pot: float):
        self.__potencia = pot
        
    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca: str):
        self.__marca = marca

class Rodas:

    def __init__(self, tamanho : int, marca: str):
        self.__tamanho = tamanho
        self.__marca = marca

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, tamanho: float):
        self.__tamanho = tamanho
        
    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca: str):
        self.__marca = marca

class Carro:

    def __init__(self):
        self.__motor = None
        self.__rodas = None

    def getMotor(self):
        return self.__motor
    
    def setMotor(self, motor):
        self.__motor = motor
        
    def getRodas(self):
        return self.__rodas
    
    def setRodas(self, rodas):
        self.__rodas = rodas

