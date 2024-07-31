import os

a = int(input("1 numero: "))
b = int(input("2 numero: "))
c = int(input("3 numero: "))
d = int(input("4 numero: "))
e = int(input("5 numero: "))
print ("numeros:",a,",",b, ",",c, ",",d, ",",e)

if a > b and a > c and a < d and a < e:
    print("a mediana é: ", a)

if a > d and a > e and a < b and a < c:
    print("a mediana é: ", a)

if a > b and a > d and a < c and a < e:
    print("a mediana é: ", a)

if a > e and a > c and a < d and a < b:
    print("a mediana é: ", a)

if a > e and a > b and a < d and a < c:
    print("a mediana é: ", a)

if b > a and b > c and b < d and b < e:
    print("a mediana é: ", b)

if b > d and b > e and b < a and b < c:
    print("a mediana é: ", b)

if b > a and b > d and b < c and b < e:
    print("a mediana é: ", b)

if b > e and b > c and b < d and b < a:
    print("a mediana é: ", b)

if b > e and b > a and b < d and b < c:
    print("a mediana é: ", b)

if c > b and c > a and c < d and c < e:
    print("a mediana é: ", c)

if c > d and c > e and c < b and c < a:
    print("a mediana é: ", c)

if c > b and c > d and c < a and c < e:
    print("a mediana é: ", c)

if c > e and c > a and c < d and c < b:
    print("a mediana é: ", c)

if c > e and c > b and c < d and c < a:
    print("a mediana é: ", c)

if d > b and d > c and d < a and d < e:
    print("a mediana é: ", d)

if d > a and d > e and d < b and d < c:
    print("a mediana é: ", d)

if d > b and d > a and d < c and d < e:
    print("a mediana é: ", d)

if d > e and d > c and d < a and d < b:
    print("a mediana é: ", d)

if d > e and d > b and d < a and d < c:
    print("a mediana é: ", d)

if e > b and e > c and e < d and e < a:
    print("a mediana é: ", e)

if e > d and e > a and e < b and e < c:
    print("a mediana é: ", e)

if e > b and e > d and e < c and e < a:
    print("a mediana é: ", e)

if e > a and e > c and e < d and e < b:
    print("a mediana é: ", e)

if e > a and e > b and e < d and e < c:
    print("a mediana é: ", e)

os.system("pause")