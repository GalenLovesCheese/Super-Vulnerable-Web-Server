from flask import Blueprint, request, render_template, jsonify, session, redirect, url_for
from app.models import files

files_bp = Blueprint("files", __name__)

@files_bp.route("/files", methods=["GET", "POST"])
def file_access_page():
    """
    Render file access page and handle file requests.
    """
    session_id = session.get("session_id")
    print(f"Session id is: {session_id}")
    owner_id = int(session_id.split("-")[1])
    user_id = request.args.get("user_id", default=str(owner_id))

    if not session_id:
        return redirect(url_for("auth.login_page"))
    
    if request.method == "GET":
        # Allow admin to view all files
        if user_id == "3":
            accessible_files = list(files.values())
            
        else:   
            accessible_files = [file for file in files.values() if str(file["owner_id"]) == user_id]
            
        return render_template("file_access.html", files=accessible_files, owner_id=user_id)

    if request.method == "POST":
        file_id = request.form.get("file_id") 


        # No comparison for owner id of file, and logged-in owner id
        for file in files.values():
            if file["file_id"] == file_id:
                    return jsonify(file), 200
        return jsonify({"message": "File not found"}), 404
