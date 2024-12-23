from flask import Blueprint, request, render_template, jsonify

files_bp = Blueprint("files", __name__)

# Mock file database
files = {
    1: {"file_id": "123.pdf", "owner_id": 1, "content": "File 123 owned by User 1"},
    2: {"file_id": "456.pdf", "owner_id": 2, "content": "File 456 owned by User 2"},
}

# Mock session store (shared with auth)
sessions = {}

@files_bp.route("/files", methods=["GET", "POST"])
def file_access_page():
    """
    Render file access page and handle file requests.
    """
    if request.method == "GET":
        return render_template("file_access.html", files=files.values())

    if request.method == "POST":
        session_id = request.form.get("session_id")
        file_id = request.form.get("file_id")

        if not session_id or session_id not in sessions:
            return jsonify({"message": "Unauthorized"}), 401

        for file in files.values():
            if file["file_id"] == file_id:
                return jsonify(file), 200

        return jsonify({"message": "File not found"}), 404
