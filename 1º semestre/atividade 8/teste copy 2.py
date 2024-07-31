
import os

num = []
x = 1

while x == 1:
    mult = float(input("Insira um número: "))

    repit = 1
    while repit == 1:
        soma = float(input("Insira um número: "))
        num.append(float(soma))
        print(" ")

        escolha = int(input("gostaria de adicionar outro numero? \n 1 - SIM \n 2 - NÃO \n --> "))

        if escolha == 1:
         print(" ")
         os.system("cls")
        elif escolha == 2:
         print(" ")
         repit = 2
         x = 2

for num2 in num:
    mult *= num2

print("A soma dos números é:", mult)


