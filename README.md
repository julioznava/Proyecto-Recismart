# Recismart



Proyecto realizado con los siguientes lenguajes y frameworks:

* Python (Django)

* HTML

* CSS

* Bootstrap 5

  

###	En que consiste?

Es un sitio en el cual tu puedes ayudar a realizar reciclaje con objetos de cualquier índole que ya no utilices en tu hogar o tu empresa.

Vale decir puedes publicar el objeto que no utilices y otra persona o empresa dedicada al reciclaje se puede contactar contigo y concretar la venta donación o intercambios de productos.

La idea es un sitio sin fines de lucros y ayuda a incentivar a la gente a darle una segunda oportunidad a objetos que ya no esta usando y lo tiene abandonado en su hogar y ayudar a empresas de reciclaje a dar mas protagonismo y cuidar el medio ambiente.



### Imágenes	

![image](https://github.com/julioznava/Proyecto-Recismart/assets/67343722/04877de9-e9a9-45eb-9a56-14e752454372)

![image](https://github.com/julioznava/Proyecto-Recismart/assets/67343722/538b446f-a5c2-41ae-a034-08f7c402d0e3)

![image](https://github.com/julioznava/Proyecto-Recismart/assets/67343722/f132f4a4-7390-49f2-840c-f04f8bac57e1)

![image](https://github.com/julioznava/Proyecto-Recismart/assets/67343722/eced46eb-7df2-488f-866b-36c3ba18bae2)

![image](https://github.com/julioznava/Proyecto-Recismart/assets/67343722/5c5a976d-ac3b-4de7-9281-c799351ad2e3)



## Instrucciones de ejecución



<h3>Cuentas de login: </h3>

     login: admin
    password: admin 

<h3>Instrucciones: </h3>

1.  descomprimir el archivo en el escritorio.
2.  abrir una consola en cmd o terminal en Linux
3.  instalar virtualenv

**pip install virtualenv env**



4. digitar para abrir entorno virtual enviroment


    env\Script\activate

5. instalar Django en entorno virtual


    pip install django

6. Realizar makemigrations y migrate


    python manage.py makemigrations
    python manage.py migrate


7. Instalar las librerías necesarias en archivo "requeriments.txt"


    pip install -r requirements.txt


8. Levantar el server


    python manage.py runserver



#### Si desea ejecutar la aplicación en algún IDE o editor de texto, debe realizar lo mismo. 


<h3>Vistas URL (aun en desarrollo)</h3>


http://127.0.0.1:8000/home

http://127.0.0.1:8000/maspublicaciones
     
http://127.0.0.1:8000/accounts/login
     
http://127.0.0.1:8000/panel
     
http://127.0.0.1:8000/registro
     
http://127.0.0.1:8000/registrorecolector
     
http://127.0.0.1:8000/registroaviso



###	Posibles desarrollo futuro y correcciones:

* A nivel de backend implementar mayores funciones, como un dashboard  y alguna sesión para mirar los usuarios que han comentado tu publicación

* Mejorar la seguridad de login y segmentar entre recolectores, usuarios y publicadores
* Tener un sistema de chat para que los mismas personas interesadas puedan tener acceso al usuario que ha publicado.
* Mejorar las publicaciones recomendadas y las listas de publicaciones (probablemente con sistema de puntuaciones y filtros)
