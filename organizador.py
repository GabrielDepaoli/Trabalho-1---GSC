tarefas = [] 

def mostrar_menu():
    print("\n--- ORGANIZADOR DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Editar tarefa")
    print("5 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de tarefas:")
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t}")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            print("\nTarefas:")
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t}")
            indice = int(input("Digite o número da tarefa que deseja remover: "))
            if 1 <= indice <= len(tarefas):
                removida = tarefas.pop(indice - 1)
                print(f"Tarefa '{removida}' removida com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == "4":
        if len(tarefas) == 0:
            print("Não há tarefas para editar.")
        else:
            print("\nTarefas:")
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t}")
            indice = int(input("Digite o número da tarefa que deseja editar: "))
            if 1 <= indice <= len(tarefas):
                nova_tarefa = input("Digite a nova descrição da tarefa: ")
                tarefas[indice - 1] = nova_tarefa
                print("Tarefa atualizada com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == "5":
        print("Finalizando...")
        break

    else:
        print("Opção inválida, tente novamente.")
