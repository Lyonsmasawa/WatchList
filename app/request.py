from app import app
import urllib.request, json
from .models import movie
Movie = movie.Movie

#getting api key
api_key = app.config['MOVIE_API_KEY']

#getting the movie base url
base_url = app.config['MOVIE_API_BASE_URL'] #APP.CONFIG['name of object to access']

def get_movies(category):
    """Function that gets the json response to our URL request"""
    get_movies_url = base_url.format(category, api_key) #will be replace the curly braces in the movie base url with the category and the api key respectively

    with urllib.request.urlopen(get_movies_url) as url: #sends a request as url
        get_movies_data = url.read() #reads the response and stores it to the variable
        get_movies_response = json.loads(get_movies_data) #convert the json response to a python dictionary and stores it

        movie_results = None

        if get_movies_response['results']: #check if it contains results
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list) #takes in the list of movie object and returns a list of movie objects

    return movie_results

def process_results(movie_list):
    """takes in the list of movie objects and transforms them to a list of objects"""
    movie_results = [] 
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster: #some movie might not have posters which will result to errors when creating our application, so we check first then create the movie object
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
            movie_results.append(movie_object)

    return movie_results

def get_movie(id):
    get_movie_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)
        
        movie_object = None

        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            
        return movie_object