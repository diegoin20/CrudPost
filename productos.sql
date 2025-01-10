-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS Prendas;
USE Prendas;

-- Crear la tabla Productos
CREATE TABLE IF NOT EXISTS Productos (
    id INT PRIMARY KEY,              -- ID del producto
    nombre VARCHAR(100) NOT NULL     -- Nombre del producto
);

-- Crear la tabla Precios
CREATE TABLE IF NOT EXISTS Precios (
    id INT PRIMARY KEY,              -- ID del producto
    precio DECIMAL(10, 2) NOT NULL,  -- Precio del producto
    FOREIGN KEY (id) REFERENCES Productos(id) ON DELETE CASCADE
);

-- Crear la tabla Stock
CREATE TABLE IF NOT EXISTS Stock (
    id INT PRIMARY KEY,              -- ID del producto
    cantidad INT NOT NULL,           -- Cantidad en stock
    FOREIGN KEY (id) REFERENCES Productos(id) ON DELETE CASCADE
);

-- Insertar datos en la tabla Productos
INSERT INTO Productos (id, nombre) VALUES
(1, 'Pantalones'),
(2, 'Camisas'),
(3, 'Corbatas'),
(4, 'Casacas');

-- Insertar datos en la tabla Precios
INSERT INTO Precios (id, precio) VALUES
(1, 200.00),
(2, 120.00),
(3, 50.00),
(4, 350.00);

-- Insertar datos en la tabla Stock
INSERT INTO Stock (id, cantidad) VALUES
(1, 50),
(2, 45),
(3, 30),
(4, 15);

-- Consultar los datos combinados

