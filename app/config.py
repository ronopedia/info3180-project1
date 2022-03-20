import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    UPLOAD_FOLDER = './uploads'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://uytclroqwecesw:18b45ba2ce46ba1505262384edca29be0f866d89b75b8d79254fcc06a55159b1@ec2-3-222-204-187.compute-1.amazonaws.com:5432/d6sr094f5gnbec'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False