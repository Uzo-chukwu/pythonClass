from src.movie_rating_app.user import User
from src.movie_rating_app.movies import Movies
user = User("user")
movies = Movies()
def main():

        while True:
            choice = input("""
                       ---Welcome to Jetflix MovieRating App---
                           what would you like to do?
                           1. Add a movie
                           2. Rate a movie
                           3. Get average rating of a movie
                           4. Get total average of all movies
                           5. Exit
               """)

            match choice:
                case "1":
                    movie_name = input("Enter movie name: ")
                    movies.add_movie(movie_name)
                    print(movie_name + " added successfully")
                case "2":
                    movie_name = input("Enter name of movie you'd like to rate: ")
                    rating = input("Enter rating 1-5: ")
                    user.rate_movie(rating, movie_name, movies)

                case "3":
                    movie_name = input("Enter movie name: ")
                    average_rating = user.get_average_movie_rating(movie_name, movies)
                    print("Average rating for " + movie_name + " is: " + str(average_rating))
                case "4":
                    total_average = user.get_total_average_rating(movies)
                    print("Total average for all movies is: " + str(total_average))
                case "5":
                    break

main()