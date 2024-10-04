import os      
from Listas import *
from Classes import *

# Menu de escolhas
def Menu():
    while True:
        print("Seja bem-vindo ao aluguel de carros Pipkabum")
        print("1- Login Cliente \n2- Cadastrar um cliente \n3- Cadastrar carros \n4- Alugar Veículo \n5- Sair")
        try:
            escolha = int(input("---> "))  # Entrada numérica
            os.system("pause")  # Pausa a execução
            os.system("cls")    # Limpa a tela
            return escolha  # Retorna a escolha
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")


# Função para cadastrar um veículo
def cadastrar_carro():
    print("\tCadastro de Carros")
    while True:
        try:
            marca = input("Marca do Carro: ")
            modelo = input("Modelo do Carro: ")
            ano = int(input("Ano do Carro: "))
            placa = input("Placa do Carro: ")
            diaria = None
            
            os.system("cls")  # Limpa a tela
            if placa not in carros:
                carros.append(placa)
                print("\n\tCadastro Realizado!")
                cadastrado = Veiculo(marca, modelo, ano, placa, diaria)
                os.system("cls")
                print("Veículo cadastrado!")
                return cadastrado
            else:
                print("Veículo já cadastrado...")
                os.system("pause")
                os.system("cls")
        except ValueError:
            print("\tEntrada inválida. Tente novamente.")

def cadastrar_moto():
    print("\tCadastro de Motos")
    while True:
        try:
            marca = input("Marca da Moto: ")
            modelo = input("Modelo da Moto: ")
            ano = int (input("Ano da Moto: "))
            placa = input("Placa da Moto: ")
            diaria = None

            os.system("cls")  # Limpa a tela
            if placa not in motos:
                motos.append(placa)
                print("\n\tCadastro Realizado!")
                cadastrado = Veiculo(marca, modelo, ano, placa, diaria)  # Cria um objeto Veiculo
                os.system("cls")
                print("Veículo cadastrado!")
                return cadastrado
            else:
                print("Veículo já cadastrado...")
                os.system("pause")
                os.system("cls")
        except ValueError:
            print("\tEntrada inválida. Tente novamente.")

# Função para cadastro de um usuário 
def cadastrar_user():
    while True:
        try:
            nome = input("Nome Completo: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            email = input("E-Mail: ")
            cep = input("CEP: ")
            senha = input("Senha: ")
            os.system("cls")
            
            if cpf in cpfs:  # Verifica se o CPF já está na lista
                print("CPF já cadastrado.")
                continue  # Volta ao início do loop se o CPF já estiver cadastrado
            
            cpfs.append(cpf)  # Adiciona o CPF
            cadastrado = Cliente(nome, senha, email, cpf, rg, cep)  # Cria um objeto Cliente
            print("\tCadastro realizado com sucesso!")
            return cadastrado  # Retorna o novo cliente cadastrado
        
        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")
        
        break

            

def alugar_veiculos():
    while True:
        print("\tAlugar Veículos")
        print("Qual veículo deseja alugar?\n")
        print("1- Carro \n2- Moto \n3- Sair")
        
        try:
            escolha = int(input("Qual opção deseja?\n--> "))
            match escolha:
                case 1:
                    print("--- CARRO ---\n")
                    print("Carros disponíveis:")
                    for carro in carros:
                        print(carro)  # Exibe os carros disponíveis

                    sel_placa = input("Escreva a placa do veículo que deseja:\n---> ")
                    for carro in carros:
                        if sel_placa == carro.getPlaca():
                            print(f"Carro alugado\t --Identificação: {carro}")
                            return carro

                case 2:
                    print("--- MOTO ---\n")
                    print("Motos disponíveis:")
                    for moto in motos:
                        print(moto)  # Exibe as motos disponíveis

                    sel_placa = input("Escreva a placa do veículo que deseja:\n---> ")
                    for moto in motos:
                        if sel_placa == moto.getPlaca():
                            print(f"Moto alugada\t --Identificação: {moto}")
                            return moto

                case 3:
                    print("Saindo do aluguel de veículos.")
                    break

                case _:
                    print("Opção inválida. Tente novamente.")
        
        except Exception as e:
            print(f"\tImpossível realizar acesso, erro encontrado: {e}")
            os.system("pause")
            os.system("cls")                   

def login():
    while True:
        try:
            print("--- Login ---")
            acesso = input("\tCPF: ")
            senha = input("\tSenha: ")
            os.system("cls")
            for userr in cliente:  # Supondo que a lista de clientes seja chamada 'clientes'
                if acesso == userr.getCpf() and senha == userr.getSenha():
                    print(f"\tBem-vindo {userr.getNome()}")
                    return userr
            
            print("Nenhum cadastro encontrado!")
            os.system("pause")
            os.system("cls")

        except Exception as e:
            print(f"\tImpossível realizar acesso, erro encontrado: {e}")
            os.system("pause")
            os.system("cls")
