# Funcionalidad para restringir el acceso a las acciones de controlador en Web2py
> Es un complemento para el modulo de permisos de web2py, el cual se basa en RBAC y permite restringir el acceso a tablas y registros determinados. En este repositorio se incluye una aplicacion web2py completa en la cual se encuentra incorporado la funcionalidad de restricción de acciones, sim embargo, los archivos necesarios para incorporar esta funcionalidad en cualquier aplicacion web2py estandar son los siguientes

* *models/permisos.py*
* *controllers/permisos.py*
* *views/permisos/admin_accion.py*
* *views/permisos/asignacion_permisos.py*

> Además, para la asignacion de permisos se utiliza el plugin Two-side Multi Select Plugin with jQuery - multiselect.js, el cual se puede descargar en el siguiente enlace https://www.jqueryscript.net/form/Two-side-Multi-Select-Plugin-with-jQuery-multiselect-js.html

* *static/js/multiselect.min.js*

## Observaciones 
> Esta aplicaciones usa una base de datos postgres. Si se utiliza este complemento con otra base de datos, debe revisarse en el modelo permisos.py las consultas a base de datos.
