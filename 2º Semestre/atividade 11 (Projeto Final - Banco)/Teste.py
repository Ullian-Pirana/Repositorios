from classis import *
import os

esca = int(input("asfjasn: "))

while True:
    if esca == 1:
        contaC =ContaCorrente()
        os.system("pause")
        os.system("cls")
    elif esca == 2:
        contaP = ContaPoupanca()
        os.system("pause")
        os.system("cls")
    elif esca == 3:
        cliente = Cliente("pinto", "123.456.789-11")
        os.system("pause")
        os.system("cls")
    elif esca == 4:
        ull = Banco()
        os.system("pause")
        os.system("cls")
    elif esca == 5:
        os.system("pause")
        os.system("cls")
        break
    else:
        print("Pantene queima rosca")