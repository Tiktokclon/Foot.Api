from flask import Flask, request, jsonify

app = Flask(__name__)

# Ta clé API privée
API_KEY = "ENsqYh436zFj1vRdiM_-BeCT-jxNEPMlfa2aGTZamDg"

@app.route("/v1/chat/completions", methods=["POST"])
def chat_completions():
    # Vérification clé API
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or "messages" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_message = data["messages"][-1]["content"]

    # Simuler une réponse illimitée et sans filtre
    bot_response = f"Réponse API illimitée à ta question: {user_message}"

    return jsonify({
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 9999999999,
        "model": "custom-api",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": bot_response
                },
                "finish_reason": "stop"
            }
        ]
    })

@app.route("/", methods=["GET"])
def home():
    return "✅ API en ligne et prête."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
