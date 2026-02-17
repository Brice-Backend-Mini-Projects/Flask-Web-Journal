# flask_web_journal/config/settings.py

"""Flask configuration module"""

import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    
class ProductionConfig(BaseConfig):
    DEBUG = False
    
class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = False
    DATABASE_URL = "sqlite:///:memory:"

config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig,
    'testing' : TestingConfig,
    'default' : DevelopmentConfig,
}