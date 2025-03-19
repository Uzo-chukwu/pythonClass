from src.movie_rating_app.movies import Movies
from src.movie_rating_app.user import User
import unittest

class UserTestCase(unittest.TestCase):

    def test_that_user_class_exists(self):
        user = User("Uzo")


    def test_that_user_can_add_movie(self):
        user = User("Uzo")
        movies = Movies()
        user.add_movie("Suits",movies)
        self.assertEqual(1,movies.get_number_of_movies())

    def test_that_user_can_add_multiple_movies(self):
        user = User("Uzo")
        movies = Movies()
        user.add_movie("Suits",movies)
        user.add_movie("Lincoln lawyer",movies)
        self.assertEqual(2,movies.get_number_of_movies())

    def test_that_when_user_tries_to_add_an_already_existing_movie_raises_value_error(self):
        user = User("Uzo")
        movies = Movies()
        user.add_movie("Suits",movies)
        self.assertRaises(ValueError,user.add_movie,"Suits",movies)

    def test_that_user_can_rate_movie(self):
        user = User("Uzo")
        movies = Movies()
        user.add_movie("Lincoln lawyer",movies)
        user.rate_movie(2,"Lincoln lawyer",movies)
        for movie in movies.movie_collection: self.assertEqual(movie.get_rating(),[2])

    def test_that_user_trying_to_rate_a_nonExisting_movie_raises_value_error(self):
        user = User("Uzo")
        movies = Movies()
        user.add_movie("Lincoln lawyer",movies)
        self.assertRaises(ValueError,user.rate_movie,2,"suits",movies)

    def test_that_user_can_get_average_rating(self):
        user = User("Uzo")
        movies = Movies()
        user.add_movie("Lincoln lawyer",movies)
        user.rate_movie(2,"Lincoln lawyer",movies)
        user.rate_movie(3,"Lincoln lawyer",movies)
        user.rate_movie(4,"Lincoln lawyer",movies)
        average_rating = user.get_average_movie_rating("Lincoln lawyer",movies)
        self.assertEqual(average_rating,3)

    def test_that_user_attampting_to_get_average_rating_for_a_non_existing_movie_raises_value_error(self):
        user = User("Uzo")
        movies = Movies()
        user.add_movie("Lincoln lawyer",movies)
        user.rate_movie(2,"Lincoln lawyer",movies)
        self.assertRaises(ValueError,user.get_average_movie_rating,"incoln lawyer",movies)



    def test_that_when_user_tries_to_get_total_average_movie_rating_raises_value_error_when_no_movie_is_rated_yet(self):
        user = User("Uzo")
        movies = Movies()
        user.add_movie("Lincoln lawyer",movies)
        self.assertRaises(ValueError,user.get_total_average_rating,movies)






if __name__ == '__main__':
    unittest.main()
