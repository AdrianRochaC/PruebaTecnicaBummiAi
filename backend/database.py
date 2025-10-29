from models import Favorite
import config
from typing import List
from datetime import datetime

async def get_favorites() -> List[dict]:
    try:
        if config.database is None:
            raise ValueError("Base de datos no inicializada")
        collection = config.database.favorites
        cursor = collection.find({})
        favorites = []
        async for doc in cursor:
            doc["_id"] = str(doc["_id"])
            favorites.append(doc)
        return favorites
    except Exception as e:
        print(f"Error obteniendo favoritos: {e}")
        return []

async def add_favorite(favorite: Favorite) -> dict:
    try:
        if config.database is None:
            raise ValueError("Base de datos no inicializada")
        collection = config.database.favorites
        
        # Verificar si ya existe
        existing = await collection.find_one({
            "$or": [
                {"id": favorite.id},
                {"name": {"$regex": f"^{favorite.name}$", "$options": "i"}}
            ]
        })
        
        if existing:
            raise ValueError("Pokémon ya existe en favoritos")
        
        favorite_dict = favorite.dict()
        favorite_dict["created_at"] = datetime.utcnow()
        
        result = await collection.insert_one(favorite_dict)
        favorite_dict["_id"] = str(result.inserted_id)
        return favorite_dict
    except Exception as e:
        print(f"Error agregando favorito: {e}")
        raise e

async def delete_favorite(name: str) -> bool:
    try:
        if config.database is None:
            raise ValueError("Base de datos no inicializada")
        collection = config.database.favorites
        result = await collection.delete_one({"name": {"$regex": f"^{name}$", "$options": "i"}})
        return result.deleted_count > 0
    except Exception as e:
        print(f"Error eliminando favorito: {e}")
        return False

async def update_favorite_nickname(name: str, nickname: str) -> dict:
    try:
        if config.database is None:
            raise ValueError("Base de datos no inicializada")
        collection = config.database.favorites
        result = await collection.find_one_and_update(
            {"name": {"$regex": f"^{name}$", "$options": "i"}},
            {"$set": {"nickname": nickname}},
            return_document=True
        )
        if not result:
            raise ValueError("Pokémon no encontrado")
        result["_id"] = str(result["_id"])
        return result
    except Exception as e:
        print(f"Error actualizando apodo: {e}")
        raise e