# Listado de directorios.
<hr>

- Creamos la carpeta *share* en **home/alu3818/webapps** para compartir los archivos.

![imagen](./img/c1.PNG)

- Editamos el archivo **/etc/nginx/sites-available/alu3818** para introducir un nuevo *location* donde irá la carpeta *share*.

![imagen](./img/c9.PNG)

- Creamos el enlace simbólico del archivo en **sites-enabled**.

![imagen](./img/c3.PNG)

- Y recargamos el servicio nginx.

![imagen](./img/c4.PNG)

<hr>

- Ahora, dentro de la carpeta */webapps/share* creamos los enlaces simbólicos a los archivos que queremos subir a la página *compartida*

![imagen](./img/c7.PNG)

<hr>


- Resultado


![imagen](./img/c8.PNG)

# **LINK** **http://alu3818.me/share/**
