from src.movie_rating_app.movie import Movie
from src.movie_rating_app.movies import Movies


class User:
    def __init__(self, user_name ):
        self.userName = user_name

    def add_movie(self, movie_name, movies:Movies):
        for movie in movies.movie_collection:
            if movie.get_title() == movie_name:
                raise ValueError(f"Movie {movie.get_title()} already exists")
        movie_name = Movie(movie_name)
        movies.add_movie(movie_name)

    def rate_movie(self, rating, movie_name, movies:Movies):
        for movie in movies.movie_collection:
            if isinstance(movie,Movie) and movie.get_title() == movie_name: movie.rate_movie(rating)
            else: raise ValueError('Movie name not found.')

    def get_average_movie_rating(self, movie_name, movies:Movies):
        for movie in movies.movie_collection:
            if isinstance(movie,Movie) and movie.get_title() == movie_name: return movie.get_average_rating()
            else: raise ValueError('Movie name not found.')

    def get_total_average_rating(self, movies:Movies):
        total = 0
        if len(movies.movie_collection) == 0:
            raise ValueError('No movies found.')
        for movie in movies.movie_collection:2222222222222222222222222222222222222222222222222222222222222222222222222222225545
            if isinstance(movie,Movie): total += movie.get_average_rating()
        return total/len(movies.movie_collection)


