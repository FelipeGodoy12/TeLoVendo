# Telovendo

La aplicacion Te Lo vendo, es una aplicacion de e-commerce que cuenta con una pagina principal que muestra el catalogo de productos
con una pestaña para el registro de proveedores y de usuarios de la aplicacion
una pagina de estadisticas y una de contacto

tambien contiene la opcion de login para los usuarios de la pagina

Para poder levantar la aplicacion de manera local, se debe clonar el repositorio, en un entorno virtual tener instalado el framework Django, 
asgiref==3.5.0
Django==4.0.4
sqlparse==0.4.2
tzdata==2022.1
tambien tener instalado la version de python 3.10.2

PERMISOS

Se crean 3 grupos de usuarios con permisos diferenciado, uno que se refiere a los clientes y tiene los permisos para el CRUD de clientes,
uno que se refiere a los proveedores y tiene los permisos para el CRUD de proveedores, uno que se refiere a los vendedores y tiene los permisos para el CRUD de vendedores, se realiza esta diferenciacion de usuarios debido a que cada uno de las clases tienen utilidades diferentes para la aplicacion
