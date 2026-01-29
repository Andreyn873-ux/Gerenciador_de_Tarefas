class usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.tarefas = []


    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)