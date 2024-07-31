num = []

x = 1

while x == 1:
    soma = float(input("Insira um número: "))
    num.append(float(soma))
    print(" ")

    escolha = int(input("gostaria de adicionar outro numero? \n 1 - SIM \n 2 - NÃO \n --> "))

    if escolha == 1:
       print(" ")
    elif escolha == 2:
        print(" ")
        x = 2

soma = 0

for num2 in num:
    soma += num2

print("A soma dos números é:", soma)


