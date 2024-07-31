import os

sair = 1

while sair == 1:
    print(" ")
    produto = input("produto: ")
    preço = float(input("Preço Do Produto: "))
    quantidade = int(input("Quantidade: "))
    
    PrecoTotal = preço * quantidade

    print("-----------------------------------------------------------------------------------------")

    print("o que gostaria de fazer agora?")
    print(" ")
    print("1 - ver produto cadastrado")
    print("2 - excluir produto cadastrado")
    print("3 - alterar quantidade do produto")
    print("   ")

    opcao = int(input("--> "))

    print("  ")

    if opcao == 1:
        print(" produto cadastrado: ", produto)

        print(" quantidade: ", quantidade)

        print(" preço:",preço, "\n preço total:", PrecoTotal )

        print("------------------------------------------------------------------------------------------")

        print("Você gostaria de sair do programa? ")
        print(" ")
        print("1 pra Sim")
        print("  ")
        print("0 pra Não")
        print(" ")

        YN = int(input("--> "))
        if YN == 1:
            sair = 0
            print("encerrando...")
        else:
            sair = 1
            print(" ")
            print("o que gostaria de fazer?")
            print(" ")
            print("1- excluir cadastro")
            print("2- alterar a quantidade do produto")
            print(" ")

            opcao2 = int(input("--> "))
            print(" ")
            
            if opcao2 == 1:   
                 print("você tem certeza que quer excluir o produto cadastrado?")
                 print("1 pra Sim")
                 print("0 pra Não")
                 print(" ")
                 print("caso escolha excluir o cadastro isso irá encerrar o programa")
                 print(" ")

                 SN = int(input("-> "))

                 if SN == 1:
                  sair = 0
                  print("  ")
                  print("excluindo cadastro...")
                  print(" ")
                  print("encerrando...")

                 else:
                  sair = 1
                  print("reiniciando programa...")
                  print("--------------------------------------------------------------------------------------")
                  print(" ")

            elif opcao2 == 2:  
                       print("gostaria de aumentar ou diminuir?")
                       print(" ")
                       print("1- aumentar")
                       print("2- diminuir")
                       print(" ")

                       escolha = int(input("--> "))
                       print(" ")
        
                       if escolha == 1:
                        print("quantidade atual:", quantidade)
                        print(" ")
                        print("gostaria de aumentar em quanto?")
                        print(" ")

                        mais = int(input("-> "))

                        soma = quantidade + mais

                        print("calculando...")
                        print("  ")
                        print("nova quantidade=", soma)
                        print(" ")

                        print("Você gostaria de repetir o programa? ")
                        print(" ")
                        print("1 pra Sim")
                        print("  ")
                        print("0 pra Não")
                        print(" ")

                       elif escolha == 2:
                        print("quantidade atual:", quantidade)
                        print(" ")
                        print("gostaria de diminuir em quanto?")
                        print(" ")

                        menos = int(input("-> "))

                        soma2 = quantidade - menos

                        print("calculando...")
                        print("  ")
                        print("nova quantidade = ", soma2)
                        print(" ")

                        print("Você gostaria de repetir o programa? ")
                        print(" ")
                        print("1 pra Sim")
                        print("  ")
                        print("0 pra Não")
                        print(" ")

                        YN2 = int(input("--> "))
                        if YN2 == 1:
                         sair = 1
                        else:
                         sair = 0
                         print("encerrando...")

    elif opcao == 2:
        print("você tem certeza que quer excluir o produto cadastrado?")
        print(" ")
        print("1 pra Sim")
        print("0 pra Não")
        print(" ")
        print("caso escolha excluir o cadastro isso irá encerrar o programa")
        print(" ")

        SN2 = int(input("-> "))

        if SN2 == 1:
            sair = 0
            
            print("  ")
            print("excluindo cadastro...")
            print(" ")
            print("encerrando programa...")

        else:
            sair = 1
            print("reiniciando programa...")
            print("--------------------------------------------------------------------------------------")
            print(" ")

    elif opcao == 3:
        print("gostaria de aumentar ou diminuir?")
        print(" ")
        print("1- aumentar")
        print("2- diminuir")
        print(" ")

        escolha2 = int(input("--> "))

        print(" ")
        
        if escolha2 == 1:
            print("quantidade atual:", quantidade)
            print(" ")
            print(" gostaria de aumentar em quanto?")
            print(" ")

            mais2 = int(input("-> "))

            soma2 = quantidade + mais2

            print("calculando...")
            print("  ")
            print("nova quantidade = ", soma2)
            print(" ")

            print("Você gostaria de repetir o programa? ")
            print(" ")
            print("1 pra Sim")
            print("  ")
            print("0 pra Não")
            print(" ")

            YN3 = int(input("--> "))
            if YN3 == 1:
             sair = 1
            else:
             sair = 0
             print("encerrando...")

        elif escolha2 == 2:
             print("quantidade atual:", quantidade)
             print(" ")
             print(" gostaria de diminuir em quanto?")
             print(" ")

             menos2 = int(input("-> "))

             soma2 = quantidade - menos2

             print("calculando...")
             print("  ")
             print("nova quantidade = ", soma2)
             print(" ")

             print("Você gostaria de repetir o programa? ")
             print(" ")
             print("1 pra Sim")
             print("  ")
             print("0 pra Não")
             print(" ")

             YN4 = int(input("--> "))
             if YN4 == 1:
              sair = 1
             else:
              sair = 0
              print("encerrando...")
os.system("pause")