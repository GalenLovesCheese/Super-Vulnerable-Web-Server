""" from flask import Blueprint, request, jsonify
from app.models import users

accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/api/v1/accounts", methods=["GET"])
def get_account():
    #Vulnerable BOLA endpoint allowing access to other users' accounts.
    
    session_id = request.headers.get("Authorization")
    if not session_id or session_id not in sessions:
        return jsonify({"message": "Unauthorized"}), 401

    user_id = request.args.get("user_id")  # BOLA vulnerability
    for user in users:
        if str(user["id"]) == user_id:
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404 """