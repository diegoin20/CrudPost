import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from datetime import date
from app.models import Producto, Precio, Stock
from app.database import db
from . import Prendas

@Prendas.route('/', methods=['GET'])
def index():
    """ Muestra el listado de productos """
    busqueda = request.args.get('busqueda', '')
    
    if busqueda:
        productos = Producto.query.filter(Producto.nombre.ilike(f'%{busqueda}%')).all()
    else:
        productos = Producto.query.all()
    
    return render_template('prendas/Listar.html', productos=productos, busqueda=busqueda)

@Prendas.route('/agregar', methods=['GET', 'POST'])
def agregar():
    """ Permite agregar un nuevo producto """
    if request.method == 'POST':
        try:
            nuevo_producto = Producto(
                nombre=request.form.get('nombre'),
            )
            
            db.session.add(nuevo_producto)
            db.session.commit()
            
            precio = request.form.get('precio')
            cantidad = request.form.get('cantidad')
            
            if precio:
                nuevo_precio = Precio(id=nuevo_producto.id, precio=precio)
                db.session.add(nuevo_precio)
            
            if cantidad:
                nuevo_stock = Stock(id=nuevo_producto.id, cantidad=cantidad)
                db.session.add(nuevo_stock)
            
            db.session.commit()
            
            flash('Producto agregado correctamente.', 'success')
            return redirect(url_for('prendas.index'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al agregar el producto: {e}', 'danger')
    
    return render_template('prendas/Agregar.html')

@Prendas.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """ Permite editar un producto existente """
    producto = Producto.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            # Actualizar producto
            producto.nombre = request.form.get('nombre')
            
            # Actualizar o crear precio
            precio_valor = request.form.get('precio')
            if precio_valor:
                if not producto.precio:
                    producto.precio = Precio(id=producto.id)
                producto.precio.precio = precio_valor
            
            # Actualizar o crear stock
            cantidad = request.form.get('cantidad')
            if cantidad:
                if not producto.stock:
                    producto.stock = Stock(id=producto.id)
                producto.stock.cantidad = cantidad
            
            db.session.commit()
            flash('Producto actualizado correctamente.', 'success')
            return redirect(url_for('prendas.index'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar el producto: {e}', 'danger')
    
    return render_template('prendas/EditarProducto.html', producto=producto)

@Prendas.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    print(f"Request method: {request.method}")  # Debug: Verificar método
    producto = Producto.query.get_or_404(id)
    print(f"Producto encontrado: {producto}")  # Debug: Verificar producto encontrado
    
    try:
        if producto.precio:
            print(f"Eliminando precio: {producto.precio}")  # Debug: Verificar precio
            db.session.delete(producto.precio)
        if producto.stock:
            print(f"Eliminando stock: {producto.stock}")  # Debug: Verificar stock
            db.session.delete(producto.stock)
        db.session.delete(producto)
        db.session.commit()
        
        flash('Producto eliminado correctamente.', 'success')
        return redirect(url_for('prendas.index'))
        
    except Exception as e:
        db.session.rollback()
        print(f"Error al eliminar el producto: {e}")  # Debug: Log de error detallado
        flash(f'Error al eliminar el producto: {e}', 'danger')
        return redirect(url_for('prendas.index'))