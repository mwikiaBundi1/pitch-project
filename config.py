import os

class Config:
    SECRET_KEY =  os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:buttonupd@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photo'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME =  os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'Gone in 60 seconds'
    SENDER_EMAIL = 'Dankariuki0101@gmail.com'
class prodConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABAASE_URL')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://root:buttonupd@localhost/pitch'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://root:buttonupd@localhost/pitch'

config_options = {
    'development': DevConfig,
    'production': prodConfig,
    'test': TestConfig
}
