import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.


class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
    # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_TOKEN_LOCATION=["headers"]
