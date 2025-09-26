# possível nova funcionalidade: marcar tarefa como concluida

tarefas = [] 

def mostrar_menu():
    print("\n--- ORGANIZADOR DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Editar tarefa")
    print("5 - Marcar tarefa como concluída")
    print("6 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append({"descricao": tarefa, "concluida": False})
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de tarefas:")
            for i, t in enumerate(tarefas, start=1):
                status = "✅ Concluída" if t["concluida"] else "⏳ Pendente"
                print(f"{i}. {t['descricao']} - {status}")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t['descricao']}")
            indice = int(input("Digite o número da tarefa que deseja remover: "))
            if 1 <= indice <= len(tarefas):
                removida = tarefas.pop(indice - 1)
                print(f"Tarefa '{removida['descricao']}' removida com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == "4":
        if len(tarefas) == 0:
            print("Não há tarefas para editar.")
        else:
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t['descricao']}")
            indice = int(input("Digite o número da tarefa que deseja editar: "))
            if 1 <= indice <= len(tarefas):
                nova_tarefa = input("Digite a nova descrição da tarefa: ")
                tarefas[indice - 1]["descricao"] = nova_tarefa
                print("Tarefa atualizada com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == "5":
        if len(tarefas) == 0:
            print("Não há tarefas para concluir.")
        else:
            for i, t in enumerate(tarefas, start=1):
                status = "✅" if t["concluida"] else "⏳"
                print(f"{i}. {t['descricao']} - {status}")
            indice = int(input("Digite o número da tarefa concluída: "))
            if 1 <= indice <= len(tarefas):
                tarefas[indice - 1]["concluida"] = True
                print("Tarefa marcada como concluída!")
            else:
                print("Número inválido.")

    elif opcao == "6":
        print("Finalizando...")
        break

    else:
        print("Opção inválida, tente novamente.")
