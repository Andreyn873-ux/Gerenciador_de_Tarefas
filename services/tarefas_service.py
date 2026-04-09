from models.tarefa import Tarefa

class TarefasService:
    def __init__(self, repository):
        self.repository = repository


    def criar_tarefa(self, titulo, usuario_id=None):
        if not titulo:
            raise ValueError("O título da tarefa é obrigatório.")
        
        tarefa = Tarefa(
            titulo = titulo,
            status = "pendente",
            usuario_id = usuario_id
        )

        self.repository.salvar(tarefa)
        return tarefa
    
    def listar_tarefas(self):
        return self.repository.listar()
    
    def atualizar_status(self, tarefa_id, novo_status):
        self.repository.atualizar_status(tarefa_id, novo_status)

    def atualizar_status_tarefa(self, tarefa_id, novo_status):
        self.atualizar_status(tarefa_id, novo_status)

    def deletar_tarefa(self, tarefa_id):
        self.repository.deletar(tarefa_id)
