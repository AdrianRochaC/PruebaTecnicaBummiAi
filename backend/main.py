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
    id: int
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
    
    # Verificar si ya existe por ID o nombre
    for existing in data:
        # Verificar si el favorito existente tiene 'id' y comparar
        if "id" in existing and existing["id"] == fav.id:
            raise HTTPException(status_code=400, detail="Pokémon ya existe en favoritos")
        # Siempre verificar por nombre
        if existing["name"].lower() == fav.name.lower():
            raise HTTPException(status_code=400, detail="Pokémon ya existe en favoritos")
    
    data.append(fav.dict())
    save_favorites(data)
    return {"message": "Favorito Guardado", "pokemon": fav.dict()}

@app.delete("/api/favorites/{name}")
def delete_favorite(name: str):
    data = load_favorites()
    original_length = len(data)
    updated = [fav for fav in data if fav["name"].lower() != name.lower()]
    
    # Si no se encontró el favorito para eliminar
    if len(updated) == original_length:
        raise HTTPException(status_code=404, detail="Favorito no Encontrado")
    
    save_favorites(updated)
    return {"message": f"{name} eliminado de favoritos"}

@app.put("/api/favorites/{pokemon_name}")
def update_favorite_nickname(pokemon_name: str, nickname_data: dict):
    data = load_favorites()
    
    # Buscar el Pokémon por nombre
    pokemon_found = False
    for fav in data:
        if fav["name"].lower() == pokemon_name.lower():
            fav["nickname"] = nickname_data.get("nickname", "")
            pokemon_found = True
            break
    
    if not pokemon_found:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado en favoritos")
    
    save_favorites(data)
    
    # Devolver el Pokémon actualizado
    updated_pokemon = next(fav for fav in data if fav["name"].lower() == pokemon_name.lower())
    return updated_pokemon
