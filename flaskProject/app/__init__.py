from flask import Flask

from app.models import Book, User
from app.extension import db, cors
from app.config import Config
from app.views import bp as api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    cors.init_app(app)

    app.register_blueprint(api_bp)

    @app.cli.command()
    def create():
        db.drop_all()
        db.create_all()
        Book.init_db()
        User.init_db()

    return app
