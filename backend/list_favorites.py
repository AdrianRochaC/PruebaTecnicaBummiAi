import asyncio
from config import connect_to_mongo, database

async def list_favorites():
    try:
        await connect_to_mongo()
        collection = database.favorites
        cursor = collection.find({})
        
        print("\n=== POKÉMON FAVORITOS ===\n")
        count = 0
        async for doc in cursor:
            count += 1
            print(f"{count}. {doc.get('name', 'Sin nombre').title()}")
            print(f"   ID: {doc.get('id')}")
            print(f"   Apodo: {doc.get('nickname', 'Sin apodo')}")
            print(f"   Imagen: {doc.get('image', 'N/A')}")
            print(f"   Creado: {doc.get('created_at', 'N/A')}")
            print()
        
        print(f"Total: {count} Pokémon favoritos\n")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if database and database.client:
            database.client.close()

if __name__ == "__main__":
    asyncio.run(list_favorites())
