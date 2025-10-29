from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json, os


app = FastAPI()
FILENAME = "favorites.json"

#Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Favorite(BaseModel):
    name: str
    image: str
    nickname: str = ""

def load_favorites():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_favorites(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=2)


#Endpoints
@app.get("/api/favorites")
def get_favorites():
    return load_favorites()

@app.post("/api/favorites")
def add_favorite(fav: Favorite):
    data = load_favorites()
    data.append(fav.dict())
    save_favorites(data)
    return {"message": "Favorito Guardado"}

@app.delete("/api/favorites/{name}")
def delete_favorite(name: str):
    data = load_favorites()
    updated = [fav for fav in data if fav["name"].lower() != name.lower()]
    if len(updated) == len(data):
        raise HTTPException(status_code=404, detail = "Favorito no Encontrado")
    save_favorites(updated)
    return {"message": f"{name} eliminado de favoritos"}