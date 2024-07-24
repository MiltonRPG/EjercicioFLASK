FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos y aplicación
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py

# Crear directorio para logs
RUN mkdir -p logs

# Establecer variables de entorno por defecto
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379
ENV REDIS_PASSWORD=

# Exponer el puerto
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
