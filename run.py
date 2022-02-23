from distutils.log import debug
from app import app #import the app instance

if __name__ == '__main__': 
    app.run(debug=True)