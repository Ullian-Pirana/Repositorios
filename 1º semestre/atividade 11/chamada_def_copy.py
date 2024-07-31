import os

TurmaA = ["\n Aluno: Alice Nº 1 \n",
"Aluno: Beatriz Nº 2\n",
"Aluno: Carlos Nº 3\n",
"Aluno: Daniel Nº 4\n",
"Aluno: Enzo Nº 5\n",
"Aluno: Fernanda Nº 6\n",
"Aluno: Gabriela Nº 7\n",
"Aluno: Henrique Nº 8\n",
"Aluno: Isabela Nº 9\n",
"Aluno: João Nº 10\n",
"Aluno: Laura Nº 11\n",
"Aluno: Lucas Nº 12\n",
"Aluno: Manuela Nº 13\n",
"Aluno: Mateus Nº 14\n",
"Aluno: Natália Nº 15\n"]

TurmaB = ["\nAluno: Ana Nº 1\n",
"Aluno: Bernardo Nº 2\n",
"Aluno: Bruna Nº 3\n",
"Aluno: Carolina Nº 4\n",
"Aluno: Davi Nº 5\n",
"Aluno: Eduardo Nº 6\n",
"Aluno: Felipe Nº 7\n",
"Aluno: Giovanna Nº 8\n",
"Aluno: Gustavo Nº 9\n",
"Aluno: Helena Nº 10\n",
"Aluno: Isadora Nº 11\n",
"Aluno: Julia Nº 12\n",
"Aluno: Leonardo Nº 13\n",
"Aluno: Luiza Nº 14\n",
"Aluno: Marcelo Nº 15\n"]

TurmaC = ["\nAluno: André Nº 1\n",
"Aluno: Arthur Nº 2\n",
"Aluno: Camila Nº 3\n",
"Aluno: Clara Nº 4\n",
"Aluno: Fernanda Nº 5\n",
"Aluno: Gabriel Nº 6\n",
"Aluno: Guilherme Nº 7\n",
"Aluno: Isabela Nº 8\n",
"Aluno: João Nº 9\n",
"Aluno: Juliana Nº 10\n",
"Aluno: Laura Nº 11\n",
"Aluno: Leonardo Nº 12\n",
"Aluno: Lucas Nº 13\n",
"Aluno: Maria Nº 14\n",
"Aluno: Matheus Nº 15\n"]

TurmaD = ["\nAluno: Amanda Nº 1\n",
"Aluno: Bruno Nº 2\n",
"Aluno: Caio Nº 3\n",
"Aluno: Carolina Nº 4\n",
"Aluno: Daniel Nº 5\n",
"Aluno: Eduardo Nº 6\n",
"Aluno: Fernando Nº 7\n",
"Aluno: Gabriela Nº 8\n",
"Aluno: Gustavo Nº 9\n",
"Aluno: Isabela Nº 10\n",
"Aluno: João Nº 11\n",
"Aluno: Larissa Nº 12\n",
"Aluno: Letícia Nº 13\n",
"Aluno: Lucas Nº 14\n",
"Aluno: Marcela Nº 15\n"]

chamada1 = { "Turma A:" : [TurmaA]}
chamada2 = { "Turma B:" : [TurmaB]}
chamada3 = { "Turma C:" : [TurmaC]}
chamada4 = { "Turma D:" : [TurmaD]}

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