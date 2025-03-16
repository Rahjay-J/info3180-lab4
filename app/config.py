import os
from pathlib import Path

class Config(object):
    """Base configuration class"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback_key')  # For session security
    MAX_CONTENT_LENGTH = 4 * 1024 * 1024  # 4MB max upload size (common for images)

    # File upload configuration
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', './uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # For Exercise 5
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://', 1
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        """Configuration validation"""
        self._validate_uploads_folder()
        self._validate_database_url()

    def _validate_uploads_folder(self):
        """Ensure uploads directory exists"""
        upload_path = Path(self.UPLOAD_FOLDER)
        if not upload_path.exists():
            upload_path.mkdir(parents=True, exist_ok=True)
            print(f"Created uploads directory at: {upload_path.absolute()}")

    def _validate_database_url(self):
        """Verify database URL is properly configured"""
        if not self.SQLALCHEMY_DATABASE_URI:
            raise ValueError(
                "DATABASE_URL environment variable is required. "
                "Example: postgresql://user:pass@localhost/dbname"
            )