from flask import Flask

from app.config import Config
from app.routes.pages import bp as bp_pages


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app


def register_bp(app):
    app.register_blueprint(bp_pages)


def main():
    app = create_app()
    register_bp(app)
    app.run(host="0.0.0.0", port=app.config['PORT'])
