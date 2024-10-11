class Controle:
    def __init__(self, tipo):
        self.tipo = tipo

class Console:
    def __init__(self, nome):
        self.nome = nome
        self.controles = []

    def adicionar_controle(self, controle):
        self.controles.append(controle)

class Gamer:
    def __init__(self, usuario):
        self.usuario = usuario
        self.consoles = []

    def adicionar_console(self, console):
        self.consoles.append(console)

gamer1 = Gamer("Player1")
console1 = Console("PlayStation 5")
controle1 = Controle("DualSense")

console1.adicionar_controle(controle1)
gamer1.adicionar_console(console1)

print(f"Gamer: {gamer1.usuario}")
for console in gamer1.consoles:
    print(f"Console: {console.nome}")
    for controle in console.controles:
        print(f"Controle: {controle.tipo}")