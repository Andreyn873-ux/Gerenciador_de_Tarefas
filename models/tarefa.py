class Tarefa:
    def __init__(self, titulo, status='pendente', usuario_id=None):
        self.titulo = titulo
        self.status = status
        self.usuario_id = usuario_id
    
    def concluir(self):
        self.status = 'concluida'