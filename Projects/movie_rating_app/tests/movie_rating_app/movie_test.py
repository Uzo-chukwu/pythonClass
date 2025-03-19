import unittest


from src.movie_rating_app.movie import Movie


class MovieTestCase(unittest.TestCase):

    def test_that_new_movie_is_created(self):
        movie_name = "Lincoln Lawyer"
        movie = Movie(movie_name)
        self.assertIsNotNone(movie)

    def test_that_movie_can_be_rated(self):
        movie_name = "Lincoln Lawyer"
        movie = Movie(movie_name)
        movie.rate_movie(4)
        self.assertEqual(movie.get_rating(),[4])

    def test_that_wrong_movie_rating_throws_exception(self):
        movie_name = "Lincoln Lawyer"
        movie = Movie(movie_name)
        self.assertRaises(TypeError, movie.rate_movie, 8)

    def test_that_movie_can_be_rated_with_different_rating(self):
        movie_name = "Lincoln Lawyer"
        movie = Movie(movie_name)
        movie.rate_movie(4)
        movie.rate_movie(5)
        movie.rate_movie(3)
        movie.rate_movie(2)
        self.assertEqual(movie.get_rating(), [4,5,3,2])

    def test_that_average_movie_rating_can_be_gotten(self):
        movie_name = "Lincoln Lawyer"
        movie = Movie(movie_name)
        movie.rate_movie(4)
        movie.rate_movie(5)
        movie.rate_movie(3)
        movie.rate_movie(2)
        average_rating = movie.get_average_rating()
        self.assertEqual(average_rating, 3.5)

    def test_that_get_title_works_as_expected(self):
        movie_name = "Lincoln Lawyer"
        movie = Movie(movie_name)
        self.assertEqual(movie.get_title(), "Lincoln Lawyer")



if __name__ == '__main__':
    unittest.main()
