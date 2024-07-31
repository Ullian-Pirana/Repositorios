import os

sair = 1

nome1 = ""
nome2 = ""
nome3 = ""

preço1 = 0
preço2 = 0
preço3 = 0

quant1 = 0
quant2 = 0
quant3 = 0

while sair == 1:
    print("O que gostaria de fazer? ")
    print(" ")
    print(" 1 pra cadastrar um produto \n 2 pra ver produtos cadastrados \n 3 pra alterar a quantidade de um produto \n 4 pra excluir um produto cadastrado \n 5 pra encerrar o programa")
    print(" ")

    escolha = int(input("--> ")) 
    print(" ")

    if escolha == 1:
        print("----------------------------------------------------------------------------------------------")
        print("Qual produto gostaria de cadastrar?")
        print(" ")
        print(" 1- produto 01 \n 2- produto 02 \n 3- produto 03") 
        print(" ")

        EscolhaProd = int(input("--> "))
        print(" ")        

        if EscolhaProd == 1:
            print("----------------------------------------------------------------------------------------------")
            nome1 = input("produto 01: ")
            preço1 = float(input("preço: "))
            quant1 = int(input("quantidade: "))
            print(" ")
            print("Cadastro realizado")
            print("----------------------------------------------------------------------------------------------")
            print(" ")
       
        elif EscolhaProd == 2:
            print("----------------------------------------------------------------------------------------------")
            nome2 = input("produto 02: ")
            preço2= float(input("preço: "))
            quant2 = int(input("quantidade: "))
            print(" ")
            print("Cadastro realizado")
            print("----------------------------------------------------------------------------------------------")
            print(" ")
       
        elif EscolhaProd == 3:
            print("----------------------------------------------------------------------------------------------")
            nome3 = input("produto 03: ")
            preço3 = float(input("preço: "))
            quant3 = int(input("quantidade: "))
            print(" ")
            print("Cadastro realizado")
            print("----------------------------------------------------------------------------------------------")
            print(" ")
        
        else:
            print("opção invalida")  
    
    elif escolha == 2:
        print("----------------------------------------------------------------------------------------------")
        print("Produtos cadastrados: ")
        print(" ")

        PçTotal1 = preço1 * quant1
        PçTotal2 = preço2 * quant2
        PçTotal3 = preço3 * quant3

        print("produto 01: \n nome:", nome1, "\n preço:", preço1, "\n quantidade:", quant1, "\n preço total: ", PçTotal1)
        print(" ")
        print("produto 02: \n nome:", nome2, "\n preço:", preço2, "\n quantidade:", quant2, "\n preço total: ", PçTotal2)
        print(" ")
        print("produto 03: \n nome:", nome3, "\n preço:", preço3, "\n quantidade:", quant3, "\n preço total: ", PçTotal3)
        print("----------------------------------------------------------------------------------------------")
        print(" ")
   
    elif escolha == 3:
        print("qual produto gostaria de alterar? \n \n 1 para o produto 01 \n 2 para o produto 02 \n 3 para o produto 03")
        print(" ")
        alterar = int(input("--> "))
        print(" ")
       
        if alterar == 1:
            print("produto:", nome1)
            print("Quantidade atual:", quant1)
            print(" ")
            quant1 = int(input("Nova quantidade: "))
            print(" ")
            print("Quantidade alterada")
            print(" ")
            print("----------------------------------------------------------------------------------------------")
            print(" ")     
       
        elif alterar == 2:
            print("produto:", nome2)
            print("Quantidade atual:", quant2)
            print(" ")
            quant2 = int(input("Nova quantidade: "))
            print(" ")
            print("Quantidade alterada")
            print(" ")
            print("----------------------------------------------------------------------------------------------")
            print(" ")
       
        elif alterar == 3:
            print("produto:", nome3)
            print("Quantidade atual:", quant3)
            print(" ")
            quant3 = int(input("Nova quantidade: "))
            print(" ")
            print("Quantidade alterada")
            print(" ")
            print("----------------------------------------------------------------------------------------------")
            print(" ")
       
        else:
            print("Opção invalida")
            print(" ")
   
    elif escolha == 4:
        print("Qual produto gostaria de excluir? \n \n 1 para o produto 01 \n 2 para o produto 02 \n 3 para o produto 03")
        print(" ")
        
        excluir = int(input("-->"))
        print(" ")

        if excluir == 1:
            print("Excluindo produto 01...")
            nome1 = ""
            preço1 = 0
            quant1 = 0
            print(" ")
            print("Produto excluido")
            print(" ")
            print("----------------------------------------------------------------------------------------------")
            print(" ")
       
        elif excluir == 2:
            print("Excluindo produto 02...")

            nome2 = ""
            preço2 = 0
            quant2 = 0
            print(" ")
            print("Produto excluido")
            print(" ")
            print("----------------------------------------------------------------------------------------------")
            print(" ")

        elif excluir == 3:
            print("Excluindo produto 03...")

            nome3 = ""
            preço3 = 0
            quant3 = 0
            print(" ")
            print("Produto excluido")
            print(" ")
            print("----------------------------------------------------------------------------------------------")
            print(" ")

        else:
            print("Opção invalida")
            print(" ")

    elif escolha == 5:
        print("Realmente deseja encerrar o programa? \n \n 1 pra sim \n 0 pra não \n")
        encerrar = int(input("-->")) 
        print(" ")
        
        if encerrar == 1:
            sair = 0
            print("Encerrando...")
        else:
            sair = 1
os.system("pause")