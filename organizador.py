tarefas = [] 

def mostrar_menu():
    print("\n--- ORGANIZADOR DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

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
        print("Função de remover tarefa ainda não implementada.")
    elif opcao == "4":
        print("Finalizando...")
        break
    else:
        print("Opção inválida, tente novamente.")
