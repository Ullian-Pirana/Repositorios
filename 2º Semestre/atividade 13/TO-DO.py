from Defs import *

sair = 1

while sair == 1:
    
    escolha = menu()
    clean()

    if escolha == 1:
          
          add()

    if escolha == 2:
        pass
    
    if escolha == 3:
        pass
    
    if escolha == 4:
        print("\t Encerrando Programa...")
        sair = 0

        clean()
    
os.system("pause")