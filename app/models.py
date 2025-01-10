from app.database import db


class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)  
    nombre = db.Column(db.String(100), nullable=False)  
    precio = db.relationship('Precio', backref='producto', uselist=False, lazy=True, cascade='all, delete')
    stock = db.relationship('Stock', backref='producto', uselist=False, lazy=True, cascade='all, delete')


class Precio(db.Model):
    __tablename__ = 'precios'
    id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False) 

class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True) 
    cantidad = db.Column(db.Integer, nullable=False)