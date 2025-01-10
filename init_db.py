from app import create_app, db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Producto, Precio, Stock  
from config import Config

app = create_app()

with app.app_context():
    engine = create_engine(f"mysql://{Config.MYSQL_USER}:{Config.MYSQL_PASSWORD}@{Config.MYSQL_HOST}")

    conn = engine.raw_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {Config.MYSQL_DB}")
        cursor.execute(f"CREATE DATABASE {Config.MYSQL_DB}")
        conn.commit()
        print(f"Base de datos '{Config.MYSQL_DB}' eliminada y creada con éxito.")
    finally:
        conn.close()

    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    db.create_all()
    print("Tablas creadas con éxito.")

    try:
        productos = [
            Producto(id=1, nombre='Pantalones'),
            Producto(id=2, nombre='Camisas'),
            Producto(id=3, nombre='Corbatas'),
            Producto(id=4, nombre='Casacas')
        ]
        session.add_all(productos)

        precios = [
            Precio(id=1, precio=200.00),
            Precio(id=2, precio=120.00),
            Precio(id=3, precio=50.00),
            Precio(id=4, precio=350.00)
        ]
        session.add_all(precios)

        stocks = [
            Stock(id=1, cantidad=50),
            Stock(id=2, cantidad=45),
            Stock(id=3, cantidad=30),
            Stock(id=4, cantidad=15)
        ]
        session.add_all(stocks)

        session.commit()
        print("Datos insertados con éxito.")
    except Exception as e:
        session.rollback()
        print(f"Error insertando los datos: {e}")
    finally:
        session.close()
