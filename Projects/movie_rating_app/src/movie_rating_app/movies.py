
class Movies:
    def __init__(self):
        self.movie_collection =[]

    def add_movie(self, movie):
        self.movie_collection.append(movie)

    def get_number_of_movies(self):
        return len(self.movie_collection)

