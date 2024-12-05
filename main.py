from app.movies_router import router as movies_router
from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="Movie API",
    description="Doctos challenge for movies",
    version="1.0.0"
)

# Router registrieren
app.include_router(movies_router, prefix="/movies", tags=["Movies"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)