import os

sair = 1

while sair == 1:
    
    compra = (input("Nome do produto: "))
    preço = float(input("Preço Do Produto:"))
    quantidade = int(input("Quantidade: "))
    
    print("  ")
    print("Você gostaria de cadastrar mais algum produto: ")
    print(" ")
    print("1 pra Sim")
    print("0 pra Não")
    print(" ")

    YN = int(input("-->"))
    if YN == 1:
        sair = 1
    else:
        sair = 0

PrecoTotal = preço * quantidade

print("produtos cadastrados: ", compra)
print("quantidade: ", quantidade)
print("preço total: ", PrecoTotal)

os.system("pause")