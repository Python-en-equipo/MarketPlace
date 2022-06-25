## 1) AisModa

AisModa es una aplicación web Marketplace que tiene el objetivo de poder comprar y vender artículos de moda. La aplicación está desarrollada principalmente por la tecnología Django.
[View Live](https://django-ecommerce-v1.herokuapp.com/)

## 2) Equipo

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
<td align="left" >Arturo Martínez Pacheco</td>
<td align="left" >BackEnd</td>
<td align="left" >Python, django, postgres, github actions, beautiful soup</td>
<td align="left" >México</td>
<td align="left" ><a href="https://www.linkedin.com/in/arturo-mart%C3%ADnez-pacheco-273456155/">Arturo</a> </td>
<td align="left" ><a href="https://github.com/Arturomtz8">Arturomtz8</a> </td>
</tr>
<!-- David -->
<tr>
<td align="left" >David Morán</td>
<td align="left" >BackEnd</td>
<td align="left" >Python, FastAPI, PostgresSQL, Javascript, git, Flask, Linux, CSS, Diseño de Base de datos</td>
<td align="left" >Panamá</td>
<td align="left" ><a href="https://www.linkedin.com/in/david-mor%C3%A1n-005163195">David</a> </td>
<td align="left" ><a href="https://github.com/davidmr27">davidmr27</a> </td>
</tr>
<!-- Fernando -->
<tr>
<td align="left" >Fernando Guerrero</td>
<td align="left" >BackEnd</td>
<td align="left" >Python, Django, Docker, Bash, JS, React</td>
<td align="left" >México</td>
<td align="left" ><a href="https://www.linkedin.com/in/fernando-guerrero1/">Fernando</a> </td>
<td align="left" ><a href="https://github.com/devrrior">devrrior</a> </td>
</tr>
<!-- Angel -->
<tr>
<td align="left" >Angel Riera</td>
<td align="left" >Full Stack</td>
<td align="left" >Python, django, PostgresSQL, tailwind, bootstrap, CSS, javascript, react, vue, docker</td>
<td align="left" >Venezuela</td>
<td align="left" ><a href="https://www.linkedin.com/in/angelriera/">Angel</a> </td>
<td align="left" ><a href="https://github.com/RagAndRoll">RagAndRoll</a> </td>
</tr>
<!-- Danny -->
<tr>
<td align="left" >Danny Solano</td>
<td align="left" >FrontEnd</td>
<td align="left" >HTML,CSS, JS, REACT, NODE, PHP, PYTHON,Tailwind, bootstrap, sass </td>
<td align="left" >Ecuador</td>
<td align="left" ><a href="https://www.linkedin.com/in/danny-solano-755a09182/">Danny</a> </td>
<td align="left" ><a href="https://github.com/Drastick17">Drastick17</a> </td>
</tr>
<!-- Oriana -->
<tr>
<td align="left" >Oriana Pellegrini</td>
<td align="left" >Team leader - Scrum Master</td>
<td align="left" >Java 8, Spring Framework, Thymeleaf, HTML,CSS, Bootstrap, Git y Github</td>
<td align="left" >Argentina</td>
<td align="left" ><a href="linkedin.com/in/oriana-pellegrini/">Oriana</a> </td>
<td align="left" ><a href="https://github.com/Oriana10">Oriana10</a> </td>
</tr>
</table>

## 2.2) Metodologia de trabajo  

Metodología Ágiles orientada a Scrum y Kanban. Haciendo uso de roles, reuniones y gestión de tareas.

## 3) User Story
Los usuarios podrán: registrarse y comprar productos. Podrán registrarse como vendedores para poner en venta productos y recibir remuneración por la compra de los mismos. 
 
## 4) Páginas y Secciones

1. Home page
   1. productos
   2. buscador
   3. categorías
   4. footer
      1. recursos
      2. redes sociales
      3. legalidad
      4. form de contacto
3. Login
4. Registro de Usuarios
5. Panel de usuarios
   1.  datos de usuarios
   2.  panel de tienda
   3.  historial productos comprados
   4.  carrito de compras
   5.  registro de vendedores
   6.  panel de tienda

## 5) Stack de Desarrollo

- Backend: 
    Django
- Relación Base de Datos
    PostgresSql
- Frontend: JavaScript / Tailwind / SASS
- Entornos virtualels:
    Virtualenv
    Pipenv
    Devcointainer
- Testing:
    Github Actions
    TestCase
    Isort
    Black
    Flake8
    
## 6) Funcionalidades

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

## 7) Herramientas 

### 7.2) Pip install
    
##### Option 1
```
$ sudo apt update
$ sudo apt install python3-venv python3-pip
```
##### Option 2
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   ⇒ descarga paquetes iniciales
python get-pip.py
python -m pip install --upgrade pip
```

### 7.3) Install Postgres SQl
```
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get -y install postgresql postgresql-contrib
$ sudo apt-get install libpq-dev
```

### 7.4) Execute Postgresql
```
$ sudo service postgresql status
$ sudo service postgresql start
```

### 7.5) Create Database and Password
```
sudo -u postgres psql // start console
```
```
postgres=# alter user Postgres with password 'newPasword';
postgres=# CREATE DATABASE name 
```
- set this dates in your .env
POSTGRES_NAME=name
POSTGRES_PASSWORD=newPasword

### 7.6) Install Environment Pipenv
```
python3 -m pip install pipenv
```

### 7.7) Activate Virtual Environment
```
pipenv shell or python3 -m pipenv shell
pipenv install
pipenv lock -r 
```

### Get Server Run
```
python manage.py runserver
```

## 8) Docker

[Ejecución del proyecto en docker como entorno de desarrollo](./readme/Docker_guide.md) 



