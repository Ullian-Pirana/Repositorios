import os 

sair = 1

tarefa1 = ""
tarefa2 = ""
tarefa3 = ""
tarefa4 = ""
tarefa5 = ""
tarefa6 = ""

desc1 = ""
desc2 = ""
desc3 = ""
desc4 = ""
desc5 = ""
desc6 = ""

urgen1 = ""
urgen2 = ""
urgen3 = ""
urgen4 = ""
urgen5 = ""
urgen6 = ""

while sair == 1:
    print("----------------------------------------------------------------------------------------------------")
    print("O que gostaria de fazer? \n 1 - Adicionar tarefa \n 2 - Ver a lista de tarefas \n 3 - Excluir tarefa \n 4 - Encerrar ")
    print(" ")

    escolha = int(input("--> ")) 
    print(" ")

    if escolha == 1:
        print("----------------------------------------------------------------------------------------------------")
        print("Qual tarefa gostaria de adicionar? \n 1 - Tarefa01 \n 2 - Tarefa02 \n 3 - Tarefa03 \n 4 - Tarefa04 \n 5 - Tarefa05 \n 6 - Tarefa06")
        print(" ")

        adicionar = int(input("-->"))

        if adicionar == 1:
            tarefa1 = input("Tarefa: ")
            desc1 = input("Descrição: ")
            urgen1 = input("Grau de urgencia: ")
            print("Tarefa adicionada")
            print(" ")

        elif adicionar == 2:
            tarefa2 = input("Tarefa: ")
            desc2 = input("Descrição: ")
            urgen2 = input("Grau de urgencia: ")
            print("Tarefa adicionada")
            print(" ")

        elif adicionar == 3:
            tarefa3 = input("Tarefa: ")
            desc3 = input("Descrição: ")
            urgen3 = input("Grau de urgencia: ")
            print("Tarefa adicionada")
            print(" ")

        elif adicionar == 4:
            tarefa4 = input("Tarefa: ")
            desc4 = input("Descrição: ")
            urgen4 = input("Grau de urgencia: ")
            print("Tarefa adicionada")
            print(" ")

        elif adicionar == 5:
            tarefa5 = input("Tarefa: ")
            desc5 = input("Descrição: ")
            urgen5 = input("Grau de urgencia: ")
            print("Tarefa adicionada")
            print(" ")

        elif adicionar == 6:
            tarefa6 = input("Tarefa: ")
            desc6 = input("Descrição: ")
            urgen6 = input("Grau de urgencia: ")
            print("Tarefa adicionada")
            print(" ")

        else:
            print("Opção invalida")
            print(" ")

    elif escolha == 2:
        print("----------------------------------------------------------------------------------------------------")
        print("Lista de tarefas: ")
        print(" ")
    
        print("Tarefa01: \n Tarefa: ", tarefa1, "\n Descrição: ", desc1, "\n Grau de urgência: ", urgen1)
        print(" ")
        print("Tarefa02: \n Tarefa: ", tarefa2, "\n Descrição: ", desc2, "\n Grau de urgência: ", urgen2)
        print(" ")
        print("Tarefa03: \n Tarefa: ", tarefa3, "\n Descrição: ", desc3, "\n Grau de urgência: ", urgen3)
        print(" ")
        print("Tarefa04: \n Tarefa: ", tarefa4, "\n Descrição: ", desc4, "\n Grau de urgência: ", urgen4)
        print(" ")
        print("Tarefa05: \n Tarefa: ", tarefa5, "\n Descrição: ", desc5, "\n Grau de urgência: ", urgen5)
        print(" ")
        print("Tarefa06: \n Tarefa: ", tarefa6, "\n Descrição: ", desc6, "\n Grau de urgência: ", urgen6)
        print(" ")

    elif escolha == 3:
        print("----------------------------------------------------------------------------------------------------")
        print("Qual tarefa gostaria de excluir? \n 1 - Tarefa01 \n 2 - Tarefa02 \n 3 - Tarefa03 \n 4 - Tarefa04 \n 5 - Tarefa05 \n 6 - Tarefa06")
        print(" ")
        
        excluir = int(input("--> "))
        
        print(" ")

        if excluir == 1:
            tarefa1 = ""
            desc1 = ""
            urgen1 = ""
            print("Tarefa excluida...")
            print(" ")

        elif excluir == 2:
            tarefa2 = ""
            desc2 = ""
            urgen2 = ""
            print("Tarefa excluida...")
            print(" ")

        elif excluir == 3:
            tarefa3 = ""
            desc3 = ""
            urgen3 = ""
            print("Tarefa excluida...")
            print(" ")

        elif excluir == 4:
            tarefa4 = ""
            desc4 = ""
            urgen4 = ""
            print("Tarefa excluida...")
            print(" ")

        elif excluir == 5:
            tarefa5 = ""
            desc5 = ""
            urgen5 = ""
            print("Tarefa excluida...")
            print(" ")

        elif excluir == 6:
            tarefa6 = ""
            desc6 = ""
            urgen6 = ""
            print("Tarefa excluida...")
            print(" ")

        else:
            print("Opção invalida")
            print(" ")

    elif escolha == 4:
        print("----------------------------------------------------------------------------------------------------") 
        print("Gostaria de encerrar o programa? \n 1 pra sim \n 0 pra não")
        print(" ")

        encerrar = int(input("--> "))

        print(" ")

        if encerrar == 1:
            sair = 0
            print("Encerrando...")

        elif encerrar == 0:
            sair = 1
            print(" ")

        else:
            print("Opção invalida")
            print(" ")
            
    else:
        print("Opção invalida")
        print(" ")

os.system("pause")