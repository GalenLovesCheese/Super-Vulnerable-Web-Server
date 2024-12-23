from flask import Blueprint, request, render_template, jsonify, redirect, url_for, session, jsonify
from app.models import users

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login_page():
    # Render login page and handle login submissions.
    if not session.get("session_id"): 
        if request.method == "GET":
            return render_template("login.html")

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            for user in users:
                if user["username"] == username and user["password"] == password:
                    session_id = f"session-{user['id']}"
                    session["username"] = username
                    session["session_id"] = session_id
                    return redirect(url_for("files.file_access_page"))
                    #return jsonify({"message": "Login successful", "session_id": session_id}), 200

            return jsonify({"message": "Invalid credentials"}), 401
    else:
        return redirect(url_for("files.file_access_page"))
    

@auth_bp.route("/logout", methods=["GET"])
def logout():
    session.pop("session_id", None)  
    return redirect(url_for("auth.login_page"))