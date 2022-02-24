from flask import render_template #takes in the name of a template file as an argument and automatically searches for the template file
#in our app/templates/subdirectory and loads it 
from app import app
from .request import get_movies #we import app instance from app folder

@app.route('/') #route decorator
def index():  #view function

    """ View root page """
    #getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    title = 'Home - Welcome to The Best Movie Review Website Online' #variable
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movies, now = now_showing_movie) #pass the variable as an argument

@app.route('/movie/<movie_id>')
def movie(movie_id):
    introduction = "Hello movie code: "
    return render_template('movie.html', id = movie_id, intro = introduction)