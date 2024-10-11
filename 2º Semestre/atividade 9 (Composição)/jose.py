class Cadastro:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.end = None

    def setEndereco(self,cep, num, rua, bairro, cidade):
        self.end = Endereco(cep, num, rua, bairro, cidade)

    def getEndereco(self):
        return self.end

    def getRua(self):
        return self.end.getRua()

class Endereco:
    def __init__(self, cep, num, rua, bairro, cidade):
        self.cep = cep
        self.num = num
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade 

    def __str__(self):
        return self.cep

    def getRua(self):
        return self.rua


jose = Cadastro("José","12312312312")
jose.setEndereco("02407320", "10","R.Senai","Tamoio", "Várzea")

print(f"Cep: {jose.getEndereco()}")
print(f"Rua: {jose.getEndereco().getRua()}")
print(f"Rua02: {jose.getRua()}")