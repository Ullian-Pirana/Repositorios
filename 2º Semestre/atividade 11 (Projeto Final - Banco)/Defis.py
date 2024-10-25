import os
from classis import *

def menu():
    while True:
        print("\t ~~~~Ull Bank~~~ \n")
        print("O que gostaria de fazer?\n \t 1 - Login\n \t 2 - Cadastrar-se \n \t 3 - Excluir Conta ")

        try:
            escolha =  int(input("--> "))

            os.system("cls")
            break

        except Exception as e:                      
            print(f"Impossivel concluir operação \n erro encontrado: {e}")

            os.system("pause")
            os.system("cls")
    
    return escolha

def cadastro(banco):
    while True:
        print("\t Cadastro \n")
        print("Para realizarmos seu cadastro vamos precisar\n das seguintes informações: ")

        try:
            nome = input("Nome: ")
            cpf = input("Cpf: ")

            cliente = Cliente(nome, cpf)
            banco.add_cliente(cliente)

            print("cadastro realizado com sucesso!")
            os.system("cls")
            
            break

        except Exception as e:                      
            print(f"Impossivel concluir operação \n erro encontrado: {e}")

            os.system("pause")
            os.system("cls")  

def excluir(banco):
    while True:
        print("\t Excluir Conta \n")

        if len(banco.getClientes()) > 0:
            print("Para realizar a exclusão da sua conta precisamos que nos de \n as seguintes informações: ")

            try:
                nome = input("Seu Nome: ")
                cpf = input("Seu Cpf: ")

                for cliente in banco.getClientes():
                    if nome == cliente.getNome() and cpf == cliente.getCpf():
                        banco.rmv_cliente(cliente)

                        print("Exclusão realizada com êxito!")

                        os.system("pause")
                        os.system("cls")
                        break 

                    else:
                        print("Nenhum cliente encontrado com essas informações...")
                        os.system("pause")
                        os.system("cls")

            except Exception as e:                      
                print(f"Impossivel concluir operação \n erro encontrado: {e}")

                os.system("pause")
                os.system("cls")

        else:
            print("Nenhum Cadastro encontrado...")
            os.system("pause")
            os.system("cls")

            break

def login(banco):
    while True:
        print("\t _-_-Login-_-_ \n")
        print("Por favor, insira suas informações de login:")

        try:
            nome = input("Nome: ")
            cpf = input("Cpf: ")

            cliente_encontrado = None

            for cliente in banco.getClientes():
                if nome == cliente.getNome() and cpf == cliente.getCpf():
                    cliente_encontrado = cliente

                    print(f"Login bem-sucedido!\n Bem-vindo, {cliente_encontrado.getNome()}!")
                    os.system("pause")
                    os.system("cls")

                    return cliente_encontrado

                else:
                    print("Nome ou CPF inválidos. Tente novamente.")
                    os.system("pause")
                    os.system("cls")
            
            break

        except Exception as e:
            print(f"Impossível concluir a operação \n erro encontrado: {e}")
            
            os.system("pause")
            os.system("cls")

def tela_banco(user):
    while True:
        print("\t Ull Bank \n")
        print(f"Usuario: {user.getNome()} \n")
        print("Qual Conta gostaria de Utilizar?\n 1- Corrente\n 2- Poupança\n 3- Sair")

        try:
            conta = int(input("--> "))

            break
            
        except Exception as e:
            print(f"Impossível concluir a operação \n erro encontrado: {e}")
            
            os.system("pause")
            os.system("cls")
            
    return conta

def conta_corrente(user):
    conta = "Conta Corrente"

    while True:
        print("Conta Corrente")

        if conta not in user.getContas():
            while True:
                print("Conta Corrente não foi Aberta ainda, gostaria de Abrir uma? \n 1- Sim \n 2- Não")

                try:
                    abrir = int(input("--> "))

                    os.system("pause")
                    os.system("cls")
                    break

                except Exception as e:                      
                    print(f"Impossivel concluir operação \n erro encontrado: {e}")

                    os.system("pause")
                    os.system("cls")

            while True:
                match abrir:
                    case 1:
                        contaC = ContaCorrente() 

                        print("Conta Corrente Aberta com sucesso!")

                        os.system("pause")
                        os.system("cls")
                        break
                    
                    case 2:
                        print("Saindo...")
                        os.system("pause")
                        os.system("cls")
                        break

                    case _:
                        print("Opção Invalida...")
                        os.system("pause")
                        os.system("cls")

        else:
            for contas in user.getContas():
                if conta == contas.getTipo():
                    conta_usar = contas

            print(f"Saldo: {conta_usar.consultar_saldo()} \n")
            print("O que gostaria de fazer?\n 1- Sacar \n 2- Depositar \n 3- Pix \n 4- sair")

            while True:
                try:
                    usar_conta = int(input("--> "))

                    break

                except Exception as e:                      
                    print(f"Impossivel concluir operação \n erro encontrado: {e}")

                    os.system("pause")
                    os.system("cls")
            
            match usar_conta:
                case 1:
                    while True:
                        try:
                            sacar = float(input("Valor do saque: "))
                            break

                        except Exception as e:                      
                            print(f"Impossivel concluir operação \n erro encontrado: {e}")

                            os.system("pause")
                            os.system("cls")
                            
                    conta_usar.sacar(sacar)


def conta_poupanca(user):
    conta = "Conta Poupança"

    while True:
        pass






