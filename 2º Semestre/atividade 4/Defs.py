import os
from classes import Gato, Cachorro

def menu():
    while True:

        print("---- SISTEMA DE VETERINARIA ----")
        print("01 - CADASTRAR ANIMAIS")
        print("02 - LISTAR ANIMAIS")
        print("03 - CONSULTA")
        print("00 - SAIR")
        print("")
        
        try:

            escolha = int(input("Qual opção deseja ? \n--> "))
            return escolha
            break

        except Exception as e:

            print(f"Impossivel concluir operação \n erro encontrado: {e}")
            os.system("pause")
            os.system("cls")

def cadastro():

    while True:
        
        while True:

            print("---- CADASTRO DE ANIMAIS ----")
            print("01 - CACHORRO")
            print("02 - GATO")
            print("00 - VOLTAR")
            print("")

            try:
                animal = int(input("Qual opção deseja ? \n--> "))
                break

            except Exception as e:
                print(f"Impossivel concluir operação \n erro encontrado: {e}")
                os.system("pause")
                os.system("cls")

        match animal:

            case 1:
                os.system("cls")

                while True:

                    print("---- CADASTRO DE CACHORRO ----")

                    try:
                        nome = input("Infome o nome do seu cachorro\n -->")
                        raca = input("Infome a raça do seu cachorro\n -->")
                        dono = input("Infome o seu nome\n -->")
                        idade = int(input("Infome a idade do seu cachorro\n -->"))

                        break

                    except Exception as e:
                        print(f"Impossivel concluir operação \n erro encontrado: {e}")
                        os.system("pause")
                        os.system("cls")

                cachorro = Cachorro(nome,raca,dono,idade)
                
                print("")
                print("CACHORRO CADASTRADO COM SUCESSO")
                os.system("pause")
                os.system("cls")

                return cachorro

            case 2:

                os.system("cls")

                while True:

                    print("---- CADASTRO DE GATO ----")

                    try:

                        nome = input("Infome o nome do seu gato\n --> ")
                        cor = input("Infome a cor do seu gato\n --> ")
                        dono = input("Infome o seu nome\n --> ")
                        idade = int(input("Infome a idade do seu gato\n --> "))

                        break

                    except Exception as e:

                        print(f"Impossivel concluir operação \n erro encontrado: {e}")
                        os.system("pause")
                        os.system("cls")

                gato = Gato(nome,cor,dono,idade)
                
                print("")
                print("GATO CADASTRADO COM SUCESSO")
                os.system("pause")
                os.system("cls")

                return gato
            
            case 0:

                print("")
                os.system("pause")
                os.system("cls")
                break

            case _:

                print("")
                print("OPÇÃO INVALIDA")
                os.system("pause")
                os.system("cls")
            
def listar(lista):
    
    while True:

        while True:

            print("---- LISTA DE ANIMAIS ----")
            print("01 - LISTAR TODOS OS ANIMAIS")
            print("02 - LISTAR TODOS OS CACHORROS")
            print("03 - LISTAR TODOS OS GATOS")
            print("00 - VOLTAR")

            try:

                escolha = int(input("Qual opção deseja ? \n--> "))
                os.system("cls")
                break

            except Exception as e:

                print(f"Impossivel concluir operação \n erro encontrado: {e}")
                os.system("pause")
                os.system("cls")

        match escolha:

            case 1:

                print("---- LISTA DE TODOS OS ANIMAIS ----\n")
                print("ID\tNOME\tIDADE\tESPECIE")
                

                cont = 1
                for animais in lista:
                    print(f"{cont}\t{animais.getNome()}\t{animais.getIdade()}\t{animais.getEspecie()}")
                    cont += 1

                print("")
                os.system("pause")
                os.system("cls")

            case 2:

                print("---- LISTA DE TODOS OS CACHORROS ----\n")
                print("ID\tNOME\tIDADE\tRAÇA\t\tDONO")            

                cont = 1
                for animais in lista:
                    if animais.getEspecie() == "Cachorro":
                        print(f"{cont}\t{animais.getNome()}\t{animais.getIdade()}\t{animais.getRaca()}\t\t{animais.getDono()}")
                        cont += 1

                print("")
                os.system("pause")
                os.system("cls")

            case 3:
                
                print("---- LISTA DE TODOS OS GATOS ----\n")
                print("ID\tNOME\tIDADE\tCOR\t\tDONO")            

                cont = 1
                for animais in lista:
                    if animais.getEspecie() == "Gato":
                        print(f"{cont}\t{animais.getNome()}\t{animais.getIdade()}\t{animais.getCor()}\t\t{animais.getDono()}")
                        cont += 1

                print("")
                os.system("pause")
                os.system("cls")

            case  0:
                print("")
                os.system("pause")
                os.system("cls")
                break

            case _:
                print("")
                print("OPÇÃO INVALIDA")
                os.system("pause")
                os.system("cls")

def consulta(lista):
    while True:

        while True:
            
            print("---- CONSULTA DE ANIMAIS ----")       
            print("01 - DIAGNOSTICAR O ANIMAL")
            print("02 - VERIFICAR DIAGNOSTICO DO ANIMAL")
            print("00 - VOLTAR")

            try:

                escolha = int(input("Qual opção deseja ? \n--> "))
                break

            except Exception as e:

                print(f"Impossivel concluir operação \n erro encontrado: {e}")
                os.system("pause")
                os.system("cls")
        
        match escolha:

            case 1:
                print("---- DIAGNOSTICANDO OS ANIMAIS ----")
                print("")
                print("ID\tNOME\tESPECIE")       

                cont = 1
                for animais in lista:
                    print(f"{cont}\t{animais.getNome()}\t{animais.getEspecie()}")
                    cont += 1

                print("")

                id_sel = int(input("Qual animal deseja consultar ? \n--> "))
                diag = input("informe o diagnostico do animal\n--> ")

                lista[id_sel - 1].setDiag(diag)

                print("")
                print("DIAGNOSTICO CADASTRADO COM SUCESSO")
                os.system("pause")
                os.system("cls")


            case 2:
                
                print("---- VERIFICANDO DIAGNOSTICO DO ANIMAL ----")
                print("")
                print("ID\tNOME\tESPECIE")       

                cont = 1
                for animais in lista:
                    print(f"{cont}\t{animais.getNome()}\t{animais.getEspecie()}")
                    cont += 1

                print("")

                id_sel = int(input("Qual animal deseja verificar ? \n--> "))

                print(f"O diagnostico do animal é: {lista[id_sel - 1].getDiag()}\n")
                os.system("pause")
                os.system("cls")

            case 0:
                print("")
                os.system("pause")
                os.system("cls")
                break

            case _:
                print("")
                print("OPÇÃO INVALIDA")
                os.system("pause")
                os.system("cls")