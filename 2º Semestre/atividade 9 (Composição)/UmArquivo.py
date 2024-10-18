class Conta:
    def __init__(self, tipo: str):
        self.__tipo = tipo
        self.__saldo = 0.0

    def getTipo(self):
        return self.__tipo

    def setSaldo(self, saldo: float):
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo


class Corrente(Conta):
    def __init__(self):
        super().__init__("Conta Corrente")


class Poupança(Conta):
    def __init__(self):
        super().__init__("Conta Poupança")


class Cliente:
    def __init__(self, nome: str):
        self.nome = nome
        self.contas = []  # Lista de contas

    def adicionarConta(self, conta: Conta):
        self.contas.append(conta)

    def listarContas(self):
        for conta in self.contas:
            print(f"Tipo: {conta.getTipo()}, Saldo: {conta.getSaldo()}")


class Banco:
    def __init__(self, nome: str):
        self.nome = nome
        self.clientes = []  # Lista de clientes

    def adicionarCliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def listarClientes(self):
        print(f"Clientes do Banco {self.nome}:")
        for cliente in self.clientes:
            print(cliente.nome)


# Exemplo de uso
banco = Banco("Banco Exemplo")

# Criando clientes
cliente1 = Cliente("João")
cliente2 = Cliente("Maria")

# Adicionando clientes ao banco
banco.adicionarCliente(cliente1)
banco.adicionarCliente(cliente2)

# Criando contas
conta_corrente = Corrente()
conta_corrente.setSaldo(1500.0)

conta_poupanca = Poupança()
conta_poupanca.setSaldo(3000.0)

# Adicionando contas aos clientes
cliente1.adicionarConta(conta_corrente)
cliente2.adicionarConta(conta_poupanca)

# Listando clientes e suas contas
banco.listarClientes()
cliente1.listarContas()
cliente2.listarContas()
