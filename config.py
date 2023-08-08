import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_default_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    # Add any other development-specific configurations here.

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    # Add any other testing-specific configurations here.

class ProductionConfig(Config):
    # Production-specific configurations, possibly more security, logging, etc.
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
