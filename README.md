# Pokedex Personal

Una aplicación web full-stack para explorar, buscar y gestionar tus Pokémon favoritos con apodos personalizados.

## Instalación y Ejecución

### Requisitos
- Python 3.8 o superior
- Node.js 18 o superior
- npm 9 o superior
- MongoDB Atlas (cuenta gratuita) o MongoDB local

### Backend (Servidor)

1. **Configurar MongoDB:**
   - **IMPORTANTE**: Cada desarrollador debe crear su propia cuenta gratuita en [MongoDB Atlas](https://cloud.mongodb.com/)
   - Crear cluster gratuito (M0 Sandbox)
   - Obtener URL de conexión personalizada
   - **Crear archivo `.env`** en la carpeta `backend/` con tu URL de conexión

2. **Instalar dependencias:**
```bash
cd backend
pip install -r requirements.txt
```

3. **Ejecutar servidor:**
```bash
uvicorn main:app --reload --port 3000
```

El backend estará disponible en: `http://localhost:3000`

### Frontend (Interfaz)

1. Instalar dependencias:
```bash
cd frontend
npm install
```

2. Ejecutar aplicación:
```bash
ng serve
```

El frontend estará disponible en: `http://localhost:4200`

## Configuración de MongoDB

**NOTA DE SEGURIDAD**: Cada desarrollador debe usar su propia cuenta de MongoDB. No compartas tus credenciales en el código.

### Opción 1: MongoDB Atlas (Recomendado)
1. Crear cuenta gratuita en [MongoDB Atlas](https://cloud.mongodb.com/)
2. Crear cluster gratuito (M0 Sandbox)
3. Crear usuario de base de datos
4. Configurar acceso de red (0.0.0.0/0 para desarrollo)
5. Obtener URL de conexión
6. **Crear archivo `.env`** en `backend/`:
   ```bash
   # Copiar plantilla
   cp backend/env.example backend/.env
   
   # Editar con tu URL
   MONGODB_URL=mongodb+srv://TU_USUARIO:TU_PASSWORD@cluster.mongodb.net/?appName=Cluster0
   DATABASE_NAME=pokedex_db
   ```

### Opción 2: MongoDB Local
1. Instalar MongoDB Community Server desde [mongodb.com](https://www.mongodb.com/try/download/community)
2. Iniciar servicio de MongoDB
3. **Crear archivo `.env`** en `backend/`:
   ```bash
   # Copiar plantilla
   cp backend/env.example backend/.env
   
   # Editar para MongoDB local
   MONGODB_URL=mongodb://localhost:27017
   DATABASE_NAME=pokedex_db
   ```

## Decisiones Técnicas

### Backend - FastAPI
- **Razón**: Framework moderno, rápido y con documentación automática
- **Ventajas**: Validación de datos automática, sintaxis simple, alta performance

### Frontend - Angular
- **Razón**: Framework robusto con componentes reutilizables y TypeScript
- **Ventajas**: Escalabilidad, mantenibilidad, ecosistema completo

### Base de Datos - MongoDB Atlas
- **Razón**: Escalabilidad, persistencia de datos y facilidad de despliegue
- **Ventajas**: Base de datos en la nube, backup automático, escalable, compatible con Render/Vercel

### API Externa - PokéAPI
- **Razón**: Datos oficiales, gratuitos y actualizados de Pokémon
- **Ventajas**: Información confiable, documentación completa, sin costos

### Arquitectura - REST API
- **Razón**: Estándar de la industria, separación clara de responsabilidades
- **Ventajas**: Escalabilidad, mantenibilidad, fácil integración

### Diseño - Responsive con Glassmorphism
- **Razón**: Experiencia de usuario moderna y accesible
- **Ventajas**: Funciona en cualquier dispositivo, efectos visuales atractivos

### Resumen de Decisiones Técnicas
- **Backend**: FastAPI por su versatilidad y sintaxis simple comparado con Node.js
- **Frontend**: Angular por su arquitectura de componentes y organización del proyecto
- **Base de Datos**: MongoDB Atlas para persistencia en la nube y facilidad de despliegue
- **Arquitectura**: Separación clara entre frontend y backend con API REST

## Uso

1. **Página de Inicio**: Muestra los 10 Pokémon más populares
2. **Búsqueda**: Busca Pokémon por nombre o número
3. **Favoritos**: Guarda, edita apodos y elimina tus Pokémon favoritos

## Configuración Inicial

### Para nuevos desarrolladores:
1. **Clonar el repositorio**
2. **Crear archivo `.env`**:
   ```bash
   cd backend
   cp env.example .env
   # Editar .env con tu URL de MongoDB
   ```
3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar servidor**:
   ```bash
   uvicorn main:app --reload --port 3000
   ```

## Comandos Rápidos

### Desarrollo
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 3000

# Frontend
cd frontend
npm install
ng serve
```

### Pruebas
```bash
# Probar conexión MongoDB
cd backend
python test_mongo.py

# Listar favoritos
cd backend
python list_favorites.py
```

### Despliegue
- **Backend**: Render, Railway, o Heroku
- **Frontend**: Vercel, Netlify, o GitHub Pages
- **Base de Datos**: MongoDB Atlas (cada proyecto debe tener su propia base de datos)
- **Variables de Entorno**: Configurar `MONGODB_URL` en la plataforma de despliegue

---

**Nota**: Asegúrate de tener tanto el backend como el frontend ejecutándose simultáneamente.