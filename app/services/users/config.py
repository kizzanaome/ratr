import os

class BaseConfig(object):
    """parent configuration class"""
    Debug = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(BaseConfig):
    """Configurations for Development."""
    Debug = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class TestingConfig(BaseConfig):
    """Configurations for Testing."""
    Debug = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1460@localhost:5432/testing_db"
    WTF_CRSF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    Debug = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
