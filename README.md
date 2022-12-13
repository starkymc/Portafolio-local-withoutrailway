<h1 align="center">Proyecto Portafolio</h1>
<hr>

<div align="center">
<img aling="center" width="900" height="400" src="index.png" />
</div>




### Projecto principal donde se trabajo inicialmente y donde estan todos los commits, y se subio a Railway
- https://github.com/starkymc/Portafolio
    
### Creacion de Projecto principal localmente funcionando
- https://github.com/starkymc/Portafolio-local-withoutrailway

<hr>

## Youtube
![image-portafolio](youtube.png) <br>
[Youtube demo - Click aqui](https://www.youtube.com/watch?v=HJ986S9yxWo "link title")

# Vamos al proyecto! 

### Para poder correr el proyecto correctamente debes seguir los pasos siguientes:
### Clonar el repositorio en la terminal
    git clone https://github.com/starkymc/Portafolio-local-withoutrailway
    
### Entramos a la carpeta Portafolio
    cd .\Portafolio-local-withoutrailway\

### Dentro de nuestra proyecto creamos nuestro entorno virtual
    virtualenv -p python3 env

### Entramos al entorno virtual
    .\env\Scripts\activate

### Instalamos los requerimientos
    pip install -r requirements.txt

### En este caso se uso la base de datos mysql con las siguientes configuraciones en caso quieras configurar aqui esta la estructura
 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            
            'NAME': 'portafolio', #nombre de la bd
            
            'USER': '', #nombre del usuario
            
            'PASSWORD': '', #password del usuario
            
            'HOST': 'localhost', #host
            
            'PORT': '3306'  #puerto
        }
    }

### Creamos nuestra base de datos en MySQL
    create database portafolio;

### Hacemos las migraciones en la terminal
    python manage.py makemigrations
    python manage.py migrate

### Finalmente ya tenemos todo listo corremos el programa
    python manage.py runserver
    
    
### Rutas principales del proyeco:
    Inicio de sesion ("/")
    Registro ("/signup")
    Vista de la pagina principal ("/profile")
    Creacion de portafolio ("/crearportafolio")
    
    
