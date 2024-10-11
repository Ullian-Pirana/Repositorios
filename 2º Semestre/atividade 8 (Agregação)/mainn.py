import os
from carrinho_compras import *

Carlos = Cliente("Carlos", "666.777.0024")

Tomate = Produtos("Tomate", 7.50)
Costela = Produtos("Costela", 9.76)
Salmão = Produtos("Salmão", 15.87)
Alfajor = Produtos("Alfajor", 6.0)
Doce_batata_doce = Produtos("Doce de Batata Doce", 8.99)

Carlos.addProd(Tomate)
Carlos.addProd(Costela)
Carlos.addProd(Salmão)
Carlos.addProd(Alfajor)
Carlos.addProd(Doce_batata_doce)

print(f"Cliente: {Carlos.getNome()}")
print(f"Cpf: {Carlos.getCpf()} \n")
print(f"Lista de Compras de {Carlos.getNome()}: ")

posicao = 1
for prod in Carlos.getCarrinho():
    print(f"  {posicao}º: \n produto: {prod.getNome()} \n valor: {prod.getValor()} \n")
    posicao += 1
    