from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import predio, predio_area_comun, predio_mdu, casa, tipo_predio, area_comun, mdu
from utils.db import db
from sqlalchemy import func
from sqlalchemy import func, text, create_engine

contacts = Blueprint('contacts',__name__)

@contacts.route('/')
def index():
    contacts_predio = predio.query.all()
    contacts_predio_area_comun = predio_area_comun.query.all()
    contacts_predio_mdu = predio_mdu.query.all()
    contacts_casa = casa.query.all()
    return render_template('index.html', contacts_predio=contacts_predio, contacts_predio_area_comun=contacts_predio_area_comun, contacts_predio_mdu=contacts_predio_mdu, contacts_casa=contacts_casa)


################################################ AGREGAR

data_Predio = []

@contacts.route('/new/predio', methods=['POST'])
def add_predio():
    #predio
    # Obtener el último ID de predio registrado
    last_predio = db.session.query(func.max(predio.id_predio)).scalar()
    # Incrementar el último ID de predio para obtener el siguiente
    new_id_predio = last_predio + 1 if last_predio else 1    

    id_tipo_predio=request.form['id_tipo_predio']
    descripcion=request.form['descripcion']
    ruc=request.form['ruc']
    telefono=request.form['telefono']
    correo=request.form['correo']
    direccion=request.form['direccion']
    idubigeo=request.form['idubigeo']
    new_contact = predio(new_id_predio,id_tipo_predio,descripcion,ruc,telefono,correo,direccion,idubigeo)
    db.session.add(new_contact)
    db.session.commit()

    # Verificar si los campos tienen valores
    if id_tipo_predio and descripcion and ruc and telefono and correo and direccion and idubigeo:
        # Agregar una nueva fila a la lista de datos
        row = [id_tipo_predio,descripcion,ruc,telefono,correo,direccion,idubigeo]
        data_Predio.append(row)

    flash("Predio añadido satisfactoriamente!")
    return render_template('index.html', data_Predio=data_Predio)


data_ArCm = []

@contacts.route('/new/predio_area_comun', methods=['POST'])
def add_predio_area_comun():
    #predio_area_comun
    # Obtener el último ID de predio registrado
    id_predio = db.session.query(func.max(predio.id_predio)).scalar()
    id_area_comun=request.form['id_area_comun']
    codigo=request.form['codigo']
    area=request.form['area']
    new_contact = predio_area_comun(id_predio,id_area_comun,codigo,area)
    db.session.add(new_contact)
    db.session.commit()

    

    # Verificar si los campos tienen valores
    if id_area_comun and codigo and area:
        # Agregar una nueva fila a la lista de datos
        row = [id_area_comun, codigo, area]
        data_ArCm.append(row)

    flash("Predio de Area Comun añadido satisfactoriamente!")
    return render_template('index.html', data_ArCm=data_ArCm)

data_Mdu = []

@contacts.route('/new/predio_mdu', methods=['POST'])
def add_predio_mdu():
    #predio_mdu
    # Obtener el último ID de predio registrado
    last_mdu = db.session.query(func.max(predio_mdu.id_predio_mdu)).scalar()
    # Incrementar el último ID de predio para obtener el siguiente
    new_id_mdu = last_mdu + 1 if last_mdu else 1
    # Obtener el último ID de predio registrado
    id_predio = db.session.query(func.max(predio.id_predio)).scalar()
    id_mdu=request.form['id_mdu']
    descripcion=request.form['descripcion']
    direccion=request.form['direccion']
    numero=request.form['numero']
    new_contact = predio_mdu(new_id_mdu,id_predio,id_mdu,descripcion,direccion,numero)
    db.session.add(new_contact)
    db.session.commit()

    # Verificar si los campos tienen valores
    if id_predio and id_mdu and descripcion and direccion and numero:
        # Agregar una nueva fila a la lista de datos
        row = [id_predio,id_mdu,descripcion,direccion,numero]
        data_Mdu.append(row)

    flash("Predio MDU añadido satisfactoriamente!")
    return render_template('index.html', data_Mdu=data_Mdu)
    

data_Casa = []

@contacts.route('/new/casa', methods=['POST'])
def add_casa():
    #casa
    # Obtener el último ID de predio registrado
    last_casa = db.session.query(func.max(casa.id_casa)).scalar()
    # Incrementar el último ID de predio para obtener el siguiente
    new_id_casa = last_casa + 1 if last_casa else 1

    id_predio = db.session.query(func.max(predio.id_predio)).scalar()
    id_estado=request.form['id_estado']
    id_predio_mdu = id_predio_mdu = db.session.query(func.max(predio_mdu.id_predio_mdu)).scalar()
    numero=request.form['numero']#Agregar que inicie desde el 1 ?
    piso=request.form['piso']
    area=request.form['area']
    participacion=request.form['participacion']
    new_contact = casa(new_id_casa,id_predio,id_estado,id_predio_mdu,numero,piso,area,participacion)
    db.session.add(new_contact)
    db.session.commit()

    # Verificar si los campos tienen valores
    if id_predio and id_estado and id_predio_mdu and numero and piso and area and participacion:
        # Agregar una nueva fila a la lista de datos
        row = [id_predio,id_estado,id_predio_mdu,numero,piso,area,participacion]
        data_Casa.append(row)

    flash("Casa añadida satisfactoriamente!")
    return render_template('index.html', data_Casa=data_Casa)

    
    

