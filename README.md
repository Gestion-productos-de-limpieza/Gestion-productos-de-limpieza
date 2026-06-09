# 🧴 CleanShop — Sistema de Gestión de Productos de Limpieza

Aplicación web desarrollada con **Spring Boot**, **Thymeleaf** y **MySQL** para la gestión de una tienda de productos de limpieza. Permite administrar productos, categorías, clientes, ventas y pedidos con control de acceso por roles.

---

## 👥 Integrantes

| Nombre | Rol |
|---|---|
| Juan Sebastián Gélvez Pérez | Desarrollador Full Stack |
| Sharon Nikol García Durán | Desarrolladora Full Stack |

---

## 🎯 Objetivos del Proyecto

### Objetivo General
Desarrollar una aplicación web que permita gestionar eficientemente el inventario, ventas y clientes de una tienda de productos de limpieza, facilitando el control administrativo mediante una interfaz intuitiva y segura.

### Objetivos Específicos
- Implementar un módulo de autenticación y autorización con control de acceso basado en roles (administrador / usuario).
- Gestionar el catálogo de productos organizados por categorías, con operaciones CRUD completas.
- Registrar y consultar ventas, pedidos y sus respectivos detalles.
- Administrar la información de los clientes de la tienda.
- Proveer una interfaz web responsiva desarrollada con Thymeleaf.

---

## 📋 Justificación

Las tiendas de productos de limpieza manejan un volumen considerable de inventario, clientes y transacciones que resulta difícil de controlar manualmente. La ausencia de un sistema centralizado genera errores en el registro de ventas, pérdida de información y dificultades para hacer seguimiento al inventario. Este proyecto busca digitalizar esos procesos mediante una aplicación web accesible, segura y fácil de usar, aplicando tecnologías del entorno empresarial actual como Spring Boot y MySQL.

---

## 🛠️ Entorno de Trabajo

| Tecnología | Versión / Detalle |
|---|---|
| Java | 17+ |
| Spring Boot | 3.x |
| Spring Security | 6/7 |
| Thymeleaf | Motor de plantillas MVC |
| Spring Data JPA / Hibernate | ORM |
| MySQL | 8.x |
| Maven | Gestión de dependencias |
| IDE | IntelliJ IDEA / VS Code |
| Control de versiones | Git + GitHub |
| SO de desarrollo | Windows 11 |

---

## ✅ Requerimientos Funcionales

| ID | Requerimiento |
|---|---|
| RF-01 | El sistema debe permitir registrar, editar, listar y eliminar productos. |
| RF-02 | El sistema debe permitir gestionar categorías de productos. |
| RF-03 | El sistema debe permitir registrar y gestionar clientes. |
| RF-04 | El sistema debe permitir registrar ventas asociadas a clientes. |
| RF-05 | El sistema debe registrar el detalle de cada venta (productos, cantidades). |
| RF-06 | El sistema debe permitir crear y gestionar pedidos. |
| RF-07 | El sistema debe registrar el detalle de cada pedido. |
| RF-08 | El sistema debe permitir crear usuarios con roles asignados (admin / usuario). |
| RF-09 | El sistema debe autenticar usuarios mediante usuario y contraseña. |
| RF-10 | El sistema debe restringir el acceso a funciones según el rol del usuario. |

---

## 🚫 Requerimientos No Funcionales

| ID | Requerimiento |
|---|---|
| RNF-01 | La contraseña de los usuarios debe almacenarse cifrada con BCrypt. |
| RNF-02 | La aplicación debe responder en menos de 3 segundos ante cualquier operación CRUD. |
| RNF-03 | La interfaz debe ser responsiva y compatible con navegadores modernos (Chrome, Firefox, Edge). |
| RNF-04 | La base de datos debe mantener integridad referencial mediante claves foráneas. |
| RNF-05 | El código fuente debe estar versionado en GitHub con ramas organizadas. |
| RNF-06 | La aplicación debe seguir el patrón de arquitectura MVC. |
| RNF-07 | El sistema debe proteger todas las rutas sensibles mediante Spring Security. |

---

## 🗄️ Base de Datos

### Diagrama de Entidad-Relación (DER)

```
categorias        productos           clientes
----------        ---------           --------
id_categoria ──── id_producto         id_cliente
nombre            nombre              nombre
descripcion       descripcion         email
                  precio              telefono
                  stock               direccion
                  id_categoria

roles             usuarios            usuario_roles
-----             --------            -------------
id_rol            id_usuario ─────── id_usuario
nombre            username            id_rol
                  password
                  email

ventas            detalle_ventas      pedidos           detalle_pedidos
------            --------------      -------           ---------------
id_venta ──────── id_detalle          id_pedido ──────── id_detalle
id_cliente        id_venta            id_cliente          id_pedido
fecha             id_producto         fecha               id_producto
total             cantidad            estado              cantidad
                  precio_unitario     total               precio_unitario
```

