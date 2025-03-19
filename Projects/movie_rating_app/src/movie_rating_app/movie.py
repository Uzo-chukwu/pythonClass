from datetime import datetime


class Movie:
    def __init__(self, title,):
        self.movie = {}
        self.movie['title'] = title
        self.movie['rating'] = []
        self.movie['date_created'] = datetime.now().replace(second=0, microsecond=0)

    def rate_movie(self, rating):
        if rating > 0 and rating <= 5:
            self.movie['rating'].append(rating)
        else:
            raise TypeError('Rating must be between 0 and 6')

    def get_average_rating(self):
        if len(self.movie['rating']) == 0:
            raise ValueError('Movie has no rating')
        else:
            return sum(self.movie['rating']) / len(self.movie['rating'])

    def get_time_created(self):
        return self.movie['date_created']

    def get_title(self):
        return self.movie['title']

    def get_rating(self):
        return self.movie['rating']
    def get_date_created(self):
        return self.movie['date_created']