################################################ ACTUALIZAR
@contacts.route('/update/predio/<id>', methods = ['POST','GET'])
def update_predio(id):
    #predio
    contact = predio.query.get(id)
    if request.method == 'POST':
        contact.id_predio=request.form['id_predio']
        contact.id_tipo_predio=request.form['id_tipo_predio']
        contact.descripcion=request.form['descripcion']
        contact.ruc=request.form['ruc']
        contact.telefono=request.form['telefono']
        contact.correo=request.form['correo']
        contact.direccion=request.form['direccion']
        contact.idubigeo=request.form['idubigeo']
        db.session.commit()
        return redirect(url_for("contacts.index"))
    contact = predio.query.get(id)
    flash("Predio actualizado satisfactoriamente!")
    return render_template('update.html', contact=contact, contact_type='predio')


@contacts.route('/update/predio_area_comun/<id>', methods = ['POST','GET'])
def update_predio_area_comun(id):
    #predio_area_comun
    contact = predio_area_comun.query.get(id)
    if request.method == 'POST':
        contact.id_predio=request.form["id_predio"]
        contact.id_area_comun=request.form["id_area_comun"]
        contact.codigo=request.form["codigo"]
        contact.area=request.form["area"]
        db.session.commit()
        return redirect(url_for("contacts.index"))
    contact = predio_area_comun.query.get(id)
    flash("Predio Area Comun actualizado satisfactoriamente!")
    return render_template('update.html', contact=contact, contact_type='predio_area_comun')


@contacts.route('/update/predio_mdu/<id>', methods = ['POST','GET'])
def update_predio_mdu(id):
    #predio_mdu
    contact = predio_mdu.query.get(id)
    if request.method == 'POST':
        contact.id_predio_mdu=request.form['id_predio_mdu']
        contact.id_predio=request.form['id_predio']
        contact.id_mdu=request.form['id_mdu']
        contact.descripcion=request.form['descripcion']
        contact. direccion=request.form['direccion']
        contact.numero=request.form['numero']
        db.session.commit()
        return redirect(url_for("contacts.index"))
    contact = predio_mdu.query.get(id)
    flash("Predio MDU actualizado satisfactoriamente!")
    return render_template('update.html', contact=contact, contact_type='predio_mdu')


@contacts.route('/update/casa/<id>', methods = ['POST','GET'])
def update_casa(id):
    #casa
    contact = casa.query.get(id)
    if request.method == 'POST':
        contact.id_casa=request.form['id_casa']
        contact.id_predio=request.form['id_predio']
        contact.id_estado=request.form['id_estado']
        contact.id_predio_mdu=request.form['id_predio_mdu']
        contact.numero=request.form['numero']
        contact.piso=request.form['piso']
        contact.area=request.form['area']
        contact.participacion=request.form['participacion']
        db.session.commit()
        return redirect(url_for("contacts.about"))
    contact = casa.query.get(id)
    flash("Casa actualizada satisfactoriamente!")
    return render_template('update.html', contact=contact, contact_type='casa')

################################################ ELIMINAR
@contacts.route('/delete/predio/<id>')
def delete_predio(id):

    # Eliminar Casas
    casas_delete = casa.query.filter_by(id_predio=id).all()
    for casa_delete in casas_delete:
        db.session.delete(casa_delete)

    # Eliminar Predio Área Común
    predio_area_comun_delete = predio_area_comun.query.filter_by(id_predio=id).all()
    for pac_delete in predio_area_comun_delete:
        db.session.delete(pac_delete)

    # Eliminar Predio MDU
    predio_mdu_delete = predio_mdu.query.filter_by(id_predio=id).all()
    for pm_delete in predio_mdu_delete:
        db.session.delete(pm_delete)

    # Eliminar Predio
    predio_delete = predio.query.get(id)
    db.session.delete(predio_delete)

    db.session.commit()
    flash("Predio y entidades relacionadas eliminadas satisfactoriamente!")
    return redirect(url_for('contacts.about'))


@contacts.route('/delete/predio_area_comun/<id>')
def delete_predio_area_comun(id):
#predio_area_comun
    contact = predio_area_comun.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash("Predio Area Comun eliminado satisfactoriamente!")
    return redirect(url_for('contacts.index'))

@contacts.route('/delete/predio_mdu/<id>')
def delete_predio_mdu(id):
#predio_mdu
    contact = predio_mdu.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash("Predio MDU eliminado satisfactoriamente!")
    return redirect(url_for('contacts.index'))

