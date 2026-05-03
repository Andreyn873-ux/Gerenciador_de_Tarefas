from utils.logger import configurar_logger
from cli import cli
from database import criar_tabelas

if __name__ == "__main__":
    configurar_logger()
    criar_tabelas()
    cli()