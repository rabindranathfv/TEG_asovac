# TEG_asovac

Este sistema esta desarrollado en Django y fueron usadas las siguientes herramientas para su desarrollo:

Framework: Django 11.13
Adaptador para conexión con PostgreSQL: psycopg2 2.7.4
Lenguaje servidor: python 2.7.6
Sistema manejador de base de datos: PosgreSQL

## Contenido

La aplicacion esta dividida en los siguientes modulos o apps 

* "core_app" : Es la app principal donde trabajaremos, esta se encargará del contenido general para todos los usuarios, y funcionalidades basicas de la aplicacion.

* "administracion" : Se  manejara  toda  la  configuración  del  sitio  para  el  administrador  o  super  admin,  desde  configuración  básica  hasta  eliminación,  activación  y  archivado  de  procesos  anteriores.

* "autores" : Se  almacenara  y  manipulara  toda  la  información  de  los  postulantes  de  los  resúmenes,  papers,etc.

* "sesiones" : Se  utilizara  para  controlar  la  asignación  de  lugares  físicos  donde  serán  expuestos  y/o  defendidos  los  resúmenes  científicos.  Consiste  en  llevar  el  control  de  todas  las  actividades  físicas  o  virtuales  según  sea  el  caso.

* "trabajos_resumenes" : Se  almacenara,  controlara  y  manipulara  toda  la  información  referente  a  los  resúmenes  científicos.

* "Seguimiento" : Facilitara  manejar  lo  involucrado  a  los  estados  de:  En  Asignación  de  trabajas  a  áreas,  En  Arbitraje  y  En  Cierre  de  Arbitraje.

* "arbitraje" : Control  de  todos  los  estados  del  proceso  de  arbitraje  en  conjunto  con  el  módulo  de  seguimiento,  accesos  flujos  de  todos  los  procesos  más  importantes  de  la  aplicación.  Manejo,  control  y  generación  de  resultados  parciales  y  totales.  Incluso  se  manejaran  las  memorias  de  AsoVAC. 

* "recursos" : Se  encargara  de  gestionar  todo  lo  referente  a  materiales  sobre  la  convención  como  los  certificados  de  asistencias,  de  postulantes,etc.

### Estructura de carpetas

Mantener la siguiente estructura para los directorios

```
├── teg_asovac/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   ├── Local/
│   │  ├── teg_asovac_src/
│   │  │     ├── administracion/
│   │  │     ├── autores/
│   │  │     ├── sesiones/
│   │  │     ├── trabajos_resumenes/
│   │  │     ├── seguimiento/
│   │  │     ├── arbitrajes/
│   │  │     ├── recursos/
│   │  │     ├── core_app/
│   │  ├── templates
│   │  └── static_env
│   │  │     ├── media_root/
│   │  │     ├── static_rooot/
│   │  └── static_pro
│   │  │     ├── static/
│   │  │     │   ├── css/
│   │  │     │   ├── fonts/
│   │  │     │   ├── imagenes/
│   │  │     │   ├── js/
│   │  ├── .gitignore
│   │  ├── manage.py
│   │  ├── .env
└── 
```

* "Static_pro" --> Define los estilos para ambiente de desarrollo (local)
* "static_env" --> Define los estilos para Produccion incluyendo static_root y media_root
* "templates" --> contendra todos los template del proyecto, respetando el formato de snake_case

### url's dispatcher

Se manejara via include en core_app y posterior se manejaran todas las rutas internamente en cada app individualmente en su urls.py

### Forma de escritura

Para la implementacion del codigo se utilizara la convecion de **snake_case** respetando las buenas practicas para el nombre de las funciones,parametros, clases, formularios, variables y constantes

### Configuracion del .env (usando Decouple)

```
DB_NAME = 'teg_asovac'
DB_HOSTNAME = ''
```

### Forma de trabajo utilizando branch

1. Existira un Branch Master que contendra los cambios ya estables y revisados.
2. Existira un Branch Development donde se se tendran los cambios estables que aun deben ser revisados por 2da vez.
3. Al desarrollar algo nuevo se procede a crear un branch nuevo con el siguiente formato *TEG-XXX* donde ese numero se indicara en la tarea del trello acompañado de una descripcion. Todos los branchs deben salir de development mientras sean funcionaldiades nuevas y si son errores deben salir desde Master. Al ser revisada la tarea por primera vez si esta correcta se hace merge hacia development.
