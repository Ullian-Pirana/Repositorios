from listas import *
from class_bib import *
import os

def menu(): #Função de menu

    print("\t \t  ~~~BRIBRIOTECA DO ALEX~~~")
    print("\t \t \t~~BEM VINDO!~~ \n")

    print("""
    \t O que gostaria de fazer?
          1 - Ver livros Disponiveis
          2 - Realizar um emprestimo
          3 - Cadastrar novo livro
          4- Sair
    """)
    
    escolha = int(input("--> ")) #Váriavel para se inserir um valor

    os.system("cls")

    return escolha #Retornara valor armazenado na váriavel escolha

#
def ver_livro():

    print(" \t Estante de livros: \n ")

    verificar = int(input("Como gostaria de verificar os livros? \n 1 - Ver todos \n 2 - Gênero \n 3 - Autores \n \t ---> "))

    os.system("cls")

    if verificar == 1:

        print("\t Todos os Livros: \n ")

        for item, valor in Estante.items():
            print(f"\n {item}: \n")
            posicao = 1

            for bolha in valor:
                print(f"{posicao}º - {bolha}")
                posicao += 1

        print(" ")

        os.system("pause")
        os.system("cls")

    elif verificar == 2:
        
        print("""\t Gêneros disponiveis:
            Distopia
            Drama
            Fantasia
            Romance
            Fábula
            Mistério/Thriller
            Realismo Mágico
            Ficção Científica
            Aventura
            Existencialismo
            Não-Ficção""")
        
        escolha_gen = input("---> ")

        for chave, valor in Estante.items():
            if chave == "genero":
                for item in valor:
                    if item == escolha_gen:
                        print(f"{chave} : {item}")
                    



    elif verificar == 3:
        pass

    else:
        print("Opção invalida...")
        os.system("pause")
        os.system("cls")

def emprestar():

    print("\t \t Fazer emprestimo \n")

    empre = int(input("O que gostaria de fazer? \n 1 - Realizar novo emprestimo \n 2 - mudar o emprestimo de um cliente \n --> "))

    os.system("cls")

    if empre == 1:

        nome = input("Nome do cliente: ")
        livro = input("Livro a ser emprestado: ")
        DDE = input("Data de retirada: ")
        DDD = input("Data da Devolução: ")
        contact = input("Forma de contato com o cliente: ")

        if livro in livros:
            print("Emprestimo Realizado!")

            emprestado = Cliente(nome, livro, DDE, DDD, contact)

            cliente.append(emprestado)
        
    elif empre == 2:

        if cliente.__len__() >= 1:

            count = 1

            print("Usuario que realizaram um emprestimo: \n ")

            for user in cliente:
                print(f"{count}º:\n nome do cliente: {user.getNC()} \n livro emprestado: {user.getLivro()} \n contato: {user.getContato} \n")

                count += 1

            os.system("pause")

            mudar_empre = int(input("Qual a posição do usuario que vc deseja realizar a mudança do livro emprestado? \n --> "))
            mudar_livro = input("Qual o novo livro do cliente? \n ---> ")

            os.system("cls")


            if cliente.__len__() <= mudar_empre:
                if mudar_livro in livros:
                    cliente(mudar_empre - 1).setLivro(mudar_livro)

                    print("Novo cadastro realizado com sucesso! ")

                    os.system("pause")
                    os.system("cls")

                else:
                    print("livro não encontrado...")

                    os.system("pause")
                    os.system("cls")

            else:
                print("Nenhum usario encontrado...")

                os.system("pause")
                os.system("cls")

        else:
            print("nenhum usuario cadastrado...")
            os.system("pause")
            os.system("cls")

    else:
        print("opção invalida...")
        os.system("pause")
        os.system("cls")

def cadastro():
    while True:
        print("---- CADASTRO DE LIVROS ----")
        nome = input("Infome o nome do livro\n -->")
        genero = input("Infome o gênero do seu livro\n -->")
        autor = input("Informe o autor do livro \n -->")

        livro = (nome, genero, autor)
        
        return livro
        
