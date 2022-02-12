from app import db


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50))
    direccion = db.Column(db.String(50))