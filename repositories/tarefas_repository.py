from database import conectar
from models.tarefa import Tarefa


class TarefasRepository:

    def salvar(self, tarefa):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tarefas (titulo, status, usuario_id)
            VALUES (?, ?, ?)
        """, (tarefa.titulo, tarefa.status, tarefa.usuario_id))
        
        tarefa_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return tarefa_id
    
    def listar(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id, titulo, status, usuario_id FROM tarefas")
        registros = cursor.fetchall()

        conn.close()

        tarefas = []

        for registro in registros:
            tarefa = Tarefa(
                titulo=registro[1],
                status=registro[2],
                usuario_id=registro[3]
            )

            tarefa.id = registro[0]
            tarefas.append(tarefa)

        return tarefas

    def buscar_por_id(self, tarefa_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, titulo, status, usuario_id FROM tarefas WHERE id = ?
        """, (tarefa_id,))

        registro = cursor.fetchone()
        conn.close()

        if not registro:
            return None

        tarefa = Tarefa(
            titulo=registro[1],
            status=registro[2],
            usuario_id=registro[3],
        )

        tarefa.id = registro[0]

        return tarefa

    def atualizar_status(self, tarefa_id, novo_status):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tarefas
            SET status = ?
            WHERE id = ?
        """, (novo_status, tarefa_id))

        atualizado = cursor.rowcount

        conn.commit()
        conn.close()

        return atualizado > 0

    def deletar(self, tarefa_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM tarefas
            WHERE id = ?
        """, (tarefa_id,))

        deletado = cursor.rowcount

        conn.commit()
        conn.close()

        return deletado > 0
