



# 1. Descripcion general del proyecto: AisModa

Aplicación web desarrollada con django, estilo Marketplace

## 1.1- User History
los usuarios podrán registrarse comprar productos,  
registrarse como vendedores, 
postear productos, y recibir remuneración por la compra de sus productos, 

## [View Live](https://django-ecommerce-v1.herokuapp.com/)

##  9.  Vistas y Secciones

1. [Home page](https://django-ecommerce-v1.herokuapp.com/)
   1. productos
   2. buscador
   3. categorías
2. footer:
   1. Sobre Nosotros: descripción, perfil, redes
3. Login
4. registro de usuarios
5. panel de usuarios
   1. datos de usuarios
   2.  panel de tienda
   3.  historial productos comprados
   4.  carrito de compras ( productos por comprar)
   5.  registro de vendedores
   6.  panel de tienda


## 4.1.- Funcionalidades

- Registro de usuarios
- Registro de vendedores
- Post Productos
- Categorías
- Precio
- Buscador
- Productos similares
- Stock de productos
- Productos destacados
- Agregar productos al carrito
- Remuneración a cada vendedor por cada producto del carrito


# 2. Metodologia de trabajo  

Metodologias agiles y scrum

## 1.1.- Colaboradores y desarrolladores

<table>

<tr>
<td align="left" ><h2>Nombre</td>
<td align="left" ><h2>Rol</td>
<td align="left" ><h2>Stack</td>
<td align="left" ><h2>Residencia</td>
<td align="left" ><h2>LinkedIn</td>
<td align="left" ><h2>GitHub</td>
</tr>

<!-- Arturo -->
<tr>
<td align="left" >Arturo</td>
<td align="left" >BackEnd</td>
<td align="left" >Python, FastAPI, PostgresSQL, Javascript, git, Flask, Linux, CSS, Diseño de Base de datos</td>
<td align="left" >México</td>
<td align="left" ><a href="https://www.linkedin.com/in/arturo-mart%C3%ADnez-pacheco-273456155/">Arturo</a> </td>

<td align="left" ><a href="https://github.com/Arturomtz8">Arturomtz8</a> </td>
</tr>

<!-- David -->
<tr>
<td align="left" >David</td>
<td align="left" >BackEnd</td>
<td align="left" >Python, django, postgres, github actions, beautiful soup </td>
<td align="left" >Panamá</td>
<td align="left" ><a href="https://www.linkedin.com/in/david-mor%C3%A1n-005163195 ">David</a> </td>
<td align="left" ><a href="https://github.com/davidmr27">davidmr27</a> </td>
</tr>

<!-- Fernando -->
<tr>
<td align="left" >Fernando</td>
<td align="left" >BackEnd</td>
<td align="left" >Python, Django, Docker, Bash, JS, React</td>
<td align="left" >México</td>
<td align="left" ><a href="https://www.linkedin.com/in/fernando-guerrero1/">Fernando</a> </td>
<td align="left" ><a href="https://github.com/devrrior">devrrior</a> </td>
</tr>

<!-- Angel -->
<tr>
<td align="left" >Angel</td>
<td align="left" >Full Stack</td>
<td align="left" >Python, django, PostgresSQL, tailwind, bootstrap, CSS, javascript, react, vue, docker</td>
<td align="left" >Venezuela</td>
<td align="left" ><a href="https://www.linkedin.com/in/angelriera/">Angel</a> </td>
<td align="left" ><a href="https://github.com/RagAndRoll">RagAndRoll</a> </td>
</tr>


<!-- Danny -->
<tr>
<td align="left" >Danny</td>
<td align="left" >FrontEnd</td>
<td align="left" >HTML,CSS, JS, REACT, NODE, PHP, PYTHON,Tailwind, bootstrap, sass </td>
<td align="left" >Venezuela</td>
<td align="left" ><a href="https://www.linkedin.com/in/danny-solano-755a09182/">Danny</a> </td>
<td align="left" ><a href="https://github.com/Drastick17">Drastick17</a> </td>
</tr>

<!-- Oriana -->
<tr>
<td align="left" >Oriana</td>
<td align="left" >Team leader</td>
<td align="left" >HTML,CSS, JS, REACT, NODE, PHP, PYTHON,Tailwind, bootstrap, sass </td>
<td align="left" >Argentina</td>
<td align="left" ><a href="linkedin.com/in/oriana-pellegrini/">Oriana</a> </td>
<td align="left" ><a href="https://github.com/Oriana10">Oriana10</a> </td>
</tr>

</table>


# 3. Stack de desarrollo

1. Backend: 
   1. Django
2. Relación Base de Datos
   1. PostgresSql
3. Frontend: JavaScript / Tailwind / SASS
4. Entornos virtualels:
   1. Virtualenv
   2. pipenv
   3. devcointainer
5. Testing:
   1. Github Actions
   2. TestCase
   3. isort
   4. black
   5. flake8

# 3. Herramientas de Produccion
7.  Deploy




# Geting Started Pipenv
## 1.- Pip install
    
Option 1
```
$ sudo apt update
$ sudo apt install python3-venv python3-pip
```
Option 2

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   ⇒ descarga paquetes iniciales
python get-pip.py
python -m pip install --upgrade pip
```


## 2.- Install Postgres SQl


```
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get -y install postgresql postgresql-contrib
$ sudo apt-get install libpq-dev
```

### 2.2.- execute postgresql

$ sudo service postgresql status
$ sudo service postgresql start


### 2.3.- Create database and password

sudo -u postgres psql => start console

```
postgres=# alter user Postgres with password 'newPasword';
postgres=# CREATE DATABASE name 
```

- set this dates in your .env

POSTGRES_NAME=name
POSTGRES_PASSWORD=newPasword





## 3.- install environment pipenv

python3 -m pip install pipenv


## 4.- activate Virtual environment

pipenv shell
or
python3 -m pipenv shell

pipenv install
pipenv lock -r 

## get server run

python manage.py runserver



# 2.- documentacion
# 2.1- [Ejecución del proyecto en docker como entorno de desarrollo](./readme/Docker_guide.md) 



