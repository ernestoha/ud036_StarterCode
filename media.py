class Movie():
    """ Movie Class to store the movies info.

    Attributes:
        movie_title (str): Movie Title.
        movie_storyline (str): Movie Descripcion.
        poster_image (str): Url from the movie image.
        trailer_youtube (str): Url from the YoTube movie trailer.

    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

