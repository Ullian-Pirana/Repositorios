#Criação das funções
import os
from Listas import *
from Classes import *

#Menu de escolhas, permitirá realizar escolhas.
def Menu():
    while True:
        print("Seja bem vindo ao aluguel de carros Pipkabum")
        print("1- Alugar um veículo \n 2- Cadastrar um cliente \n 3-Cadastrar carros \n 4-Sair")
        try:
            
            escolha = int(input("--->")) #permite criar uma variável, onde só poderá informar somente de maneira númerica

            os.system("pause")  # pausará o código
            os.system("cls")    # limpará o código, permitindo que a pessoa possa realizar uma outra ação ou a mesma

            break
            #Ao informar uma resposta que não seja válida, aparecerá uma resposta informando "Valor inválido".
        except Exception as e:
            print("Valor inválido, erro {e}")
    #Ao fazer uma ação, retornará para a posição do comando específico     
    return escolha


#Funcao para cadastrar um  veiculo
def cadastrar_veiculo():

    print("\tCasdastro de Veiculos")

    while True:
        #envolver o código que pode gerar erros.
        try:
            #variáveis = campos de preenchimento, permitindo colocar informações
            marca = input("Marca do Carro: ")
            modelo = input("Modelo do Carro: ")
            ano = int(input("Ano do Carro: "))
            placa = input("Placa do Carro: ")
            # limpará o código, permitindo que a pessoa possa realizar uma outra ação ou a mesma
            os.system("cls")

            break
        #Ao informar uma resposta que não seja válida, aparecerá uma resposta informando "Valor inválido".
        except Exception as e:
            print(f" \tNão foi possivel realizar o cadastro, erro encontrado: {e}")
            
    if placa not in placas:
        placas.append(placa)   # Se a placa não estiver na lista de placas, adicione-a.
 
        print("")
        print("\tCadastro Realizado!")
        cadastrado = Veiculo(marca,modelo, ano, placa)    # Cria um objeto Veiculo com os dados fornecidos.
        
        
        os.system("cls")
        
        print("Veículo cadastrado !")

        return cadastrado   #Ao fazer uma ação, retornará para a posição do comando específico  
        
    else:
        print("Veículo já Cadastrado...")

        os.system("pause")
        os.system("cls")  # limpará o código, permitindo que a pessoa possa realizar uma outra ação ou a mesma

    

#Funcao para cadastro de um usuario 
def cadastrar_user():
    #Entra em um loop
    while True:
        try:
            nome = input("Nome Completo: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            email = input("E-Mail: ")
            cep = input("CEP: ")
            senha = input("Senha: ")

            os.system("cls")
            break 
    
        except Exception as e:
            print (f"Valor errado. (Type error {e})")
            
            if cpf not in cpfs: # vai verificar se a variavel cpf esta na lista
                cpfs.append(cpf) #Se a condicao for verdadeira o cpf sera adicionado a lista de cpfs
                                 # A condicao vai ser 
            cadastrado = Cliente(nome, senha, email, cpf, rg, cep,)
            
        return cadastrado


def alugar_veiculos():

    while True:
        
        print("\tAlugar Veiculos")
        print("Qual veiculo deseja alugar?\n")
        print("1- Carro \n 2- Moto \n 3-Sair")
        
        try:

            escolha= int(input("Qual opção deseja?\n-->"))
            
            match escolha:

                case 1:
                    print("--- CARRO ---")
                        
                    
                    
                
                case 2:
                    print("--- MOTO ---")
                        
                case 3:
                    os.system("cls")
                    break
                    
                        
                
            

            
            

            os.system("cls")

            break

        except Exception as e:
            print(f" \tNão foi possivel realizar o cadastro, erro encontrado: {e}")

def login():
    while True:
        try:
            acesso = input("\t CPF: ")
            senha = input("\t Senha: ")
            os.system("cls")
            break
        except Exception as e:
            print(f" \t impossivel realizar acesso, erro encontrado: {e}")

            os.system("pause")
            os.system("cls")

    for userr in cliente:
        if acesso == userr.verCpf() and senha == userr.verSenha():
                
                print(f"\t Bem Vindo {userr.verUsuario()}")
                
                return userr
        else:
            print("Nenhum cadastro encontrado!")

            os.system("pause")
            os.system("cls")
        