import os
a = int(input("1 numero: "))
b = int(input("2 numero: "))
c = int(input("3 numero: "))
print ("numeros:",a,",",b, ",",c)

if a > b and a < c:
    print("a mediana é: ", a)

if a > c and a < b:
    print("a mediana é: ", a)

if b > a and b < c:
    print("a mediana é: ", b)

if b > c and b < a:
    print("a mediana é: ", b)

if c > a and c < b:
    print("a mediana é: ", c)

if c > b and c < a:
    print("a mediana é: ", c)

os.system("pause")