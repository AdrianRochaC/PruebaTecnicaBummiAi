from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from models import Favorite
from database import get_favorites, add_favorite, delete_favorite, update_favorite_nickname
from config import connect_to_mongo, close_mongo_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()

app = FastAPI(lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/favorites")
async def get_favorites_endpoint():
    return await get_favorites()

@app.post("/api/favorites")
async def add_favorite_endpoint(fav: Favorite):
    try:
        result = await add_favorite(fav)
        return {"message": "Favorito Guardado", "pokemon": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/favorites/{name}")
async def delete_favorite_endpoint(name: str):
    success = await delete_favorite(name)
    if not success:
        raise HTTPException(status_code=404, detail="Favorito no Encontrado")
    return {"message": f"{name} eliminado de favoritos"}

@app.put("/api/favorites/{pokemon_name}")
async def update_favorite_nickname_endpoint(pokemon_name: str, nickname_data: dict):
    try:
        result = await update_favorite_nickname(pokemon_name, nickname_data.get("nickname", ""))
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))