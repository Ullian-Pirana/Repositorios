import os

print("Bem-vindo à Ordenação Matemática!")
print("----------------------------------")
print("Por favor, digite os três números que deseja ordenar:")


n1 = int(input("Número 01:"))

n2 = int(input("Número 02:"))

n3 = int(input("Número 03:"))

print(" ")

print("Você digitou os números:", n1, n2, n3)

print("              ")
print("----------------------------------")
print("              ")

if n1 < n2 and n1 < n3 and n2 > n1 and n2 < n3 and n3 > n1 and n3 > n2:
    print ("Aqui está a ordem crescente dos números:", n1, n2, n3)

if n2 < n1 and n2 < n3 and n1 > n2 and n1 < n3 and n3 > n1 and n3 > n2:
    print ("Aqui está a ordem crescente dos números:", n2, n1, n3)

if n3 < n2 and n3 < n1 and n2 > n3 and n2 < n1 and n1 > n3 and n1 > n2:
    print ("Aqui está a ordem crescente dos números:", n3, n2, n1)

if n1 < n2 and n1 < n3 and n3 > n1 and n3 < n2 and n2 > n1 and n2 > n3:
    print ("Aqui está a ordem crescente dos números:", n1, n3, n2)

if n2 < n1 and n2 < n3 and n3 > n2 and n3 < n1 and n1 > n3 and n1 > n2:
    print ("Aqui está a ordem crescente dos números:", n2, n3, n1)

if n3 < n2 and n3 < n1 and n1 > n3 and n1 < n2 and n2 > n3 and n2 > n1:
    print ("Aqui está a ordem crescente dos números:", n3, n1, n2)

os.system("pause")