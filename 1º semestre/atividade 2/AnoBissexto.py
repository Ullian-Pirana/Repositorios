import os

print("Bem-vindo ao Desafio da Vila das Estações!")

print("------------------------------------------")

print("Você foi convocado para ajudar os moradores da Vila das Estações a determinar se um ano é bissexto ou não,")

print("mantendo viva a tradição de celebrar os anos bissextos com festivais especiais.")

print("       ")

ano = int(input("Por favor, digite um ano para verificar se é bissexto:"))

print("       ")

Div4 = ano%4
Div100 = ano%100
Div400 = ano%400

if Div4 == 0:
    if Div100 == 0:
        if Div400 == 0:
            print("o ano", ano, "É bissexto")
        else:
            print("o ano", ano, "NÃO é bissexto")
    else:
        print("o ano", ano, "É bissexto")
else:
    print("o ano", ano, "NÃO é bissexto")

os.system ("pause")