from flask import Blueprint, request, jsonify
from utils.jwt_auth import verify_token

secure_admin_bp = Blueprint("secure_admin", __name__)

@secure_admin_bp.route("/secure-admin")

def secure_admin():

    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error":"Unauthorized"}), 401

    decoded = verify_token(token)

    if not decoded:
        return jsonify({"error":"Invalid Token"}), 401

    return jsonify({
        "status":"Access Granted",
        "user": decoded["username"]
    })