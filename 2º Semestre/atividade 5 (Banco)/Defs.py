import os
from Listas import *
from Classes import *

def menu():

    while True:
        print("--- ULL Bank ---")
        print("Seja bem vindo ao ULL Bank, um banco especializado em resolver os seus problemas: \nO que deseja fazer? \n 1- Fazer Login \n 2- Fazer cadastro \n 3 - sair")
        
        while True:
            try:
                escolha = int(input("Qual opção deseja ? \n ---> "))

                os.system("cls")

                break

            except Exception as e:

                print(f"Impossivel concluir operação \n erro encontrado: {e}")

                os.system("pause")
                os.system("cls")
            
            return escolha

def cadastro():

    print("\t \t Cadastro~~~\n")

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
            print(f" \t impossivel realizar operação, erro encontrado: {e}")

        if cpf not in cpfs:
            cpfs.append(cpf)

            print("\t Cadastro quase finalizado.... \n \t para finalizar o cadastro nos informe o saldo inicial de sua conta...\n")
            print("OBS: O Saldo é transferido automaticamente de uma conta ativa sua cadastrado em outro banco, em caso de ser sua primeira conta o valor do saldo depositado ira ser cobrado como emprestimo e sera quitado utilizando valores depositados em sua conta no futuro!")
            print("Todos os processos são legalizados de acordo com a lei Nº9314.213.4927, em caso de tentiva de golpe nossa equipe juridica será acionada!! \n")


            saldo = float(input("Insira o Valor do saldo que deseja tranferir para a conta\n ---> "))

            cadastrado = Cliente(nome, senha, email, cpf, rg, cep, saldo)

            os.system("cls")

            print("\t --->Cadastro Realizado com Sucesso!<---")

            os.system("pause")
            os.system("cls")

            return cadastrado
        
        else:
            print("Cpf Já Cadastrado...")

            os.system("pause")
            os.system("cls")

def login():

    print("\t \t ~~~ULL Bank~~~ \n")

    print("Bem vindo ao Ull bank, para realizar o acesso a sua conta por favor nos informe suas informações de acesso: \n")

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

    for user in cadastros:
        if user.verCpf() == acesso and user.verSenha() == senha:
                
                print(f"\t Bem Vindo {user.verUsuario()}")
                
                return user
        
        else:
            print("Nenhum cadastro encontrado!")

            os.system("pause")
            os.system("cls")

def tela_banco(usuario):

    print("\t \t ~~~~ULL Bank~~~ \n ")

    print(f"\t Usuario: {usuario.verUsuario()}")
    print(f"Saldo: {usuario.verSaldo()}")

    while True:

        try:
            usar = int(input("Qual conta gostaria de utilizar? \n 1- Conta Corrente \n 2- Conta Poupança \n \t ---> "))

            os.system("cls")

            break

        except Exception as e:
            print(f" \t impossivel realizar operação, erro encontrado: {e}")

        return usar
    
def corrente(usuario):


    print("\t \t ~~~ULL Bank~~~")
    print("\t Conta corrente \n")

    print(f"\t Usuario: {usuario.verUsuario()}")
    print(f"\t Saldo: {usuario.verSaldo()}")

    while True:

        try:
            dindin = int(input("O que gostaria de fazer? \n 1- Depositar \n 2- Realizar Pagamento \n 3- Sair \n ---> "))

            os.system("cls")

            break

        except Exception as e:
            print(f" \t impossivel realizar operação, erro encontrado: {e}")    

            os.system("pause")
            os.system("cls")

    return dindin

def deposito(usuario):

    print("\t \t Deposito \n")
    print(f"\t Usuario: {usuario.verUsuario()}")
    print(f"\t Saldo: {usuario.verSaldo()} \n")

    while True:
        try:
            deposito = float(input("valor do Deposito: "))

            break

        except Exception as e:
            print(f" \t impossivel realizar operação, erro encontrado: {e}")

    sald0 = usuario.verSaldo() + deposito

    usuario.setSaldo(sald0)

    print("Transação Realizada com sucesso!")

    os.system("pause")
    os.system("cls")

def pix(usuario):
    print("\t \t ~~Sacar \n")

    print(f"\t Usuario: {usuario.verUsuario()}")
    print(f"\t Saldo: {usuario.verSaldo()}")

    saldo = usuario.verSaldo()

    if saldo <= 1:
        print("Nenhum Saldo disponivel...")

        os.system("pause")
        os.system("cls")

    else:

        while True:
            try:
                recebe = input("Insira o CPF do Destinatario: ")
                saque = float(input("Valor do pagamento: "))

                break

            except Exception as e:
                print(f" \t impossivel realizar operação, erro encontrado: {e}")

        saldoo = saldo - saque

        if saldoo > 0:
            print(f"Pagamento realizado com Sucesso para {recebe}!")

            usuario.setSaldo(saldoo)

            os.system("pause")
            os.system("cls")

        else:
            print("Impossivel Realizar transação, você não possui toda essa grana :(")

            os.system("pause")
            os.system("cls")









