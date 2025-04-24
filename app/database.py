import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Leer la URL de la base de datos desde la variable de entorno
DATABASE_URL = os.getenv(
    "DATABASE_URL", "mysql+pymysql://user:password@localhost/todo_db"
)  # Default for local testing

# Crear el motor SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear una clase base para los modelos declarativos
Base = declarative_base()


# Dependencia para obtener la sesión de la base de datos en las rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
