# Dockerfile para el backend (Django)
FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema para psycopg2
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo requirements.txt
COPY requirements.txt ./

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto en el que corre la aplicación
EXPOSE 8000

# Ejecuta las migraciones y luego arranca el servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
