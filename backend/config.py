import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# MongoDB connection string
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = "pokedex_db"

# Función para obtener URL de MongoDB
def get_mongodb_url():
    return os.getenv("MONGODB_URL", "mongodb://localhost:27017")

# Global client
client = None
database = None

async def connect_to_mongo():
    global client, database
    try:
        mongodb_url = get_mongodb_url()
        print(f"Conectando a MongoDB: {mongodb_url[:50]}...")
        
        # Configuración simple y compatible
        client = AsyncIOMotorClient(
            mongodb_url,
            serverSelectionTimeoutMS=8000
        )
        database = client[DATABASE_NAME]
        
        # Test connection
        await client.admin.command('ping')
        print("Conectado a MongoDB Atlas")
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")
        raise e

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("Desconectado de MongoDB Atlas")