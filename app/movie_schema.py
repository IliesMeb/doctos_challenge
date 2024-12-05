from pydantic import BaseModel

class MovieInput(BaseModel):
    title: str = ""
    genre: str = ""
    year: int 

class Movie(BaseModel):
    id: int = 0
    title: str = ""
    genre: str = ""
    year: int 


    class Config:
        orm_mode = True
