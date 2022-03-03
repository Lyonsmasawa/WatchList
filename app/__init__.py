import imp
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos', IMAGES) #UPLOAD SET DEFINES WHAT WE ARE UPLOADING, we pass in a name and the type of file we want to upload which is an image
login_manager = LoginManager() #create an instance 
login_manager.session_protection = 'strong' #provides diff security levels and by using strong it will minitor changes in the user header and log the user out
login_manager.login_view = 'auth_login' #add the blueprint name as the login endpoint as it is located inside a blueprint

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])

    configure_uploads(app, photos)

    bootstrap.init_app(app)
    db.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    configure_request(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    return app