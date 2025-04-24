# Usar una imagen base de Python compatible con ARM64
FROM python:3.11-slim

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar uv
RUN pip install uv

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN uv pip install --no-cache --system -r requirements.txt

# Copiar el directorio de la aplicación
COPY ./app /app/app

# Exponer el puerto en el que correrá Uvicorn dentro del contenedor
# Usaremos 8000 como estándar dentro del contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación
# Escucha en 0.0.0.0 para ser accesible desde fuera del contenedor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 