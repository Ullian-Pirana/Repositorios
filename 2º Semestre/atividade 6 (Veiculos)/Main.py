#Principal
import os
from Defs import *
from Listas import *
from Classes import *

while True:
    os.system("cls")
    escolha = Menu()

    match escolha:
        case 1:
            user = login(cliente)
        case 2:
            cliente.append(cliente())
        case 3:
            veículo.append(cadastrar_veiculo())
        case 4:
            pass
            
        