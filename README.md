# Pokedex Personal

Una aplicación web full-stack para explorar, buscar y gestionar tus Pokémon favoritos con apodos personalizados.

## Instalación y Ejecución

### Requisitos
- Python 3.8 o superior
- Node.js 18 o superior
- npm 9 o superior

### Backend (Servidor)

1. Instalar dependencias:
```bash
cd backend
pip install -r requirements.txt
```

2. Ejecutar servidor:
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

## Decisiones Técnicas

### Backend - FastAPI
- **Razón**: Framework moderno, rápido y con documentación automática
- **Ventajas**: Validación de datos automática, sintaxis simple, alta performance

### Frontend - Angular
- **Razón**: Framework robusto con componentes reutilizables y TypeScript
- **Ventajas**: Escalabilidad, mantenibilidad, ecosistema completo

### Base de Datos - JSON
- **Razón**: Simplicidad para prototipos y aplicaciones pequeñas
- **Ventajas**: No requiere instalación, fácil de entender, portabilidad

### API Externa - PokéAPI
- **Razón**: Datos oficiales, gratuitos y actualizados de Pokémon
- **Ventajas**: Información confiable, documentación completa, sin costos

### Arquitectura - REST API
- **Razón**: Estándar de la industria, separación clara de responsabilidades
- **Ventajas**: Escalabilidad, mantenibilidad, fácil integración

### Diseño - Responsive con Glassmorphism
- **Razón**: Experiencia de usuario moderna y accesible
- **Ventajas**: Funciona en cualquier dispositivo, efectos visuales atractivos

### Resumes de Decisiones Tecnicas
- Se tomo la decisión de manejar el tema del backend por su versatilidad y sintaxis con menos complejidad que nodeJS, y unir con Angular un framework el cual trabaja por componetes da una organizacion mayor al proyecto.

## Uso

1. **Página de Inicio**: Muestra los 10 Pokémon más populares
2. **Búsqueda**: Busca Pokémon por nombre o número
3. **Favoritos**: Guarda, edita apodos y elimina tus Pokémon favoritos

---

**Nota**: Asegúrate de tener tanto el backend como el frontend ejecutándose simultáneamente.