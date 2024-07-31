print("---FATORAÇÂO---")

num_fat = int(input("Informa um valor inteiro que deseja fatorar\n-->"))

x = 1
for i in range(num_fat,0,-1):
    x *= i

for i in range(num_fat, 0,-1):
    if i != 1:
        print(f"{i} x" , end=" ")
    else:
        print(f"{i} =" , end=" ")