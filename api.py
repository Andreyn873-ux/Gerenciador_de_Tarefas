from flask import Flask
from Controllers.controllers import tarefas_bp, init_routes
from database import criar_tabelas
from repositories.tarefas_repository import TarefasRepository
from services.tarefas_service import TarefasService

app = Flask(__name__)

criar_tabelas()

repository = TarefasRepository()
service = TarefasService(repository)

init_routes(service)
app.register_blueprint(tarefas_bp)

@app.route("/")
def home():
    return "API funcionando!"

if __name__ == "__main__":
    app.run(debug=True)
