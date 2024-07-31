import os

dicionario = {
    "Nome" : "carlos",
    "Idade" : 25,
    "Cidade" : "SP"
}

dicionario["Nome"] = "marquinho"
print(dicionario["Nome"])

for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

os.system("pause")