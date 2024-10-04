#Principal

import os                
from Defs import *      
from Listas import *   
from Classes import *  

while True: # A execução funcionará se a condição for verdadeira
    os.system("cls")
    escolha = Menu()

    match escolha:
        case 1:
            user = login()# autenticar um usuário
        case 2:
            cliente.append(cadastrar_user()) # Adiciona um novo cliente à lista cliente
        case 3:
            veículo.append(cadastrar_carro())
           
            veículo.append(cadastrar_moto()) # Adiciona um novo veículo à lista veículo
        case 4:
            alugar_veiculos()
            
        