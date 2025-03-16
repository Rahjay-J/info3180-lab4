import os
from pathlib import Path

class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback_key')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', './uploads')
    
    # Database configuration with validation
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable is missing")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False