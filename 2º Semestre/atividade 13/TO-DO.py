from Defs import *

sair = 1

while sair == 1:
    
    escolha = menu()
    os.system("cls")

    if escolha == 1:
          
        add()

    if escolha == 2:
        
        ver()
    
    if escolha == 3:
        
        excluir()
    
    if escolha == 4:
        print("\t Encerrando Programa...")
        sair = 0

        clean()
    
os.system("pause")