import os

idade=int(input("informe sua idade: "))

print ("voce tem:", idade)

aposentadoria = 65
idade2 = aposentadoria - idade
idade3 = idade - aposentadoria

if idade <= aposentadoria:
  print("faltam", idade2, "anos pra sua aposentadoria")
else:
  print("voce já é aposentado a", idade3, "anos")
os.system ("pause")