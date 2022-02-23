from email import message
from operator import imod
from flask import render_template #takes in the name of a template file as an argument and automatically searches for the template file
#in our app/templates/subdirectory and loads it 
from app import app #we import app instance from app folder

@app.route('/') #route decorator
def index():  #view function

    """ View root page """
    message = 'Hello World' #variable
    return render_template('index.html', message = message) #pass the variable as an argument

@app.route('/movie/<movie_id>')
def movie(movie_id):
    return render_template('movie.html', id = movie_id)