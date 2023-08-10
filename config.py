import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_default_key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://mongo:27017/santex'


class DevelopmentConfig(Config):
    DEBUG = True
    # Add any other development-specific configurations here.


class TestingConfig(Config):
    TESTING = True
    MONGO_URI = 'mongodb://mongo:27017/test_db'
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
