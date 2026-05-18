# Gestión de Citas Médicas API

API REST desarrollada con FastAPI para la gestión de citas médicas, 
con chat en tiempo real entre pacientes y médicos.

## Características

- Gestión de usuarios (pacientes y médicos)
- Centros médicos y especialidades
- Sistema de citas con estados
- Chat en tiempo real con WebSockets
- Autenticación con JWT
- Mensajes guardados en base de datos

## Tecnologías

- FastAPI
- PostgreSQL
- SQLAlchemy
- WebSockets
- JWT (python-jose)
- bcrypt

## Instalación

1. Clona el repositorio
2. Crea un entorno virtual e instala las dependencias:
   pip install -r requirements.txt
3. Crea un archivo .env con las variables:
   DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_db
   SECRET_KEY=tusecretkey
4. Arranca el servidor:
   uvicorn app.main:app --reload

## Endpoints principales

- POST /users — Crear usuario
- POST /login — Autenticación
- POST /quotes — Crear cita
- WS /ws/{user_id}/{receptor_id}?token= — Chat en tiempo real
- GET /messages — Historial de mensajes
