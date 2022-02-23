import unittest
import movie
Movie = movie.Movie

class TestMovie(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie)) #isinstance checks if 

    def test__init__(self):
        self.assertEqual(self.new_movie.id, 1234)
        self.assertEqual(self.new_movie.title, 'Python Must Be Crazy')
        self.assertEqual(self.new_movie.overview, 'A thrilling new Python Series')
        self.assertEqual(self.new_movie.poster, 'https://image.tmdb.org/t/p/w500/' + 'khsjha27hbs')
        self.assertEqual(self.new_movie.vote_average, 8.5)
        self.assertEqual(self.new_movie.vote_count, 129993)

if __name__ == '__main__':
    unittest.main()