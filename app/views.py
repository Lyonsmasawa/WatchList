from flask import render_template #takes in the name of a template file as an argument and automatically searches for the template file
#in our app/templates/subdirectory and loads it 
from app import app
from .request import get_movies, get_movie #we import app instance from app folder

@app.route('/') #route decorator
def index():  #view function

    """ View root page """
    #getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    title = 'Home - Welcome to The Best Movie Review Website Online' #variable
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movies, now = now_showing_movie) #pass the variable as an argument

@app.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html',title = title,movie = movie)