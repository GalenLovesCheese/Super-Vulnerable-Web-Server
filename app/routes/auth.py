from flask import Blueprint, request, render_template, abort, redirect, url_for, session
from app.models import users
from app import logger

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def index():
    return redirect(url_for("auth.login_page"))

@auth_bp.route("/login", methods=["GET", "POST"])
def login_page():
    # Render login page and handle login submissions.
    if not session.get("session_id"): 
        if request.method == "GET":
            return render_template("login.html")

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            logger.info(f"Login attempt for username: {username}")

            for user in users:
                if user["username"] == username and user["password"] == password:
                    session_id = f"session-{user['id']}"
                    session["username"] = username
                    session["session_id"] = session_id
                    logger.info(f"Login successful for username: {username}, session ID: {session_id}")
                    return redirect(url_for("files.file_access_page"))
                    #return jsonify({"message": "Login successful", "session_id": session_id}), 200

            logger.warning(f"Invalid login attempt for username: {username}")
            abort(401, description="Invalid credentials")
    else:
        logger.info("User already logged in, redirecting to file access page.")
        return redirect(url_for("files.file_access_page"))
    

@auth_bp.route("/logout", methods=["GET"])
def logout():
    session_id = session.pop("session_id", None)  
    if session_id:
        logger.info(f"Logout successful for session ID: {session_id}")
    else:
        logger.warning("Logout attempted with no active session.")
    return redirect(url_for("auth.login_page"))