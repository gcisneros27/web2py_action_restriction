########### administracion de aciones de controlador ###########################
def admin_accion():
    grid= SQLFORM.grid(db.auth_function,
    headers={'auth_function.accion' : 'Acción de Controlador'},
	searchable=True,
	deletable=True,
	editable=True,
	create=True,
    onvalidation=validar_accion
	)

    return dict(grid=grid)

######## Construye el formulario de asignacion de permisos #####################
def asignacion_permisos():
    grupos=db(db.auth_group).select()
    form = formulario_permisos(grupos)
    if  request.vars.rol and request.vars.to:
        rol=request.vars.rol
        try:
            db(db.auth_permission.group_id == rol).delete()
            for i in request.vars.to:
                db.auth_permission.insert(group_id=rol,name='default',table_name='auth_function',record_id=i)
            response.flash='Permisos guardados exitosamente'
        except:
            db.rollback()
        else:
            db.commit()
    elif request.vars.rol:
        db(db.auth_permission.group_id == request.vars.rol).delete()
        response.flash='Permisos revocados'
    else:
        response.flash='Seleccione un Grupo'


    return locals()

# Responde al llamado de la funcion ajax que solicita los permisos disponibles #
def permisos_disponibles():
    opciones=''
    control1='';
    grupo=request.vars.grupo
    sql1=PERMISOS_DISPONIBLES %(grupo)
    result1=db.executesql(sql1,as_dict=True)
    for i in result1:
        if i['controlador']!=control1 and control1=='':
            opciones+='<optgroup label="'+str(i['controlador'])+'">'
            control1=i['controlador']
        elif  i['controlador']!=control1:
            opciones+='</optgroup><optgroup label="'+str(i['controlador'])+'">'
            control1=i['controlador']
        opciones+='<option value="'+str(i['id'])+'">'+str(i['accion'])+'</option>'
    opciones+='</optgroup>'
    return opciones

# Responde al llamado de la funcion ajax que solicita los permisos asignados ##
def permisos_asignados():
    opciones=''
    control1='';
    grupo=request.vars.grupo
    sql1=PERMISOS_ASIGNADOS %(grupo)
    result1=db.executesql(sql1,as_dict=True)
    for i in result1:
        if i['controlador']!=control1 and control1=='':
            opciones+='<optgroup label="'+str(i['controlador'])+'">'
            control1=i['controlador']
        elif  i['controlador']!=control1:
            opciones+='</optgroup><optgroup label="'+str(i['controlador'])+'">'
            control1=i['controlador']
        opciones+='<option value="'+str(i['id'])+'">'+str(i['accion'])+'</option>'
    opciones+='</optgroup>'
    return opciones
