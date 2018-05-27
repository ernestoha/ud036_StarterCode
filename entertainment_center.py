import media
import fresh_tomatoes
import json


def get_movies():
  movies = []
  json_movies = json.load(open('movies.txt'))
  for json_movie in json_movies:
    movies.append(media.Movie(json_movie['movie_title'],
                              json_movie['movie_storyline'],
                              json_movie['poster_image'],
                              json_movie['trailer_youtube']
                              )
                  )
  return movies


fresh_tomatoes.open_movies_page(get_movies())
