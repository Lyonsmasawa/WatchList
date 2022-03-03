import os

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:passdb@localhost/watchlist'
    UPLOADED_FILES_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com' #smtp server
    MAIL_PORT = 587 #gmail smtp server port
    MAIL_USE_TLS = True #enables a transport layer security to secure emails when sending
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") #these are yours
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development' :DevConfig,
    'production' :ProdConfig
}