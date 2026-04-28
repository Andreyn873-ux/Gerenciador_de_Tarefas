from flask import Blueprint, request, jsonify

tarefas_bp = Blueprint("tarefas", __name__)


def response_success(data=None, message=None, status_code=200):
    return jsonify({
        "status": "success",
        "data": data,
        "message": message
    }), status_code


def response_error(message, status_code):
    return jsonify({
        "status": "error",
        "message": message
    }), status_code


def init_routes(service):

    @tarefas_bp.route("/tarefas", methods=["GET"])
    def listar():
        tarefas = service.listar_tarefas()

        data = [{
            "id": t.id,
            "titulo": t.titulo,
            "status": t.status
        } for t in tarefas]

        return response_success(data)

    @tarefas_bp.route("/tarefas/<int:tarefa_id>", methods=["GET"])
    def buscar(tarefa_id):
        try:
            tarefa = service.buscar_tarefa(tarefa_id)

            return response_success({
                "id": tarefa.id,
                "titulo": tarefa.titulo,
                "status": tarefa.status
            })

        except ValueError as e:
            return response_error(str(e), 404)

    @tarefas_bp.route("/tarefas", methods=["POST"])
    def criar():
        data = request.json or {}

        if "titulo" not in data:
            return response_error("Campo 'titulo' é obrigatório", 400)

        try:
            tarefa = service.criar_tarefa(data["titulo"])

            return response_success({
                "id": tarefa.id,
                "titulo": tarefa.titulo,
                "status": tarefa.status
            }, "Tarefa criada com sucesso", 201)

        except ValueError as e:
            return response_error(str(e), 400)

    @tarefas_bp.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
    def atualizar(tarefa_id):
        data = request.json or {}

        if "status" not in data:
            return response_error("Campo 'status' é obrigatório", 400)

        try:
            service.atualizar_status(tarefa_id, data["status"])

            return response_success(
                message="Tarefa atualizada com sucesso"
            )

        except ValueError as e:
            return response_error(str(e), 400)

    @tarefas_bp.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
    def deletar(tarefa_id):
        try:
            service.deletar_tarefa(tarefa_id)

            return response_success(
                message="Tarefa deletada com sucesso"
            )

        except ValueError as e:
            return response_error(str(e), 404)