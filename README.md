# Recismart
Projecto Recismart pre-entrega  14-12-2022 (En desarrollo!)



<h1>Instrucciones para la ejecucion del programa</h1>
<h3>Cuentas de login: </h3>

     login: test
    password: taller.2022 ( no disponible aun)
<br>
<h3>Instrucciones: </h3>

1.  descomprimir el archivo en el escritorio.
2.  abrir una consola en cmd o terminal en linux
3.  instalar virtualenv

**pip install virtualenv env**



4. digitar para abrir entorno virtual enviroment


    env\Script\activate

5. instalar django en entorno virtual


    pip install django

6. Realizar makemigrations y migrate


    python manage.py makemigrations
    python manage.py migrate


7. Instalar las librerias necesarias en archivo "requeriments.txt"


    pip install -r requirements.txt


8. Levantar el server


    python manage.py runserver


<h4>Si desea ejecutar la aplicacion en algun IDE o editor de texto, debe realizar lo mismo. </h4>


<h3>Vistas URL (aun en desarrollo)</h3>


http://127.0.0.1:8000/home

http://127.0.0.1:8000/maspublicaciones
     
http://127.0.0.1:8000/accounts/login
     
http://127.0.0.1:8000/panel
     
http://127.0.0.1:8000/registro
     
http://127.0.0.1:8000/registrorecolector
     
http://127.0.0.1:8000/registroaviso
