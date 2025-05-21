from flask import Flask, render_template
from flask_migrate import Migrate
import logging
from app.models import db


migrate = Migrate()


def create_app(configname):
    app = Flask(__name__)
    app.config.from_object(configname)
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app import views  # noqa: F401

    return app
