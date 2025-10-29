#!/usr/bin/env python3
"""
Script para iniciar el servidor backend de la Pokedex Personal
"""

import uvicorn
import sys
import os

def main():
    """Inicia el servidor FastAPI"""
    try:
        print("Iniciando servidor backend de Pokedex Personal...")
        print("Backend disponible en: http://localhost:3000")
        print("API docs disponibles en: http://localhost:3000/docs")
        print("Presiona Ctrl+C para detener el servidor")
        print("-" * 50)
        
        uvicorn.run(
            "main:app",
            host="127.0.0.1",
            port=3000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario")
    except Exception as e:
        print(f"Error al iniciar el servidor: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
