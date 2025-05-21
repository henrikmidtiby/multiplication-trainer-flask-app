"""Flask configuration."""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base config."""

    SECRET_KEY = os.urandom(20)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://multtrainer:devpassword@0.0.0.0:5432/multiplication-trainer"
    )
    FLASK_ENV = "development"
    DEBUG = True


class ProdConfig(Config):
    # Access value from the .env file
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class DevConfig(Config):
    SECRET_KEY = "a"
    pass
