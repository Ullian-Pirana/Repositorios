print("---FATORIAL---")

n = 0
numero = int(input("Digite um numero: "))
fatorial = numero

for i in range(1,numero):
 n += 1
 print(numero)
 fatorial = fatorial * i
 print("O Fatorial de", numero,"*", n , "É", fatorial)

print("")
print("resultado final:", fatorial)