@contacts.route('/delete/casa/<int:id>')
def delete_casa(id):
    casa_delete  = casa.query.get_or_404(id)
    #casa
    db.session.delete(casa_delete )
    db.session.commit()
    flash("Casa eliminada satisfactoriamente!")
    return redirect(url_for('contacts.index'))

############################################# INVENTARIO.html
@contacts.route('/inventario')
def about():
    contacts_predio = predio.query.all()
    contacts_predio_area_comun = predio_area_comun.query.all()
    contacts_predio_mdu = predio_mdu.query.all()
    contacts_casa = casa.query.all()
    tipos_predio = tipo_predio.query.all()
    areas_comunes = area_comun.query.all()
    contacts_mdu = mdu.query.all()

    # Obtén el recuento de casas para cada id_predio
    cantidad_casas = {}
    for contact in contacts_casa:
        id_predio = contact.id_predio
        if id_predio in cantidad_casas:
            cantidad_casas[id_predio] += 1
        else:
            cantidad_casas[id_predio] = 1

    return render_template(
        'inventario.html',
        areas_comunes=areas_comunes,
        tipos_predio=tipos_predio,
        contacts_predio=contacts_predio,
        contacts_predio_area_comun=contacts_predio_area_comun,
        contacts_predio_mdu=contacts_predio_mdu,
        contacts_casa=contacts_casa,
        cantidad_casas=cantidad_casas,
        contacts_mdu=contacts_mdu
    )
@contacts.route('/mostrar_casas/<int:id_predio>', methods=['GET', 'POST'])
def mostrar_casas(id_predio):
    val = None
    if request.method == 'GET':
        val = request.args.get('val')
    casas_predio = casa.query.filter_by(id_predio=id_predio).all()
    predios_mdu = predio_mdu.query.all()
    mdus = mdu.query.all()
    return render_template('mostrar_casas.html', casas_predio=casas_predio, predios_mdu=predios_mdu, mdus=mdus, val=val)

@contacts.route('/contacts/filter_predios', methods=['GET', 'POST'])
def filter_predios():
    tipo_predio = request.form.get('tipo_predio')
    descripcion_predio = request.form.get('descripcion_predio')
    ruc_predio = request.form.get('ruc_predio')

    engine = create_engine('postgresql://modulo4:modulo4@137.184.120.127:5432/sigcon')
    connection = engine.connect()

    # Obtén el recuento de casas para cada id_predio
    contacts_casa = casa.query.all()
    cantidad_casas = {}
    for contact in contacts_casa:
        id_predio = contact.id_predio
        if id_predio in cantidad_casas:
            cantidad_casas[id_predio] += 1
        else:
            cantidad_casas[id_predio] = 1

    query = '''
    SELECT p.id_predio, tp.nomre_predio,
       (
           SELECT STRING_AGG(DISTINCT ac.descripcion, ', ')
           FROM predio_area_comun pac
           JOIN area_comun ac ON pac.id_area_comun = ac.id_area_comun
           WHERE pac.id_predio = p.id_predio
       ) AS area_comun_descripcion,
       (
           SELECT STRING_AGG(CASE WHEN m.descripcion IS NOT NULL THEN CONCAT(m.descripcion, ': ', pm.descripcion) ELSE pm.descripcion END, ', ')
           FROM predio_mdu pm
           JOIN mdu m ON pm.id_mdu = m.id_mdu
           WHERE pm.id_predio = p.id_predio
       ) AS mdu_descripcion,
       p.descripcion, p.ruc, p.telefono, p.correo, p.direccion, p.idubigeo
    FROM predio p
    JOIN tipo_predio tp ON p.id_tipo_predio = tp.id_tipo_predio
    LEFT JOIN predio_area_comun pac ON p.id_predio = pac.id_predio
    LEFT JOIN area_comun ac ON pac.id_area_comun = ac.id_area_comun
    LEFT JOIN predio_mdu pm ON p.id_predio = pm.id_predio
    LEFT JOIN mdu m ON pm.id_mdu = m.id_mdu
    WHERE (tp.nomre_predio = :tipo_predio OR :tipo_predio IS NULL OR :tipo_predio = '') -- Filtro por tipo_predio
    AND (p.descripcion ILIKE :descripcion_predio OR :descripcion_predio IS NULL OR :descripcion_predio = '')
    AND (p.ruc ILIKE :ruc_predio OR :ruc_predio IS NULL OR :ruc_predio = '')
    GROUP BY p.id_predio, tp.nomre_predio, p.descripcion, p.ruc, p.telefono, p.correo, p.direccion, p.idubigeo
    ORDER BY p.id_predio
    '''

    result = connection.execute(text(query).bindparams(tipo_predio=tipo_predio, descripcion_predio=f'%{descripcion_predio}%', ruc_predio=f'%{ruc_predio}%'))
    contacts = result.fetchall()

    connection.close()
    engine.dispose()

    return render_template('inventario.html', contacts=contacts, cantidad_casas=cantidad_casas)



