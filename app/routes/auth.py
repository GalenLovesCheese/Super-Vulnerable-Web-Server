from flask import Blueprint, request, render_template, jsonify

auth_bp = Blueprint("auth", __name__)

# Mock session store
sessions = {}

# Mock user database
users = [
    {"id": 1, "username": "user1", "password": "pass1"},
    {"id": 2, "username": "user2", "password": "pass2"},
    {"id": 3, "username": "admin", "password": "adminpass"},
]

@auth_bp.route("/login", methods=["GET", "POST"])
def login_page():
    
    # Render login page and handle login submissions.
    
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        for user in users:
            if user["username"] == username and user["password"] == password:
                session_id = f"session-{user['id']}"
                sessions[session_id] = user
                #return jsonify({"message": "Login successful", "session_id": session_id}), 200
                return render_template("file_access.html")

        return jsonify({"message": "Invalid credentials"}), 401