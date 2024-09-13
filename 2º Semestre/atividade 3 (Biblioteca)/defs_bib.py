from listas import *
from class_bib import *
import os

def menu(): #Função de menu
    print("\t \t  ~~~BIBLIOTECA MIO NOKAZA~~~")
    print("\t \t \t~~BEM VINDO!~~ \n")

    print("""
    \t  O que gostaria de fazer?
        1 - Ver livros Disponiveis
        2 - Realizar um emprestimo
        3 - Cadastrar novo livro
        4 - Sair
        """)
    
    escolha = int(input("--> ")) #Váriavel para se inserir um valor

    os.system("cls")

    return escolha #Retornara valor armazenado na váriavel escolha

#Função de pesquisa de livros
def ver_livro():

    print(" \t Estante de livros: \n ")
    #Váriavel para inserir o número da estante escolhida 
    verificar = int(input("Como gostaria de verificar os livros? \n 1 - Ver todos \n 2 - Gênero \n 3 - Autores \n \t ---> "))

    os.system("cls")
    #Se verficar for igual a 1, vai listar todos os livros 
    if verificar == 1:

        print("\t Todos os Livros: \n ")
        
        for item, valor in Estante.items():  # Item e valor são variaveis para armazenar os valores no dicionario estante
            print(f"\n {item}: \n") #imprimir o valor inserido na variavel item
            posicao = 1 #Numerar os itens na lista 

            for bolha in valor: #Bolha é a variavel para iterar em valor
                print(f"{posicao}º - {bolha}") #Imprime a poisção e o item
                posicao += 1 #Posição vai ser incrementada em 1

        print(" ")

        os.system("pause")
        os.system("cls")
    #Se verificar for igual a 2, vai listar todos gêneros disponíveis
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
        #Váriavel para escolher um genero em especifico
        escolha_gen = input("---> ")

        for chave, valor in Estante.items(): #Chave e valor para armazenar no dicionário estante
            if chave == "genero": #Valor de chave vai ser igual a genero
                for item in valor: 
                    if item == escolha_gen: #Item vai ser o genero inserido na variavel escolha_gen
                        print(f"{chave} : {item}")# Se a condição for verdadeira vai imprimir valores de chave e item
    
        os.system("pause")
        os.system("cls")

    #Se não ser nenhuma destas opções será inválido
    else:
        print("Opção invalida...")
        os.system("pause")
        os.system("cls")

def emprestar(): #Função com o objetivo de realizar o empréstimo

    print("\t \t Fazer emprestimo \n")

 #Variavel onde o cliente escolhe o que gostaria de realizar /// Opção 1: "Realizar novo emprestimo" - "Mudar o emprestimo de um cliente"
    empre = int(input("O que gostaria de fazer? \n 1 - Realizar novo emprestimo \n 2 - Mudar o emprestimo de um cliente \n --> "))

    os.system("cls")
    #Se escolha for igual a 1 vai fazer um novo emprestimo
    if empre == 1:
        
        nome = input("Nome do cliente: ") #Inserir nome do cliente
        livro = input("Livro a ser emprestado: ") # O nome do livro a ser emprestado
        DDE = input("Data de retirada: ") #DDE = data de empréstimo, data de retirada
        DDD = input("Data da Devolução: ") #DDD = data de devolução, data de entrega
        contact = input("Forma de contato com o cliente: ") #Inserir a forma de contato do cliente

        #Verifica se o livro inserido está presente na lista
        if livro in livros:
            print("Emprestimo Realizado!")
            #Instância 
            emprestado = Cliente(nome, livro, DDE, DDD, contact)

            #Adiciona na lista cliente as informações da instância
            cliente.append(emprestado)

        os.system("pause")
        os.system("cls")
        
    #Função de empréstimo  
    elif empre == 2:

        #Mede o comprimento da lista
        if cliente.__len__() >= 1:
            #Cria um contador para a lista 
            count = 1

            print("Usuario que realizaram um emprestimo: \n ")
            #Verifica se o cliente existe na lista 
            for user in cliente:
                print(f"{count}º:\n Nome do cliente: {user.getNC()} \n Livro emprestado: {user.getLivro()} \n Contato: {user.getContato()} \n")
                #Imrpime as infroamções do cliente
                count += 1
                #Incrementa mais um na lista quando fizer mais um empréstimo 

            os.system("pause")

            #Inserir a posição do cliente desejado na lista
            mudar_empre = int(input("Qual a posição do usuario que vc deseja realizar a mudança do livro emprestado? \n --> "))
            mudar_livro = input("Qual o novo livro do cliente? \n ---> ")

            os.system("cls")

            #Verifica o número do cliente 
            if cliente.__len__() <= mudar_empre:
                if mudar_livro in livros:  #Verifica se o novo livro está dentro da lista
                    cliente[mudar_empre - 1].setLivro(mudar_livro) #Muda as informações de empréstimo 

                    print("Novo cadastro realizado com sucesso! ")

                    os.system("pause")
                    os.system("cls")

                #Caso o livro não esteja cadastrado 
                else:
                    print("Livro não encontrado...")

                    os.system("pause")
                    os.system("cls")

            #Caso o usuário inserido não existir
            else:
                print("Nenhum usuário encontrado...")

                os.system("pause")
                os.system("cls")

        #Caso um usuário não tenha feito um empréstimo e registrado seu nome
        else:
            print("Nenhum usuário cadastrado...")
            os.system("pause")
            os.system("cls")

    #Caso o usuário insira uma opção inexistente
    else:
        print("Opção inválida...")
        os.system("pause")
        os.system("cls")

##Função Cadasto do nome dos livros literários, onde é cadastrado e salvo dentro da lista "livro"
def cadastro():
    print("---- CADASTRO DE LIVROS ----")
    nome = input("Informe o nome do livro\n -->")

    livro = (nome)  
        
    return livro

#Função Cadasto de generos literários, onde é cadastrado e salvo dentro da lista "genero"
def cadastro2():
    genero = input("Informe o gênero do seu livro\n -->")

    generoTipo = (genero)
    return generoTipo

#Função Cadasto do autor dos livros, onde é cadastrado e salvo dentro da lista "autor"
def cadastro3():
    autor = input("Informe o autor do livro \n -->")

    autorLivro = (autor)
    return autorLivro
    
        
