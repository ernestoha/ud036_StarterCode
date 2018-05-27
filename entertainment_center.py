import media
import fresh_tomatoes
import json


def get_movies():
    # Parse Json "movies.txt" file and return a media.Movie array.
    movies = []
    json_movies = json.load(open('movies.txt'))
    for json_movie in json_movies:
        movies.append(media.Movie(
            json_movie['movie_title'],
            json_movie['movie_storyline'],
            json_movie['poster_image'],
            json_movie['trailer_youtube'])
        )
    return movies

# Create .html file with the movies array.
fresh_tomatoes.open_movies_page(get_movies())
