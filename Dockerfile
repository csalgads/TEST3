# Usamos una imagen base de Python
FROM python:3.12-rc-slim


#set envionment variables
ENV PYTHONUNBUFFERED 1


# run this before copying requirements for cache efficiency
RUN pip install --upgrade pip


# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el archivo de requisitos (requirements.txt) al contenedor
COPY requirements.txt .

# Instalamos las dependencias usando pip
RUN pip install -r requirements.txt

# Copiamos el resto de los archivos de la aplicación al contenedor
COPY . .

# Comando por defecto que se ejecutará cuando se inicie el contenedor
#CMD ["python", "./manage.py]