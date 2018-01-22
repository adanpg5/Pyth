# UT4-A1: Implantación de Wordpress

---

## Realizar la instalación de Wordpress en el dominio wordpress.alu3818.me

* Wordpress necesita un usuario/contraseña para acceder a una base de datos. Para ello, usaremos el intérprete de MySQL:

![img](./img/000047.png)

* Tenemos que crear la base de datos, el usuario y asignar privilegios:

![img](./img/000048.png)

* Descargamos el código fuente de Wordpress desde su página web:

![img](./img/000049.png)

* Lo descomprimimos.

![img](./img/000050.png)

* Y lo copiamos a `/usr/share`, estableciendo también los permisos necesarios.

![img](./img/000051.png)

![img](./img/000052.png)

* Básicamente, debemos especificar el nombre de la base de datos, el usuario y la contraseña, para que Wordpress pueda usarlos:

![img](./img/000053.png)

* Para que nuestro sitio Wordpress sea accesible desde un navegador web, debemos incluir las directivas necesarias en la configuración del servidor web Nginx.
  * Supongamos que queremos acceder a nuestro Wordpress desde la url wordpress.alu3818.me. Para ello tendremos que crear un nuevo virtual host de la siguiente manera:

![img](./img/000054.png)

* Enlazamos con `sites-enabled`

![img](./img/000055.png)

* Y reiniciamos el servicio.

![img](./img/000056.png)

* Una vez esto, ya podemos instalar **Wordpress**.
  * Para ello accedemos al navegador mediante `wordpress.alu3818.me` y elegimos el idioma, nombre/contraseña y correo.

![img](./img/000057.png)

![img](./img/000058.png)

* Y ya tenemos wordpress instalado y configurado.

![img](./img/000059.png)

---

## Ajustar los permalinks a Día y Nombre.

![img](./img/000060.png)

* En primer lugar, nos dirigimos a *Ajustes -> Enlaces permanentes* y activamos esta opción dentro de la interfaz administrativa de Wordpress:

![img](./img/000061.png)

* Ahora debemos indicar a Nginx que procese estas URLs:

![img](./img/000062.png)

---

## Instalar y activar un tema gratuito.

* En la pestaña <Kbd>Apariencia</kbd> -> <Kbd>Temas</kbd> buscamos uno que nos guste. Clickamos sobre el, y le pulsamos **Instalar**.

![img](./img/000063.png)

* Cuando finalice, clickamos esta vez en **Activar**.

![img](./img/000064.png)

---

## Escribir un post con las estadísticas de uso de Wordpress vistas en clase y entrar a dicho post.

* En la sección <Kbd>Entradas</kbd> podemos crear nuestros posts.
  * Para hacer uno nuevo vamos a *Añadir nuevo*, le ponemos un título y a continuación el texto que nosotros queramos publicar.
  * Pulsamos sobre <Kbd>Publicar</kbd>.

![img](./img/000065.png)

* Ya podemos ver nuestra primera publicación.

![img](./img/000066.png)

---
