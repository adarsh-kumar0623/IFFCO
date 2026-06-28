import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = "iffco_super_secret_key_2026"

    DATABASE = os.path.join(BASE_DIR, "database", "iffco.db")

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "data", "uploads")

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    SESSION_PERMANENT = False

    SESSION_TYPE = "filesystem"