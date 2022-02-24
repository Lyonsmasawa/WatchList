from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import DevConfig

# initializing the application
app = Flask(__name__, instance_relative_config = True)

#setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing bootstrap
bootstrap = Bootstrap(app)

from app import views