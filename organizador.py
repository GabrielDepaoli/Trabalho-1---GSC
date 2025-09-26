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
        print("Função de adicionar tarefa ainda não implementada.")
    elif opcao == "2":
        print("Função de ver tarefas ainda não implementada.")
    elif opcao == "3":
        print("Função de remover tarefa ainda não implementada.")
    elif opcao == "4":
        print("Finalizando...")
        break
    else:
        print("Opção inválida, tente novamente.")
