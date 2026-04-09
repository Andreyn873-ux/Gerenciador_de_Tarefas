from services.tarefas_service import TarefasService
from repositories.tarefas_repository import TarefasRepository
from utils.logger import configurar_logger
from cli import iniciar_sistema
from database import criar_tabelas

if __name__ == "__main__":
    configurar_logger()
    criar_tabelas()

    repository = TarefasRepository()
    service = TarefasService(repository)

    iniciar_sistema(service)
    
