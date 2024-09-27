import os

def Menu():
    while True:
        print("Seja bem vindo ao aluguel de carros Pipkabum")
        print("1- Alugar um veículo \n2- Cadastrar um cliente \n3-Cadastrar carros \n4-Sair")
        try:
            
            escolha = int(input("--->"))
            
            break
        except Exception as e:
            print("Valor inválido, erro {e}")
    
    return escolha

    