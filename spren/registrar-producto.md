# HU-XXX: Registrar Producto

## 📖 Historia de Usuario
Como **administrador del sistema**,
Quiero **registrar nuevos productos de limpieza en el sistema**,
Para **tener un inventario actualizado de los productos disponibles para la venta**.

## 🔁 Flujo Esperado
- El administrador autenticado accede a la interfaz de registro de productos.
- El administrador introduce el `nombre`, `descripcion`, `precio`, `cantidad` y `categoria` del producto.
- El sistema valida que el `nombre` del producto no esté registrado previamente en la base de datos.
- El sistema valida que todos los campos obligatorios estén presentes y sean válidos (ej. `precio` y `cantidad` positivos).
- El sistema consume el endpoint `POST /api/v1/products` con los datos del nuevo producto.
- El sistema registra el nuevo producto en la base de datos.
- El sistema confirma la creación exitosa del producto.
- En caso de que el nombre ya exista o los datos sean inválidos, el sistema notifica el error.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe permitir ingresar `nombre` (UNIQUE), `descripcion`, `precio` (mayor a 0), `cantidad` (mayor o igual a 0) y `categoria` del producto.
- [ ] El sistema debe validar que el `nombre` del producto no esté registrado previamente.
- [ ] El sistema debe confirmar cuando el producto fue registrado exitosamente.
- [ ] El sistema debe mostrar un mensaje de error claro si algún campo obligatorio está vacío, si los datos son inválidos o si el `nombre` del producto ya está registrado.
- [ ] Solo el `administrador` autenticado puede registrar productos.

