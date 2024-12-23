from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("static/config.py")

    from .routes.auth import auth_bp
    from .routes.files import files_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(files_bp)

    return app