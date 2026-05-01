import click

from services.tarefas_service import TarefasService
from repositories.tarefas_repository import TarefasRepository

repository = TarefasRepository()
service = TarefasService(repository)

@click.group()
def cli():
    """Gerenciador de Tarefas CLI"""
    pass

@cli.command()
@click.argument('titulo')
def criar(titulo):
    try:
        tarefa = service.criar_tarefa(titulo)
        click.echo(f"Tarefa criada: {tarefa.id} - {tarefa.titulo}")
    except ValueError as e:
        click.echo(f"Erro: {e}")
    
@cli.command()
def listar():
    tarefa = service.listar_tarefas()
    if not tarefa:
        click.echo("Nenhuma tarefa encontrada.")
    else:
        for t in tarefa:
            click.echo(f"[{t.id}] - {t.titulo} - {t.status}")

@cli.command()
@click.argument("tarefa_id", type=int)
@click.argument("status")

def atualizar_status(tarefa_id, status):
    try:
        service.atualizar_status(tarefa_id, status)
        click.echo(f"Tarefa atualizada com sucesso!")
    except ValueError as e:
        click.echo(f"Erro: {e}")

@cli.command()
@click.argument("tarefa_id", type=int)
def deletar(tarefa_id):
    try:
        service.deletar_tarefa(tarefa_id)
        click.echo(f"Tarefa deletada com sucesso!")
    except ValueError as e:
        click.echo(f"Erro: {e}")

if __name__ == "__main__":
    cli()
