from services.tarefas_service import TarefasService


def iniciar_sistema():
    service = TarefasService()

    while True:
        print("\n === GERENCIADOR DE TAREFAS ===")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar tarefa")
        print("4 - Deletar tarefa")
        print("0 - Sair")

        try:
            opção = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido. ")
            continue 

        if opção == 1:
            titulo = input("Digite o título da tarefa: ")

            try:
                service.criar_tarefa(titulo)
                print("Tarefa criada com sucesso!")
            except ValueError as e:
                print(f" Erro: {e}")

        elif opção == 2:
            tarefas = service.listar_tarefas()

            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                for tarefa in tarefas:
                    print(f"ID: {tarefa.id} | {tarefa.titulo} | {tarefa.status}")

        elif opção == 3:
            try:
                tarefa_id = int(input("Digite o ID da tarefa: "))
                novo_status = input("Novo status (pendente/concluída): ")
                service.atualizar_tarefa(tarefa_id, novo_status)
            except ValueError:
                print("ID inválido.")

        elif opção == 4:
            try:
                tarefa_id = int(input("Digite o ID da tarefa: "))
                service.deletar_tarefa(tarefa_id)
            except ValueError:
                print("ID inválido.")

        elif opção == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção Inválida.")