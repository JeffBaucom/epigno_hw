import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret-secret'
    REDIS_URL = 'redis://redis:6379/0'
    QUEUES = ['default']
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/epigno_dev"
    SQLALCHEMY_BINDS = {
        'hospital': 'sqlite:///hospital.db'
    }
