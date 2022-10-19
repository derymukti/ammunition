"""System Module"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base Config"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY','xlOk-911=1daACXXX')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class ProductionConfig(Config):
    """Production"""
    DEBUG = False


class StagingConfig(Config):
    """Staging"""
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """Development"""
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """Testing"""
    TESTING = True