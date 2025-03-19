import unittest

from src.movie_rating_app.movies import Movies


class MoviePortalTestCase(unittest.TestCase):
    def setUp(self):
        movies = Movies()

    def test_that_movie_portal_class_exists(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
