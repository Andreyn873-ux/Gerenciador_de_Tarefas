from database import criar_tabelas

criar_tabelas()
print("Banco de dados criado com sucesso!")

from models.usuario import usuario
from models.tarefa import Tarefa

usuario1 = usuario('Andrey', 'andrey@gmail.com')

tarefa1 = Tarefa('Estudar POO')
tarefa2 = Tarefa('Praticar SQL')
usuario1.adicionar_tarefa(tarefa1)
usuario1.adicionar_tarefa(tarefa2)


print(usuario1.nome)

for tarefa in usuario1.tarefas:
    print("-", tarefa.titulo)