### Tablas del sistema

La base de datos `cleanshop_db` contiene 10 tablas:

`categorias` · `productos` · `clientes` · `ventas` · `detalle_ventas` · `pedidos` · `detalle_pedido` · `usuarios` · `roles` · `usuario_roles`

### Script SQL

```sql
-- ============================================================
--  CleanShop DB - Script de creación e inserción de datos
-- ============================================================

CREATE DATABASE IF NOT EXISTS cleanshop_db;
USE cleanshop_db;

-- Categorías
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Productos
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- Clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    email VARCHAR(100),
    telefono VARCHAR(20),
    direccion TEXT
);

-- Roles
CREATE TABLE roles (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Usuarios
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);

-- Usuario-Roles (relación N:M)
CREATE TABLE usuario_roles (
    id_usuario INT,
    id_rol INT,
    PRIMARY KEY (id_usuario, id_rol),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

-- Ventas
CREATE TABLE ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    fecha DATE NOT NULL,
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Detalle de Ventas
CREATE TABLE detalle_ventas (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT,
    id_producto INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Pedidos
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    fecha DATE NOT NULL,
    estado VARCHAR(50) DEFAULT 'PENDIENTE',
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Detalle de Pedidos
CREATE TABLE detalle_pedido (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    id_producto INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- ============================================================
--  Datos de prueba
-- ============================================================

INSERT INTO categorias (nombre, descripcion) VALUES
('Desengrasantes', 'Productos para remover grasa y aceite'),
('Desinfectantes', 'Productos para eliminar gérmenes y bacterias'),
('Limpiadores de piso', 'Productos especiales para superficies de piso'),
('Limpiavidrios', 'Productos para limpiar vidrios y espejos');

INSERT INTO productos (nombre, descripcion, precio, stock, id_categoria) VALUES
('Desengrasante Industrial 1L', 'Alta concentración para cocinas', 18500.00, 50, 1),
('Cloro Multiusos 2L', 'Desinfectante y blanqueador', 12000.00, 80, 2),
('Limpiador de Pisos Lavanda 3L', 'Deja aroma fresco', 15000.00, 60, 3),
('Limpiavidrios Transparente 500ml', 'Sin rayas para vidrios', 9500.00, 40, 4),
('Desinfectante de Superficies 1L', 'Elimina el 99.9% de gérmenes', 22000.00, 35, 2);

INSERT INTO clientes (nombre, email, telefono, direccion) VALUES
('María Fernández', 'maria@email.com', '3001234567', 'Calle 45 #23-10, Bucaramanga'),
('Carlos Ruiz', 'carlos@email.com', '3107654321', 'Carrera 18 #12-34, Bucaramanga'),
('Distribuciones López', 'lopez@distrib.com', '6076001122', 'Av. Los Estudiantes #9-50');

INSERT INTO roles (nombre) VALUES ('ROLE_ADMIN'), ('ROLE_USER');

-- Contraseña: admin123 (BCrypt)
INSERT INTO usuarios (username, password, email) VALUES
('admin', '$2a$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'admin@cleanshop.com'),
('usuario1', '$2a$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'user1@cleanshop.com');

INSERT INTO usuario_roles VALUES (1, 1), (2, 2);

INSERT INTO ventas (id_cliente, fecha, total) VALUES
(1, '2026-06-01', 45500.00),
(2, '2026-06-03', 22000.00);

INSERT INTO detalle_ventas (id_venta, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 1, 18500.00), (1, 3, 1, 15000.00), (1, 4, 1, 9500.00),
(2, 5, 1, 22000.00);

INSERT INTO pedidos (id_cliente, fecha, estado, total) VALUES
(3, '2026-06-05', 'PENDIENTE', 75000.00);

INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 2, 18500.00), (1, 2, 3, 12000.00);
```

---

## 🚀 ¿Cómo ejecutar el proyecto?

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/CleanShop.git

# 2. Crear la base de datos y ejecutar el script SQL
mysql -u root -p < cleanshop_db.sql

# 3. Configurar application.properties
spring.datasource.url=jdbc:mysql://localhost:3306/cleanshop_db
spring.datasource.username=root
spring.datasource.password=TU_PASSWORD

# 4. Ejecutar con Maven
./mvnw spring-boot:run
```

Acceder en: `http://localhost:8080`

---

## 📁 Estructura del Proyecto

```
src/
├── main/
│   ├── java/com/cleanshop/
│   │   ├── controller/
│   │   ├── model/
│   │   ├── repository/
│   │   ├── service/
│   │   └── security/
│   └── resources/
│       ├── templates/
│       ├── static/
│       └── application.properties
```

---

*Proyecto académico — Unidades Tecnológicas de Santander (UTS), Bucaramanga*
