################################################################################
#   Decorador para restringir el acceso a las acciones de controlador a los
#   usuarios con permisos sobre dichas acciones
################################################################################
def val_permisos():
    def val_permisos_decorador(f):
        def tiene_permisos(*args, **args2):
            scriptpath = os.path.realpath(__file__)
            cad1=scriptpath.split('/')
            controlador=cad1[-1].split('.')
            registro=db(db.auth_function.controlador==controlador and db.auth_function.accion==f.__name__).select()
            if auth.has_permission('default', db.auth_function,registro[0]['id'], auth.user.id):
                return f(*args, **args2)
            else:
                redirect(URL(request.application, 'default', 'user/not_authorized'))
                #raise HTTP(403, "NO AUTORIZADO")
        return tiene_permisos
    return val_permisos_decorador
#################################################################################################
# Funcion para verificar si un determiando usuario tiene permisos sobre una accion de controlador
#################################################################################################
def tiene_permiso(controlador,accion,usuario):
    registro=db(db.auth_function.controlador==controlador and db.auth_function.accion==accion).select()
    if auth.has_permission('default', db.auth_function,registro[0]['id'], usuario):
        return True
    else:
        return False
###########################################################################################
# Funcion que permite validar que una accion de controlador no se registre mas de una vez
###########################################################################################
def validar_accion(form):
    result=0
    cont=form.vars.controlador
    acc=form.vars.accion
    result=db((db.auth_function.controlador==cont) & (db.auth_function.accion==acc)).count()
    if result>0:
        form.errors.accion='La acción "'+acc+'" ya se encuentra registrada en el controlador "'+cont+'"'

    else:
        form.accepted = True

############################################################################################
# Función que construlle el formulario
###########################################################################################

def formulario_permisos(grupos):
    form = FORM(
        DIV(
            DIV(
                DIV(
                    LABEL('Rol'),
                    SELECT( OPTION('Seleccione', _value=''),
                                *[OPTION(grupos[i].role, _value=str(grupos[i].id)) for i in range(len(grupos))],
                                _class="form-control",_size="1",_id='grupo_id',_name='rol'
                            ),
                    )
                , _class='col-sm-5'
                )
            ,_class='row'
            ),
        BR(),
        LABEL('Permisos'),
        DIV(
            DIV(
                SELECT('',
                _name="from",_id="optgroup", _class='form-control',_size="15",_multiple="multiple")
            ,_class='col-sm-5'
            ),
            DIV(
                XML('<button type="button" id="optgroup_rightAll" class="btn btn-block btn-success"><i class="glyphicon glyphicon-forward"></i></button><button type="button" id="optgroup_rightSelected" class="btn btn-block btn-basic"><i class="glyphicon glyphicon-chevron-right"></i></button><button type="button" id="optgroup_leftSelected" class="btn btn-block btn-basic"><i class="glyphicon glyphicon-chevron-left"></i></button><button type="button" id="optgroup_leftAll" class="btn btn-block btn-danger"><i class="glyphicon glyphicon-backward"></i></button>'),BR(),BR(),INPUT(_value='Guardar', _type='submit',_class='btn btn-block btn-primary')
            ,_class='col-sm-2'
            ),
            DIV(
                SELECT('',
                _name="to",_id="optgroup_to", _class='form-control',_size="15",_multiple="multiple")
            ,_class='col-sm-5'
            )

        ,_class='row'
        ),
        )
    return form


############################################################################################
####################################### CONSULTAS ##########################################
############################################################################################

PERMISOS_DISPONIBLES= """
SELECT  id,controlador,accion FROM  auth_function
EXCEPT
SELECT  a.id,a.controlador,a.accion FROM  auth_function AS a
LEFT JOIN auth_permission AS b ON a.id=b.record_id
WHERE group_id=%s AND a.id=b.record_id
ORDER BY controlador, accion
     """

PERMISOS_ASIGNADOS= """
SELECT  a.id,a.controlador,a.accion  FROM  auth_function AS a
LEFT JOIN auth_permission AS b ON a.id=b.record_id
WHERE group_id=%s AND a.id=b.record_id
ORDER BY a.controlador, a.accion
     """
