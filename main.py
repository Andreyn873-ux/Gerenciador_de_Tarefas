from database import criar_tabelas
from services.tarefas_service import TarefasService
from models.usuario import Usuario
from models.tarefa import Tarefa


criar_tabelas()
print("Banco de dados criado com sucesso!")


usuario1 = Usuario('Andrey', 'andrey@gmail.com')

tarefa1 = Tarefa('Estudar POO')
tarefa2 = Tarefa('Praticar SQL')

usuario1.adicionar_tarefa(tarefa1)
usuario1.adicionar_tarefa(tarefa2)

print(usuario1.nome)

for tarefa in usuario1.tarefas:
    print("-", tarefa.titulo)


service = TarefasService()
tarefa = service.criar_tarefa("Estudar camada service")

print("Tarefa criada:", tarefa.titulo)



criar_tabelas()
print("Banco de dados criado com sucesso!")

usuario1 = Usuario('Andrey', 'andrey@gmail.com')

tarefa1 = Tarefa('Estudar POO')
tarefa2 = Tarefa('Praticar SQL')
usuario1.adicionar_tarefa(tarefa1)
usuario1.adicionar_tarefa(tarefa2)


print(usuario1.nome)

for tarefa in usuario1.tarefas:
    print("-", tarefa.titulo)

service = TarefasService()

tarefa = service.criar_tarefa("Estudar camada service")
print("Tarefa criada:", tarefa.titulo)

tarefas = service.listar_tarefas()
print('\n lista de tarefas:')

for tarefa in tarefas:
    print(f' - {tarefa.titulo} | Status: {tarefa.status}')

service.atualizar_status(1, 'concluída')
print("Status da tarefa atualizado!")

tarefas = service.listar_tarefas()

for tarefa in tarefas:
    print(f"ID: {tarefa.id}, Título: {tarefa.titulo}, Status: {tarefa.status}")

service.deletar_tarefa(1)
print("\n   🗑️ Tarefa deldetada!\n")

for tarefa in tarefas:
    print(tarefa.id, tarefa.titulo, tarefa.status)