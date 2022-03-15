## Rquerimientos:

1. instalar docker Destokc [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Intalar los plugins de vscode  
    1. [https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
    2. [https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Docker simple Imagen

entre las funciones de docker es tener un servidor aparte del nuestro para ejecutar el proyecto, para ello creamos una build para con los archivos de nuestro proyecto que seran trasladados a el contenedor de docker ademas esta build debera tener algunas instalaciones para trabajar con las herramientas del proyecto

1. Creamos un archivo `Dokerfile` preferiblemente que este alado de manage.py
    
```python
FROM python:3.8

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements 
#COPY backend/requirements.txt /backend/
#RUN python -m pip install --upgrade pip
#RUN python -m pip install -r requirements.txt
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate

WORKDIR /app
COPY . ./app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]

```

Details:
- `FROM python:3.8` ⇒ imagen que vamos a descargar desde docker hub, continene una terminal de linux expecializada para desarrollo con la herramienta objetiva
- `EXPOSE 8000` ⇒ le decimos que puerto usara dentro del container “localhost:8000”
- `ENV PYTHONDONTWRITEBYTECODE=1`
- `ENV PYTHONUNBUFFERED=1`

- Ejecucion de los comandos
```jsx
# Install pip requirements
#COPY backend/requirements.txt /backend/
#python -m pip install --upgrade pip
#RUN python -m pip install -r requirements.txt
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate
```
        
> esta toda la logica que se va a ejecutar tras crear en contenedor, lo comento para que no se ejecute para acelerar el desarrollo en local, pero recuerda ejecutar estos comandos manualmente mas adelante
- `WORKDIR /app` ⇒ le decimos al contenedor que en “/app” sera el espacio de trabajo
- `COPY . ./app` ⇒ copia todos los archivos en “.” a la direccion dentro del contenedor “./app”
- `CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]`  ⇒ la ejecucion de gunicorn
2. Acontinuacion podemos ejecutar  la build lo cual llevar todo nuestro proyecto a un contenedor
    1. `docker build` ⇒ ejecuta la build con nuestro proyecto dentro del container
3. Cada ves que modifiquemos algo de nuestro proyecto tenemos que apagar la ejecucion del container y volver a crear la build y ejecutarla, evitaremos todo este proceso en el con el `devcontainer` mas adelante

####  Hoja de comandos para la administracion de docker:
    
    `docker version`

    “Docker hub para ver las imágenes disponibles”

    `docker images`  ⇒ verifica todas las imagenes disponibles

    `docker rmi [nombre de la imagen]`  ⇒ elimina una imagen del sistema

    `docker rmi $(docker images -aq)` ⇒ Script que elimina todas las imagenes 

    `docker pull hello-word` ⇒ descarga la imagen

    `docker run hello-word` ⇒ ejecuta la imagen 

    `docker search [nombre de la imagen]` ⇒ Busca las versiones de las imágenes

    `docker run ubuntu echo 'hello world'`  ⇒ ejecuta los programas disponibles dentro de la imagen

    `docker run -it ubuntu bash`  ⇒ ejecuta de manera interactiva los programas disponibles dentro de la imagen

    “ todos los contenedores al crearse mueren vuelven a un estado en stop automáticamente”

    `docker ps`  ⇒ muestra las imágenes que están en ejecución y sus datos

    `docker ps -a`  ⇒ todos los contenedores existentes en stop

    `docker ps -aq`  ⇒ todos los contenedores existentes en stop solo mostrando una lista de id’s

    `docker rm [id o nombre]` ⇒  elimina del historial un contenedor ejecutado a través del nombre o id devuelto en el historial

    `docker rm $(docker ps -aq)` ⇒ Script que elimina todos los contenedores en stop

    `docker rm $(docker ps -aq) -f`  ⇒ Fuerza a detener y eliminar los contenedores

    `docker start [id o nombre]` ⇒ vuelve a ejecutar un contenedor del historial o en stop

    `docker stop [id o nombre]` ⇒ detiene el contenedor en ejcucion

    `docker exec -it [id o nombre] bash`  ⇒ ejecuta un programa disponible dentro del contenedor en un contenedor previamente creado
    

## Docker compose

podemos ejecutar nuestro proyecto normalmente dentro del container, el problema es que nuestro container no tiene una lectura para nuestra base de datos local, también hay otros servicios locales que necesita nuestro proyecto para ejecutarse, por ello usamos el compose

1. Creamos un archivo docker-compose.yml
2. agregamos esta configuracion
    
```
version: '3.4'

services:
    
  redis:
    restart: always
    image: redis:5
    ports:
      - "6379:6379"

  db:
    restart: always
    #restart: unless-stopped
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data
    ports:
      - 5432:5432 # para que sea visible en nuestro entorno local 
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

  django:    
    restart: always
    image: django
    container_name: django
    build:      
      context: .
      dockerfile: ./Dockerfile
    # Overrides default command so things don't shut down after the process ends.
    command: sleep infinity   
    # command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - ALLOWED_HOSTS=127.0.0.1, localhost     

    volumes:
      - .:/workspace
    depends_on:
      - db
      - redis
```
Explicaciones:
cada subcategoria de redis sera una imagen o una terminal de linux que se ejecutara en nuestro container,  ose la maquina virtual que creamos,
    
```python
  django:    # => nombre de imgen personalizada
    restart: always # => momento de ejecuciones 
    image: django  # => nombre de imgen personalizada
    container_name: django  # nombre de imgen personalizada
    build:      # => definimos que imagen tendra esta terminal
      context: .  # => definimos en que ruta buscar la imagen
      dockerfile: ./Dockerfile # => el archivo que creamos en el paso anteriro
    # Overrides default command so things don't shut down after the process ends.
    command: sleep infinity   
    # command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000" #=> el puerto que usa la imagen : el puerto en el que estara disponible en el enrtonro local
    environment: #=> variables de entorno en el path
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - ALLOWED_HOSTS=127.0.0.1, localhost     

    volumes:
      - .:/workspace #=> define que archivos de nuestro projecto se llevara al container
    depends_on: #=> definecon que otras terminales se va a conocetar
      - db
      - redis
```
    
3. aquí prefiero agregar las variables de entorno a nuestro proyecto local para poder alternar entre entornos virtuales
    1. definición de los datos de postgres
    2. sttigns usando las nuevas variables de entorno
    3. variables de entorno definidas en el docker-compose
4. ejecutamos `docker-compose build` en la terminal deberia funcionar correctamente
5. Recuerda ejecutar los comandos omitidos en el Dockerfile
    


## Devcointainer

con esta herramienta de trabajo podremos usar nuestro container como espacio de trabajo, para no tener que parar ,  y crear nuevamente la build despues de cada edicion de nuestro proyecto

1. en el entorno de desarrollo crea una carpeta `.devcontainer` que contendrá los siguientes archivos
2. El archivo `devcontainer.json` contiene la inicialización del contenedor por medio de vscode
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a71be627-ebe5-49fb-b068-072fa0e4f9ae/Untitled.png)
    
    1. contenido del archivo
    
    ```json
    // For format details, see https://aka.ms/devcontainer.json. For config options, see the README at:
    // https://github.com/microsoft/vscode-dev-containers/tree/v0.217.1/containers/docker-existing-docker-compose
    // If you want to run as a non-root user in the container, see .devcontainer/docker-compose.yml.
    {
    	"name": "Existing Docker Compose (Extend)",
    
    	// Update the 'dockerComposeFile' list if you have more compose files or use different names.
    	// The .devcontainer/docker-compose.yml file contains any overrides you need/want to make.
    	"dockerComposeFile": [
    		"../docker-compose.yml"		
    	],
    
    	// The 'service' property is the name of the service for the container that VS Code should
    	// use. Update this value and .devcontainer/docker-compose.yml to the real service name.
    	"service": "django",
    
    	// The optional 'workspaceFolder' property is the path VS Code should open by default when
    	// connected. This is typically a file mount in .devcontainer/docker-compose.yml
    	"workspaceFolder": "/workspace",
    
    	// Set *default* container specific settings.json values on container create.
    	"settings": { 		
    		"python.linting.enabled": true,
    		"python.linting.pylintEnabled": true,
    		"python.linting.pylintPath": "/usr/local/bin/pylint"
    	},
    
    	// Add the IDs of extensions you want to install when the container is created.
    	"extensions": [
    		"ms-python.python"
    	],
    
    	"remoteEnv": {
    		"PATH": "${containerEnv:PATH}"
    	},
    
    	// The 'service' property is the name of the service for the container that VS Code should
    	// use. Update this value and .devcontainer/docker-compose.yml to the real service name.
    	
    
    	// Use 'forwardPorts' to make a list of ports inside the container available locally.
    	// "forwardPorts": [],
    
    	// Uncomment the next line if you want start specific services in your Docker Compose config.
    	// "runServices": [],
    
    	// Uncomment the next line if you want to keep your containers running after VS Code shuts down.
    	"shutdownAction": "stopCompose",
    
    	// Uncomment the next line to run commands after the container is created - for example installing curl.
    	// "postCreateCommand": "apt-get update && apt-get install -y curl",
    
    	// Uncomment to connect as a non-root user if you've added one. See https://aka.ms/vscode-remote/containers/non-root.
    	// "remoteUser": "vscode"
    }
    ```
    
    `"dockerComposeFile":` ⇒ busca la ubicacion de docker-compose
    
    `"service": "django"`, ⇒ define cual de las imagenes de docker-compose 
    `"workspaceFolder": "/workspace",` ⇒ define cual seran los archivos que tomara en cuentra para actualizarlos en tiempo real
    
3. para ejecutar nuestro espacio de trabajo deberas cerrar el vscode y volverlo a abrir y utilizar la siguiente opción 
    
    Reopen in Container
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e35b0d7-f744-4682-b20e-85c819fde17b/Untitled.png)
    
4. Recuerda ejecutar los comandos omitidos en el Dockrfile
    
    ```json
    #RUN python -m pip install --upgrade pip
    #RUN python -m pip install -r requirements.txt
    #RUN python3 manage.py makemigrations
    #RUN python3 manage.py migrate
    ```
