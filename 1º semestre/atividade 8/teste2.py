num = []

n = 0
ad = int(input("---> "))

print("fatoração de: ", ad)
print(" ")

for fat in range (1, ad):
    n += 1
    calc = ad * fat
    RF = ad * fat
    print(ad, "*", n, "=", calc)

print(" ")
print("Resultado final: ", RF)