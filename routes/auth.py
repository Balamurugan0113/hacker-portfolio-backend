from flask import Blueprint, request, jsonify
from utils.jwt_auth import generate_token

auth_bp = Blueprint("auth", __name__)

ADMIN_USER = "admin"
ADMIN_PASS = "admin123"

@auth_bp.route("/login", methods=["POST"])
def login():

    username = request.json["username"]
    password = request.json["password"]

    if username == ADMIN_USER and password == ADMIN_PASS:

        token = generate_token(username)

        return jsonify({
            "status":"success",
            "token": token
        })

    return jsonify({"status":"fail"}), 401