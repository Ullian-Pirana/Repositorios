import os
######################################################################################################################

print("Bem-vindo ao Enigma dos Números!")
print("--------------------------------")
print("Você encontrou uma caixa misteriosa no parque, contendo um papel com um enigma.")
print("O enigma diz que para abrir o próximo compartimento, você deve determinar se um número é par ou ímpar")
print("Vamos resolver esse mistério!")

print(" ")

PouI = int(input("Por favor, digite um número inteiro:"))

print(" ")

if PouI%2 == 0:
    print("o numero", PouI,"é PAR")
else:
    print("o numero", PouI,"é IMPAR")

print(" ")

print("Obrigado por jogar!")

os.system ("pause")