### 2. 📆 Estructura de la información
- [ ] La solicitud `POST` para registrar un producto debe incluir `nombre`, `descripcion`, `precio`, `cantidad` y `categoria` en formato JSON.
- [ ] La respuesta exitosa (código `201 Created`) debe incluir el `id`, `nombre`, `descripcion`, `precio`, `cantidad` y `categoria` del producto creado, y un `mensaje` de éxito.
- [ ] La respuesta de error por nombre de producto duplicado (código `409 Conflict`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por datos inválidos o campos vacíos (código `400 Bad Request`) debe incluir un `mensaje` descriptivo.

## 🔧 Notas Técnicas
- La lógica de registro de productos, incluyendo la validación de unicidad del nombre y la validación de los campos numéricos, debe residir en la capa de servicio (`Service Layer`) [2].
- La tabla de productos (`productos`) debe tener una restricción de unicidad en el campo `nombre`.
- La autenticación del usuario debe ser verificada mediante el JWT proporcionado en el encabezado de la solicitud, y se debe validar que el rol del usuario sea `administrador` para acceder a esta funcionalidad.

## 🚀 Endpoint – Registrar Producto
- **Método HTTP:** `POST`
- **Ruta:** `/api/v1/products` (propuesto)

## 📤 Ejemplo de Estructura JSON

### Request (lo que se envía)
```json
{
  "nombre": "Jabón líquido",
  "descripcion": "Jabón antibacterial para manos",
  "precio": 5000,
  "cantidad": 100,
  "categoria": "limpieza personal"
}
```

### Response exitoso (201 Created)
```json
{
  "codigo": 201,
  "producto": {
    "id": 1,
    "nombre": "Jabón líquido",
    "descripcion": "Jabón antibacterial para manos",
    "precio": 5000,
    "cantidad": 100,
    "categoria": "limpieza personal"
  },
  "mensaje": "Producto registrado exitosamente"
}
```

### Response error (409 Conflict)
```json
{
  "codigo": 409,
  "mensaje": "El producto ya está registrado en el sistema"
}
```

### Response error (400 Bad Request)
```json
{
  "codigo": 400,
  "mensaje": "Datos inválidos o campos vacíos: [Detalle del campo]"
}
```

### Response error (401 Unauthorized)
```json
{
  "codigo": 401,
  "mensaje": "Usuario no autenticado"
}
```

### Response error (403 Forbidden)
```json
{
  "codigo": 403,
  "mensaje": "Usuario no autorizado para registrar productos"
}
```

### Response error (500 Internal Server Error)
```json
{
  "codigo": 500,
  "mensaje": "Error interno del servidor al registrar el producto"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Registro exitoso de un nuevo producto
- **Precondición:** El nombre "Limpiador Multiusos" no está registrado. El usuario está autenticado como `administrador`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/products` con `nombre: "Limpiador Multiusos"`, `descripcion: "Limpiador para todo tipo de superficies"`, `precio: 12000`, `cantidad: 50`, `categoria: "limpieza del hogar"`.
- **Resultado esperado:**
  - Código HTTP `201 Created`.
  - La respuesta JSON contiene los datos del producto registrado y `mensaje`: "Producto registrado exitosamente".
  - El producto es persistido en la base de datos.

### ❌ Caso 2: Intento de registrar un producto con nombre duplicado
- **Precondición:** El nombre "Jabón líquido" ya está registrado en el sistema. El usuario está autenticado como `administrador`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/products` con `nombre: "Jabón líquido"` y otros datos válidos.
- **Resultado esperado:**
  - Código HTTP `409 Conflict`.
  - La respuesta JSON contiene `mensaje`: "El producto ya está registrado en el sistema".

### ❌ Caso 3: Intento de registrar un producto con campos obligatorios faltantes
- **Precondición:** El usuario está autenticado como `administrador`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/products` con un cuerpo JSON incompleto (ej. sin `nombre`).
- **Resultado esperado:**
  - Código HTTP `400 Bad Request`.
  - La respuesta JSON contiene `mensaje`: "Datos inválidos o campos vacíos: [Detalle del campo faltante]".

### ❌ Caso 4: Intento de registrar un producto con `precio` o `cantidad` inválidos
- **Precondición:** El usuario está autenticado como `administrador`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/products` con `precio: -100` o `cantidad: -5`.
- **Resultado esperado:**
  - Código HTTP `400 Bad Request`.
  - La respuesta JSON contiene `mensaje`: "Datos inválidos: El precio y la cantidad deben ser valores positivos".

### ❌ Caso 5: Intento de registrar un producto sin autenticación
- **Precondición:** El usuario no está autenticado.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/products` con datos válidos sin un token de autenticación.
- **Resultado esperado:**
  - Código HTTP `401 Unauthorized`.
  - La respuesta JSON contiene `mensaje`: "Usuario no autenticado".

### ❌ Caso 6: Intento de registrar un producto por usuario no autorizado (ej. vendedor)
- **Precondición:** El usuario está autenticado como `vendedor`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/products` con datos válidos.
- **Resultado esperado:**
  - Código HTTP `403 Forbidden`.
  - La respuesta JSON contiene `mensaje`: "Usuario no autorizado para registrar productos".

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema permite el registro de nuevos productos con `nombre`, `descripcion`, `precio`, `cantidad` y `categoria`.
- [ ] El sistema valida la unicidad del `nombre` del producto.
- [ ] El sistema valida que `precio` y `cantidad` sean valores válidos.
- [ ] El sistema maneja correctamente los casos de nombres duplicados, datos inválidos y accesos no autorizados.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la validación de campos, unicidad del nombre y validación de valores numéricos.
- [ ] Se cubrieron los casos de registro exitoso de productos.
- [ ] Se cubrieron los casos de error por nombre duplicado, campos faltantes/inválidos y usuarios no autorizados.
- [ ] Las pruebas funcionales para el endpoint de registro de productos están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de registro de productos está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Campos de entrada y salida (modelos JSON).
  - Ejemplos de respuestas exitosas y de error.
- [ ] La estructura de la tabla `productos` en la base de datos está documentada.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `400 Bad Request` para datos inválidos o campos vacíos.
- [ ] Se devuelve código HTTP `401 Unauthorized` si el usuario no está autenticado.
- [ ] Se devuelve código HTTP `403 Forbidden` si el usuario autenticado no tiene permisos para registrar productos.
- [ ] Se devuelve código HTTP `409 Conflict` cuando se intenta registrar un producto con un nombre ya existente.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] ENTREGABLE WEB SERVICE (1).pdf - Sección "2. API del Módulo de Productos"
[2] API Layer.txt - Sección "Service Layer"
