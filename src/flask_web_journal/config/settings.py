# flask_web_journal/config/settings.py

"""Flask configuration module"""

import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_JOURNAL_DB")
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("JOURNAL_DB")
    
class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_JOURNAL_DB")