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







