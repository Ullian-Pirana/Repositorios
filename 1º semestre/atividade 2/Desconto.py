import os

print("Bem-vindo à Sol & Mar - Sua Loja de Artigos de Praia Favorita!")

print("----------------------------------------------------------------")

print("Hoje é um dia perfeito para planejar sua próxima aventura à praia!")

print("Aproveite nossa promoção especial de descontos progressivos e leve os melhores equipamentos para aproveitar o sol e o mar!")

compra = float(input ("Por favor, digite o valor total de sua compra: R$"))

print("       ")
print("------------------------------------------------------------------------------------------------------------------------")
print("       ")

if compra < 50:
    print("não qualificado pra desconto")

if compra >= 50 and compra < 100: 
    print("Com base no valor total da sua compra, você se qualifica para o desconto de 5%.")

if compra >= 100 and compra < 150:
    print("Com base no valor total da sua compra, você se qualifica para o desconto de 10%.")

if compra >= 150 and compra < 200:
    print("Com base no valor total da sua compra, você se qualifica para o desconto de 15%.")

if compra >= 200 and compra < 250:
    print("Com base no valor total da sua compra, você se qualifica para o desconto de 20%.")

if compra >= 250:
    print("Com base no valor total da sua compra, você se qualifica para o desconto de 25%.")

print("       ")
print("------------------------------------------------------------------------------------------------------------------------")
print("       ")
print("Veja o resumo da sua compra:")

print("Valor total da compra: R$", compra)

desconto = float(input("Desconto aplicado:"))

ValorDesconto =  compra * (desconto/100)

final = compra - ValorDesconto

print("Total a pagar:", final)

os.system ("pause")