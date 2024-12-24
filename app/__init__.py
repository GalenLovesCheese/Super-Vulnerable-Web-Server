from flask import Flask
from app.logging_config import configure_logger

# Intitialising logger
logger = configure_logger()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("static/config.py")

    from .routes.auth import auth_bp
    from .routes.files import files_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(files_bp)

    logger.info("Server has started")

    return app