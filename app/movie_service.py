from typing import List, Optional
from data.movies import mocked_movies as movies
from app import movie_schema as schema


def get_all_movies() -> List[schema.Movie]:
    """get all movies from movies list and assign id 
    (usually id would be not changable and unique, 
    but as I need the ids to be incremented as there is otherwise the possibility of duplicated ids, 
    this is my workaround)"""
    movies_with_ids = [movie.copy(update={"id": index}) for index, movie in enumerate(movies, start=1)]

    return movies_with_ids

def add_movie(movie_data: schema.Movie) -> schema.Movie:
    """add one new movie and put it on the end of movies list"""
    new_movie = schema.Movie(
        title=movie_data.title,
        year=movie_data.year,
        genre=movie_data.genre
    )
    movies.append(new_movie)
    return new_movie

def get_movie_by_id(movie_id: int) -> Optional[schema.Movie]:
    """get one movie by id assign id to it (explanation above)"""
    movie = [movie.copy(update={"id": index}) for index, movie in enumerate(movies, start=1) if index == movie_id]
    if not movie:
        return None
    return movie[0]

def delete_movie(movie_id: int) -> bool:
    "delete movie by id"
    movie = [movie for index, movie in enumerate(movies, start=1) if index == movie_id]
    if not movie:
        return False
    movies.remove(movie[0])
    return movie[0]
