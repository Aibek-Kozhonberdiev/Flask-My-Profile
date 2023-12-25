import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = bool(int(os.environ.get('FLASK_DEBUG', "0")))
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('FLASK_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'templates'
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
