def iniciar_sistema(service):
    while True:
        print("\n === GERENCIADOR DE TAREFAS ===")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar tarefa")
        print("4 - Deletar tarefa")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            print("Digite um numero valido.")
            continue

        if opcao == 1:
            titulo = input("Digite o titulo da tarefa: ")

            try:
                service.criar_tarefa(titulo)
                print("Tarefa criada com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == 2:
            tarefas = service.listar_tarefas()

            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                for tarefa in tarefas:
                    print(f"ID: {tarefa.id} | {tarefa.titulo} | {tarefa.status}")

        elif opcao == 3:
            try:
                tarefa_id = int(input("Digite o ID da tarefa: "))
                novo_status = input("Novo status (pendente/concluida): ").strip().lower()

                if novo_status in ["concluida", "concluída"]:
                    novo_status = "concluida"

                status_validos = ["pendente", "concluida"]
                if novo_status not in status_validos:
                    print("Status invalido!")
                    continue

                service.atualizar_status(tarefa_id, novo_status)
                print("Status atualizado com sucesso!")

            except ValueError:
                print("ID invalido.")

        elif opcao == 4:
            try:
                tarefa_id = int(input("Digite o ID da tarefa: "))
                service.deletar_tarefa(tarefa_id)
                print("Tarefa deletada com sucesso!")
            except ValueError:
                print("ID invalido.")

        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida.")
