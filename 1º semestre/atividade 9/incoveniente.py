import os

cad = []
sen = []

a = 1

while a == 1:
    cadastro = input("login: ")
    senha  = input("senha: ")
    sen.append(senha)
    cad.append(cadastro)
    print(" ")

    escolha = int(input("1- login \n ---> "))

    if escolha == 1:

        log = input("login: ")
        senh = input("Senha: ")
        cont = -1

        for n in cad:  
            cont += 1   
            if log == n:
                if sen[cont] == senh:
                    print("Kmila")
                else:
                    print("senha invalida")
