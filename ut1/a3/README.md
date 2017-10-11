# Trabajo con *virtual-hosts*

<hr>

* La actividad consiste en configurar 4 sitios web (virtual hosts) en nuestro servidor web Nginx.

<hr>

# Página 1. - http://imw.alu3818.me/

* Nos dirigimos a la carpeta `/etc/nginx/sites-available`, que es donde creamos el *virtual host*.
* Creamos el archivo llamada **imw**, y en él introducimos el *nombre de servidor* y la *ruta* donde tendremos el cuerpo de la página.

![imagen](./img/c2.PNG)

![imagen](./img/c3.PNG)

* Con un `cd ../sites-enabled` nos dirigimos a la carpeta de sitios activos, donde haremos el enlace simbólico del servidor de *sites-available*.
  - Utilizamos `sudo ln -s ../sites-available/imw` para crear dicho enlace.

![imagen](./img/c4.PNG)

* En la carpeta */home/alu3818/webapps* es donde pondremos todos los cuerpos de nuestras webs, o los **index**.
  - Creamos la carpeta **imw**.

![imagen](./img/c5.PNG)

* Dentro de la carpeta *imw* creamos un html, y ponemos un enlace a la imagen que vamos a mostrar en nuestra web.

![imagen](./img/c6.PNG)

* Hacemos un `sudo systemctl reload nginx.service` para recargar el servicio y entramos a dicha página en el navegador, y se mostraría la imagen.

![imagen](./img/c7.PNG)

* Para hacer una **subweb**, añadimos un *location* en el archivo del server, que quedaría de esta forma.

![imagen](./img/c8.PNG)

* Y volvemos a crear la carpeta con el nombre de la *subweb* en *webapps*

![imagen](./img/c9.PNG)

* Ponemos el contenido que queremos dentro de dicha carpeta.

![imagen](./img/c10.PNG)

* Editamos el index para que tenga una forma dentro del navegador.

![imagen](./img/c11.PNG)

* Y volvemos a *reiniciar* el servicio.

![imagen](./img/c12.PNG)

* Si entramos en http://imw.alu3818.me/mec, vemos que ya está la página que hicimos.

![imagen](./img/c13.PNG)

<hr>

# Página 2. - http://varlib.alu3818.me:9000

* Vamos a *sites-available* y creamos un archivo llamado **varlib**.
  - Añadimos el puerto que va a escuchar, que nosotros elegiremos el **9000**.
  - La ruta de los archivos que queremos mostrar.
  - Un autoindex, para que lo indexe todo con órden.

![imagen](./img/c14.PNG)

* Creamos el enlace simbólico en *sites-enabled* de lo anterior.

![imagen](./img/c15.PNG)

* Y recargamos el servicio nginx.

![imagen](./img/c16.PNG)

* Utilizando [este enlace](http://varlib.alu3818.me:9000) entramos en la página resultado.


![imagen](./img/c17.PNG)

<hr>

# Página 3. - https://ssl.alu3818.me/students/

* Vamos a acceder a esta web con *Usuario y contraseña*, para ello creamos una contraseña encriptada de *aula108*.
  - La contraseña encriptada la metemos dentro de un archivo de texto con el nombre del usuario.

![imagen](./img/c19.PNG)

![imagen](./img/c21.PNG)

* Volvemos a **sites-available** y creamos su archivo.
En este caso tendremos que añadir líneas nuevas, como el *auth_basic y el auth_basic_user_file* para poner el archivo de la contraseña y el usuario.
  - El usuario es `usuario1`.
  - La contraseña es `aula108`.

![imagen](./img/c23.PNG)

* Introducimos las credenciales al entrar en la página
https://ssl.alu3818.me/students/ y ya entraríamos.

![imagen](./img/c24.PNG)

![imagen](./img/c25.PNG)

<hr>

# Página 4. - http://redirect.alu3818.me

* Descargamos en la moodle el archivo que vamos a utilizar en nuestra web, pero en la máquina producción.

![imagen](./img/c26.PNG)

* Lo descomprimimos.

![imagen](./img/c27.PNG)

* Y lo mandamos por `scp` a la máquina de desarrollo, al *cloud*.

![imagen](./img/c28.PNG)

* Desde la carpeta en la que lo tengamos, tenemos que llevarlo hacia `webapps/target` que es donde tendremos la ruta hacia el servidor.

![imagen](./img/c29.PNG)

* En *sites-available* creamos dos archivos, uno como `redirect` y otro como `target`.
  * En el **redirect**, realizaremos las **redirecciones**, es decir, nosotros queremos que nos redireccione desde *redirect.alu3818.me* a *target.alu3818.me*.
  * De la misma manera queremos que nos reenvíe desde *www.redirect.alu3818.me* a *target.alu3818.me*.

* En el **target**, escucharemos desde el puerto 80, le damos el nombre de servidor, y la ruta hacia los archivos que va a tener nuestra página web (*webapps/target*).


![imagen](./img/c34.PNG)

* Y ya por último, entrando desde http://redirect.alu3818.me
o desde http://www.redirect.alu3818.me entraríamos a la web final.

![imagen](./img/c35.PNG)

<hr>

# Enlaces directos a las webs.


WEB | Enlace | :octocat:
 ------------ | ------------- | ------------
Primera | [Enlace](http://imw.alu3818.me/)  | :+1:
Segunda | [Enlace](http://varlib.alu3818.me:9000) | :+1:
Tercera | [Enlace](https://ssl.alu3818.me/students/) | :+1:
Cuarta  | [Enlace sin www](http://redirect.alu3818.me) / [Enlace con www](http://www.redirect.alu3818.me) | :+1:)
