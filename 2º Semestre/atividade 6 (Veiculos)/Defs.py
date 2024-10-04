import os
from Listas import *

def Menu():
    while True:
        print("Seja bem vindo ao aluguel de carros Pipkabum")
        print("1- Alugar um veículo \n 2- Cadastrar um cliente \n 3-Cadastrar carros \n 4-Sair")
        try:
            
            escolha = int(input("--->"))

            os.system("pause")
            os.system("cls")
            
            break
        except Exception as e:
            print("Valor inválido, erro {e}")
            
    return escolha

def Login():
    while True:
        try:

            cliente  = input("\t CPF ")
            senha = input("\t Senha: ")

            os.system("cls")

            break
             
        except Exception as e:

            print(f" \t impossivel realizar acesso, erro encontrado: {e}")

            os.system("pause")
            os.system("cls")

    for userr in cliente:
        if cliente == userr.verCpf() and senha == userr.verSenha():
            print(f"\t Bem Vindo {userr.verUsuario()}")
            return userr
        else:
            print("Nenhum cadastro encontrado!")

            os.system("pause")
            os.system("cls")
    


def cadastrar_veiculo():

    print("\tCasdastro de Veiculos")

    while True:

        try:

            marca = input("Marca do Carro: ")
            modelo = input("Modelo do Carro: ")
            ano = int(input("Ano do Carro: "))
            placa = input("Placa do Carro: ")

            os.system("cls")

            break

        except Exception as e:
            print(f" \tNão foi possivel realizar o cadastro, erro encontrado: {e}")

        cadastrado = (marca,modelo, ano, placa)

        return cadastrado
    

def cadastrar_user():
    pass
