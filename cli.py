import click

from database import criar_tabelas
from repositories.tarefas_repository import TarefasRepository
from services.tarefas_service import TarefasService

criar_tabelas()

repository = TarefasRepository()
service = TarefasService(repository)

@click.group()
def cli():
    """Gerenciador de Tarefas CLI"""
    return

@cli.command()
@click.argument('titulo')
def criar(titulo):
    try:
        tarefa = service.criar_tarefa(titulo)
        click.echo(f"Tarefa criada: {tarefa.id} - {tarefa.titulo}")
    except ValueError as e:
        click.echo(click.style(f"Erro: {e}", fg="red"))
    
@cli.command()
def listar():
    tarefas = service.listar_tarefas()
    if not tarefas:
        click.echo("Nenhuma tarefa encontrada.")
    else:
        for t in tarefas:
            click.echo(f"[{t.id}] - {t.titulo} - {t.status}")

@cli.command()
@click.argument("tarefa_id", type=int)
def buscar(tarefa_id):
    try:
        tarefa = service.buscar_tarefa(tarefa_id)
        click.echo(f"[{tarefa.id}] - {tarefa.titulo} - {tarefa.status}")
    except ValueError as e:
        click.echo(click.style(f"Erro: {e}", fg="red"))

@cli.command(name="atualizar-status")
@click.argument("tarefa_id", type=int)
@click.argument("status")
def atualizar_status(tarefa_id, status):
    try:
        service.atualizar_status(tarefa_id, status)
        click.echo("Tarefa atualizada com sucesso!")
    except ValueError as e:
        click.echo(click.style(f"Erro: {e}", fg="red"))

@cli.command()
@click.argument("tarefa_id", type=int)
def deletar(tarefa_id):
    try:
        service.deletar_tarefa(tarefa_id)
        click.echo("Tarefa deletada com sucesso!")
    except ValueError as e:
        click.echo(click.style(f"Erro: {e}", fg="red"))

if __name__ == "__main__":
    cli()
