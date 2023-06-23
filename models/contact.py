from utils.db import db


class mdu(db.Model):
    id_mdu = db.Column(db.SmallInteger, primary_key=True)
    descripcion = db.Column(db.String(30))

    def __init__(self, id_mdu, descripcion):
        self.id_mdu = id_mdu
        self.descripcion = descripcion


class area_comun(db.Model):
    id_area_comun = db.Column(db.SmallInteger, primary_key=True)
    descripcion = db.Column(db.String(50))

    def __init__(self, id_area_comun, descripcion):
        self.id_area_comun = id_area_comun
        self.descripcion = descripcion

class tipo_predio(db.Model):
    id_tipo_predio = db.Column(db.Integer, primary_key=True)
    nomre_predio = db.Column(db.String)

    def __init__(self, id_tipo_predio, nomre_predio):
        self.id_tipo_predio = id_tipo_predio
        self.nomre_predio = nomre_predio

class predio(db.Model):
    id_predio = db.Column(db.Integer, primary_key=True)
    id_tipo_predio = db.Column(db.Integer)
    descripcion = db.Column(db.String(80))
    ruc = db.Column(db.String(20))
    telefono = db.Column(db.String(12))
    correo = db.Column(db.String(80))
    direccion = db.Column(db.String(100))
    idubigeo = db.Column(db.String(6))

    def __init__(self, id_predio, id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo):
        self.id_predio = id_predio
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.idubigeo = idubigeo


class predio_area_comun(db.Model):
    id_predio = db.Column(db.Integer, primary_key=True)
    id_area_comun = db.Column(db.Integer)
    codigo = db.Column(db.String(6))
    area = db.Column(db.Numeric)

    def __init__(self, id_predio, id_area_comun, codigo, area):
        self.id_predio = id_predio
        self.id_area_comun = id_area_comun
        self.codigo = codigo
        self.area = area


class predio_mdu(db.Model):
    id_predio_mdu = db.Column(db.Integer, primary_key=True)
    id_predio = db.Column(db.Integer)
    id_mdu = db.Column(db.SmallInteger)
    descripcion = db.Column(db.String(4))
    direccion = db.Column(db.String(10))
    numero = db.Column(db.String(10))

    def __init__(self, id_predio_mdu, id_predio, id_mdu, descripcion, direccion, numero):
        self.id_predio_mdu = id_predio_mdu
        self.id_predio = id_predio
        self.id_mdu = id_mdu
        self.descripcion = descripcion
        self.direccion = direccion
        self.numero = numero


class casa(db.Model):
    id_casa = db.Column(db.Integer, primary_key=True)
    id_predio = db.Column(db.Integer)
    id_estado = db.Column(db.Integer)
    id_predio_mdu = db.Column(db.Integer)
    numero = db.Column(db.SmallInteger)
    piso = db.Column(db.SmallInteger)
    area = db.Column(db.Numeric)
    participacion = db.Column(db.Numeric(6,2))#precision=6, scale=2

    def __init__(self, id_casa, id_predio, id_estado, id_predio_mdu, numero, piso, area, participacion):
        self.id_casa = id_casa
        self.id_predio = id_predio
        self.id_estado = id_estado
        self.id_predio_mdu = id_predio_mdu
        self.numero = numero
        self.piso = piso
        self.area = area
        self.participacion = participacion
