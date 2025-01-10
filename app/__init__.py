from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from .Prendas import Prendas as Prendas_blueprint
from config import Config
from .database import db

def create_app():
    app = Flask(__name__)
    
    # Configuración de la aplicación
    app.config.from_object(Config)
    
    # Inicialización de la base de datos
    db.init_app(app)
    
    # Registro del blueprint de Prendas
    app.register_blueprint(Prendas_blueprint, url_prefix='/prendas')
    
    # Crear todas las tablas de la base de datos
    with app.app_context():
        db.create_all()
    
    # Redirigir la ruta raíz al listado de prendas
    @app.route('/')
    def home():
        return redirect(url_for('prendas.index'))
    
    return app