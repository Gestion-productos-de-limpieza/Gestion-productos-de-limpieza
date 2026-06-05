# HU-XXX: Listar Productos

## 📖 Historia de Usuario
Como **administrador o vendedor del sistema**,
Quiero **listar todos los productos de limpieza registrados en el sistema**,
Para **consultar el inventario disponible y gestionar las ventas**.

## 🔁 Flujo Esperado
- El usuario autenticado (administrador o vendedor) accede a la sección de productos del sistema.
- El sistema realiza una consulta a la base de datos para obtener los productos, aplicando filtros si se especifican (por `nombre` o `categoría`).
- Para cada producto, el sistema recupera sus detalles, incluyendo `nombre`, `descripción`, `precio`, `cantidad` (stock) y `categoría`.
- El sistema presenta la lista de productos al usuario.
- Si no hay productos registrados o no se encuentran resultados con los filtros aplicados, el sistema muestra un mensaje informativo.
- Si el usuario no está autenticado, el sistema deniega el acceso.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe mostrar todos los productos registrados con sus detalles completos (`id`, `nombre`, `descripcion`, `precio`, `cantidad`, `categoria`).
- [ ] El sistema debe permitir filtrar productos por `nombre` (búsqueda parcial) o `categoría`.
- [ ] El sistema debe mostrar la `cantidad` disponible (stock) de cada producto.
- [ ] El sistema debe mostrar un mensaje claro si no hay productos registrados o si la búsqueda no arroja resultados.
- [ ] Solo usuarios autenticados (con roles de `administrador` o `vendedor`) pueden listar los productos.

### 2. 📆 Estructura de la información
- [ ] La solicitud para listar productos puede incluir parámetros de consulta para filtros (ej. `?nombre=jabón`, `?categoria=limpieza%20personal`).
- [ ] La respuesta exitosa (código `200 OK`) debe incluir una lista de objetos `productos`, cada uno con la estructura detallada en el ejemplo JSON.
- [ ] La respuesta de error por no haber productos registrados (código `404 Not Found`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por usuario no autenticado (código `401 Unauthorized`) debe incluir un `mensaje` descriptivo.

## 🔧 Notas Técnicas
- La lógica de listado y filtrado de productos debe residir en la capa de servicio (`Service Layer`) [2].
- La consulta a la base de datos debe ser eficiente, utilizando índices adecuados para los campos de filtro (`nombre`, `categoria`).
- La autenticación del usuario debe ser verificada mediante el JWT proporcionado en el encabezado de la solicitud, y se debe validar que el rol del usuario tenga permisos para acceder a esta funcionalidad.

## 🚀 Endpoint – Listar Productos
- **Método HTTP:** `GET`
- **Ruta:** `/api/v1/products` (propuesto)

## 📤 Ejemplo de Estructura JSON

### Response exitoso (200 OK)
```json
{
  "codigo": 200,
  "productos": [
    {
      "id": 1,
      "nombre": "Jabón líquido",
      "descripcion": "Jabón antibacterial para manos",
      "precio": 5000,
      "cantidad": 100,
      "categoria": "limpieza personal"
    },
    {
      "id": 2,
      "nombre": "Desinfectante",
      "descripcion": "Desinfectante multiusos para superficies",
      "precio": 8000,
      "cantidad": 50,
      "categoria": "limpieza del hogar"
    }
  ]
}
```

### Response error (404 Not Found)
```json
{
  "codigo": 404,
  "mensaje": "No hay productos registrados"
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
  "mensaje": "Usuario no autorizado para listar productos"
}
```

### Response error (500 Internal Server Error)
```json
{
  "codigo": 500,
  "mensaje": "Error interno del servidor al listar productos"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Listar todos los productos sin filtros (usuario autorizado)
- **Precondición:** Existen múltiples productos registrados en el sistema. El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/products`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene una lista de todos los productos con sus detalles completos.

### ✅ Caso 2: Listar productos filtrados por nombre (usuario autorizado)
- **Precondición:** Existen productos con el nombre "Jabón" (o similar). El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/products?nombre=jabón`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene solo los productos cuyo nombre coincide con el filtro.

### ✅ Caso 3: Listar productos filtrados por categoría (usuario autorizado)
- **Precondición:** Existen productos en la categoría "limpieza del hogar". El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/products?categoria=limpieza%20del%20hogar`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene solo los productos de la categoría especificada.

### ❌ Caso 4: Intento de listar productos sin autenticación
- **Precondición:** El usuario no está autenticado.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/products` sin un token de autenticación.
- **Resultado esperado:**
  - Código HTTP `401 Unauthorized`.
  - La respuesta JSON contiene `mensaje`: "Usuario no autenticado".

### ❌ Caso 5: Intento de listar productos por usuario no autorizado (ej. cliente)
- **Precondición:** El usuario está autenticado como `cliente`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/products`.
- **Resultado esperado:**
  - Código HTTP `403 Forbidden`.
  - La respuesta JSON contiene `mensaje`: "Usuario no autorizado para listar productos".

### ❌ Caso 6: No hay productos registrados (usuario autorizado)
- **Precondición:** No existen productos en el sistema. El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/products`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - La respuesta JSON contiene `mensaje`: "No hay productos registrados".

### ❌ Caso 7: No hay productos que coincidan con los filtros (usuario autorizado)
- **Precondición:** Existen productos, pero ninguno coincide con los filtros aplicados (ej. nombre de producto inexistente). El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/products?nombre=productoinexistente`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - La respuesta JSON contiene `mensaje`: "No hay productos registrados" (o "No se encontraron productos con los filtros aplicados").

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema permite listar todos los productos con sus detalles completos, incluyendo el stock.
- [ ] El sistema soporta el filtrado de productos por `nombre` y `categoría`.
- [ ] El sistema maneja los casos donde no hay productos o no se encuentran resultados con los filtros.
- [ ] El acceso al listado de productos está protegido por autenticación y autorización de roles.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la lógica de filtrado y la recuperación de detalles de producto.
- [ ] Se cubrieron los casos de listado exitoso con y sin filtros.
- [ ] Se cubrieron los casos de error por falta de autenticación, usuario no autorizado y ausencia de productos.
- [ ] Las pruebas funcionales para el endpoint de listado de productos están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de listado de productos está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Parámetros de consulta para filtros.
  - Ejemplos de respuestas exitosas y de error.
- [ ] La estructura de la tabla `productos` en la base de datos está documentada.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `401 Unauthorized` si el usuario no está autenticado.
- [ ] Se devuelve código HTTP `403 Forbidden` si el usuario autenticado no tiene permisos para listar productos.
- [ ] Se devuelve código HTTP `404 Not Found` si no hay productos registrados o no se encuentran resultados con los filtros.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] ENTREGABLE WEB SERVICE (1).pdf - Sección "2. API del Módulo de Productos"
[2] API Layer.txt - Sección "Service Layer"
