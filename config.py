
# POSTGRE_URI = 'postgresql://helen:123@127.0.0.1:5432/flask_test'
# SALT = 'my_sJHLHLHKLаваыпuper_s!alt_#4$434'
# SQLALCHEMY_TRACK_MODIFICATIONS = False

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = '**************'
    SECRET_KEY = '***********'
    SQLALCHEMY_DATABASE_URI = 'postgresql://helen:123@127.0.0.1:5432/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '********************************'


class ProductionConfig(Config):
    DEBUG = False


class DevelopConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True

