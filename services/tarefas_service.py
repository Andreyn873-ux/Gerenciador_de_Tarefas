from models.tarefa import Tarefa
from database import conectar

class TarefasService:
    def criar_tarefa(self, titulo, usuario_id=None):
        if not titulo:
            raise ValueError("O título da tarefa é obrigatório.")
        
        tarefa = Tarefa(titulo=titulo, usuario_id=usuario_id)
        self.salvar_no_banco(tarefa)
        return tarefa
    
    def salvar_no_banco(self, tarefa):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(""" 
            INSERT INTO tarefas (titulo, status, usuario_id)
            VALUES (?, ?, ?)
        """, (tarefa.titulo, tarefa.status, tarefa.usuario_id))

        conn.commit()
        conn.close()

    def listar_tarefas(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id, titulo, status, usuario_id FROM tarefas')
        registros = cursor.fetchall()
        conn.close()
        tarefas = []
        for registro in registros:
            tarefa = Tarefa(
                titulo=registro[1],
                status=registro[2],
                usuario_id=registro[3],
            )
            tarefa.id = registro[0]
            tarefas.append(tarefa)
        return tarefas

    def atualizar_status(self, tarefa_id, novo_status):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tarefas
            SET status = ?
            WHERE id = ?
        """, (novo_status, tarefa_id))
        conn.commit()
        conn.close()

    def deletar_tarefa(self, tarefa_id):
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            DELETE FROM tarefas
            WHERE id = ?
        """, (tarefa_id,))
        conn.commit()
        conn.close()
