nome = [1,2]
descrição = [1,2]
data = [1,2]

Tarefas = {"nome": nome, "descrição": descrição, "data": data}




print("\t \t Lista de Tarefas: \n")

posição = 1

if len(Tarefas) == 0:
    print("\t NENHUMA tarefa encontrada...")
    
else:
    for chave, valor in Tarefas.items():
        print(f"{chave}: ")
        for item in valor:
            print(f"{posição}º - {item} \n")
            posição += 1

    
    print(" ")
    
