import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Подключается БД SQLite
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:'
        )
    # Задаётся конкретное значение для конфигурационного ключа
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS', ''
        ).lower() in ['true', 'yes', '1']
    SECRET_KEY = os.getenv('SECRET_KEY', '')
