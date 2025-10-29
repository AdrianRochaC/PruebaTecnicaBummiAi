import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# MongoDB connection string
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = "pokedex_db"

# Función para obtener URL con parámetros SSL
def get_mongodb_url():
    url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    if "mongodb+srv://" in url:
        # Agregar parámetros SSL para Render
        if "?" not in url:
            url += "?retryWrites=true&w=majority&ssl=true&tlsAllowInvalidCertificates=true"
        elif "ssl=" not in url:
            url += "&ssl=true&tlsAllowInvalidCertificates=true"
    return url

# Global client
client = None
database = None

async def connect_to_mongo():
    global client, database
    try:
        # Usar URL con parámetros SSL
        mongodb_url = get_mongodb_url()
        client = AsyncIOMotorClient(mongodb_url)
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