import os 

x = 1

while x == 1:
 a = int(input("1 numero: "))
 b = int(input("2 numero: "))
 c = int(input("3 numero: "))

 print(" ")
 print ("numeros:",a,",",b, ",",c)
 print(" ")

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
 
 print(" ")

 print("gostaria de repetir o programa?")

 print("0 pra SIM")

 print("1 pra NÃO")

 print(" ")

 sair = int(input("--->"))

 if sair == 0:
    x = 1
 else:
    x = 0
    print("Encerrando...")

os.system("pause")