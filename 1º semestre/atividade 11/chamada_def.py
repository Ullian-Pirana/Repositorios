import os

chamada1 = { "Turma A: \n" : "Alice Mepelo Nº 1 \n Beatriz Globel Nº 2\n Carlos Dourado Nº 3\n Daniel Vivara Nº 4\n Enzol peixeira Nº 5\n Fernanda Padeiro Nº 6\n Gabriela Especel Nº 7\n Henrique Contecel Nº 8\n Isadora Pinto Nº 9\n João Pehféjoh Nº 10\n Laura Tomate Nº 11\n Lucas Mynuuts Nº 12\n Manuela Motos Nº 13\n Mateu Baguos Nº 14\n Natália Manjedora Nº 15\n "}
chamada2 = { "Turma B: \n" : "Benjamin Scott Nº 1\n Elijahco Meupatel Nº 2\n Emily Garcia Nº 3\n Ethan Murphy Nº 4\n Gabriel Martinez Nº 5\n Grace Johnson Nº 6\n Liam Brown Nº 7\n Lucas Wright Nº 8\n Mia Chavez Nº 9\n Natalie Baker Nº 10\n Penelope Kim Nº 11\n Scarlett Williams Nº 12\n Victoria Hernandez Nº 13\n Xavier Jones Nº 14\n Zoey Sullivan Nº 15\n"}
chamada3 = { "Turma C: \n" : "Ariti metica Nº 1\n Aurora Smith Nº 2\n Chloe Morales Nº 3\n Donovan Chang Nº 4\n Harper Lee Nº 5\n Henry Lopez Nº 6\n Isabella Patel Nº 7\n Jackson Kim Nº 8\n Logan Silva Nº 9\n Mason Gonzalez Nº 10\n Olivia Wang Nº 11\n Oliver Santos Nº 12\n Sophia Khan Nº 13\n Stella Martinez Nº 14\n William Ramirez Nº 15\n"}
chamada4 = { "Turma D: \n" : "Alexander Nguyen Nº 1\n Amelia Cooper Nº 2\n Audrey Lewis Nº 3\n Ava Rivera Nº 4\n Caleb Walker Nº 5\n Charlotte Taylor Nº 6\n Daniel Adams Nº 7\n Eleanor Phillips Nº 8\n Jack Reed Nº 9\n Lily Almeida Nº 10\n Luna Nguyen Nº 11\n Maxwell Santos Nº 12\n Noah Thompson Nº 13\n Samuel O'Connor Nº 14\n Tobias Rodriguez Nº 15\n"}

def stop():
    os.system("pause")
    os.system("cls")

def menu():
    print("<---MENU---> \n")

    escolha = int(input("O que gostaria de fazer? \n 1 - Chamada \n 2 - Sair \n --> "))

    return escolha

def presença():
    
    qual = int(input("De qual turma Gostaria de fazer a chamada? \n 1 - Turma A \n 2 - Turma B \n 3 - Turma C \n 4 - Turma D \n --> "))

    if qual == 1:

        print("---TURMA A--- \n")

        for turma, aluno in chamada1.items():
            print(turma, aluno)

    elif qual == 2:

        print("---TURMA B--- \n")

        for turma, aluno in chamada2.items():
            print(turma, aluno)

    elif qual == 3:

        print("---TURMA C--- \n")

        for turma, aluno in chamada3.items():
            print(turma, aluno)

    elif qual == 4:

        print("---TURMA D--- \n")

        for turma, aluno in chamada4.items():
            print(turma, aluno)