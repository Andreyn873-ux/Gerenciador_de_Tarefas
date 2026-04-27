from flask import Flask, request, jsonify
from services.tarefas_service import TarefasService
from repositories.tarefas_repository import TarefasRepository

app = Flask(__name__)

repository = TarefasRepository()
service = TarefasService(repository)

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    tarefas = service.listar_tarefas()
    resultado = []
    for t in tarefas:
        resultado.append({
            "id": t.id,
            "titulo": t.titulo,
            "Status": t.status
        })

    return jsonify(resultado)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    data = request.json
    titulo = data.get("titulo")

    try:
        tarefa = service.criar_tarefa(titulo)

        return jsonify({
            "id": tarefa.id,
            "titulo": tarefa.titulo,
            "status": tarefa.status
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def home():
    return "API funcionando!"

@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefas(tarefa_id):
    data = request.json or {}
    novo_status = data.get("status")

    status_validos = ["pendente", "concluída"]

    if novo_status not in status_validos:
        return jsonify({"error": "Status inválidos"}), 400
    try:
        service.atualizar_status(tarefa_id, novo_status)
        return jsonify({"mensagem": "Tarefa atualizada com sucesso"})
    except ValueError as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def deletar_tarefa(tarefa_id):
    try:
        service.deletar_tarefa(tarefa_id)
        return jsonify({"mensagem": "Tarefa deletada com sucesso"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500