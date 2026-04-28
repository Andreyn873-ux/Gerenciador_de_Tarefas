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

    def bsucar_tarefa(self, tarefa_id):
        tarefa = self.repository.buscar_por_id(tarefa_id)

        if not tarefa:
            raise ValueError("Tarefa não encontrada")

        return tarefa
    
    def atualizar_status(self, tarefa_id, novo_status):
        status_validos = ["pendente", "concluida"]

        if novo_status not in status_validos:
            raise ValueError("Status invalido")

        self.repository.atualizar_status(tarefa_id, novo_status)

        if not atualizado:
            raise ValueError("Tarefa não encontrada")

        return True

    def deletar_tarefa(self, tarefa_id):
        self.repository.deletar(tarefa_id)

        if not deletado:
            raise ValueError("Tarefa não encontrada")

        return True
