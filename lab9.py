from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados temporário em memória (exemplo de recurso)
mensagens = [
    {"id": 1, "mensagem": "Hello, World!", "origem": "Flask RESTful API"}
]


# Rota GET: Retorna a lista de recursos em formato JSON
@app.route("/items", methods=["GET"])
def get_hello():
    return jsonify({"status": "success", "data": mensagens}), 200


# Rota POST: Adiciona um novo recurso (opcional para demonstrar REST)
@app.route("/api/v1/hello", methods=["POST"])
def create_hello():
    data = request.get_json()
    if not data or "mensagem" not in data:
        return jsonify({"status": "error", "message": "Campo 'mensagem' é obrigatório"}), 400

    nova_mensagem = {
        "id": len(mensagens) + 1,
        "mensagem": data["mensagem"],
        "origem": data.get("origem", "Usuário")
    }
    mensagens.append(nova_mensagem)
    return jsonify({"status": "success", "data": nova_mensagem}), 201


if __name__ == "__main__":
    app.run(debug=True)