import os

sair = 1
NT = []
DT = []
UT = []

while sair == 1:
    print("""
          ---BEM VINDO A LISTA DE TAREFAS!!!---
         """)
    
    escolha = int(input("O que gostaria de fazer? \n 1 - Adicionar uma tarefa \n 2 - Ver a lista de tarefas \n 3 - Excluir uma terefa \n 4 - Encerrar o programa \n ---> "))
   
    print(" ")

    if escolha == 1:
        print("Voce escolheu adicionar uma tarefa")
        print(" ")
        NT.append(input(" Titulo da tarefa: "))
        DT.append(input(" Descrição da tarefa: "))
        UT.append(input(" Urgencia da tarefa: "))

        print(" ")
        print("TAREFA ADICIONADA")
        print(" ")

        os.system("pause")
        os.system("cls")

    elif escolha == 2:
        print("LISTA DE TAREFAS: ")
        print(" ")

        t = 0
        d = 0
        u = 0

        for listar in (NT):
            t += 1
            print(t,"º Tarefa: ", listar)
        print(" ")

        for listar2 in (DT):
            d += 1
            print(d,"º Descrição: ", listar2)
        print(" ")

        for listar3 in (UT):
            u += 1
            print(u,"º Grau de urgencia: ", listar3)
        print(" ")

        os.system("pause")
        os.system("cls")

    elif escolha == 3:
      print("Qual tarefa gostaria de excluir? ")
      print(" ")
      tar = 0
      print("Tarefas: ")
      print(" ")

      for tarefas in (NT):
          tar += 1
          print(tar, "º tarefa: ", tarefas)

      print(" ")

      excluir = int(input("Tarefa a ser excluida: "))

      NT.pop(excluir - 1)
      DT.pop(excluir - 1)
      UT.pop(excluir - 1)

      print(" ")
      print("TAREFA EXCLUIDA...")
      print(" ")

      os.system("pause")
      os.system("cls")

    elif escolha == 4:

        encerrar = int(input("Gostaria de encerrar o programa? \n 1 - SIM \n 2 - NÃO \n ---> "))
        print(" ")
        
        if encerrar == 1:
            sair = 0
            print("ENCERRANDO...")
        elif encerrar == 2:
            os.system("pause")
            os.system("cls")
        else:
            print("Opção invalida")
            os.system("pause")
            os.system("cls")

    else:
        print("Opção invalida...")
        os.system("pause")
        os.system("cls")

os.system("pause")
