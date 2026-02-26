from flask import Blueprint, request, jsonify
from utils.ai import get_ai_response

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/chat", methods=["POST"])
def chat():

    data = request.json
    message = data["message"]

    reply = get_ai_response(message)

    return jsonify({"reply": reply})