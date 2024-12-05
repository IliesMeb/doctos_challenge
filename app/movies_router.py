from fastapi import APIRouter, HTTPException
from typing import List

from app import movie_schema as schema
from app import movie_service as service	

router = APIRouter()

@router.get("/", response_model=List[schema.Movie])
def get_movies():
    """get all movies"""
    return service.get_all_movies()

@router.post("/", response_model=dict)
def add_movie(movie: schema.MovieInput):
    """add one new movie"""
    movie = service.add_movie(movie)
    return {"message": "Movie successful added", "movie": movie}

@router.get("/{movie_id}", response_model=schema.Movie)
def get_movie_by_id(movie_id: int):
    """get one movie by id"""
    movie = service.get_movie_by_id(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")
    return movie

@router.delete("/{movie_id}", response_model=dict)
def delete_movie(movie_id: int):
    """delete one movie by id"""
    movie = service.delete_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with id {movie_id} not found")
    return {"message": f"Movie {movie.title} with id {movie_id} successful deleted"}
