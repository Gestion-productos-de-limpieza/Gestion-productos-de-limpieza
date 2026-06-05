# HU-XXX: Registrar Factura

## 📖 Historia de Usuario
Como **administrador o vendedor del sistema**,
Quiero **registrar nuevas facturas en el sistema**,
Para **gestionar las ventas, aplicar descuentos y actualizar el inventario**.

## 🔁 Flujo Esperado
- El usuario autenticado (administrador o vendedor) accede a la interfaz de registro de facturas.
- El usuario selecciona un `cliente_id` existente y una lista de `productos` con sus `cantidades`.
- El sistema valida la existencia del cliente y de cada producto, así como la disponibilidad de stock para las cantidades solicitadas.
- El sistema calcula el `subtotal` de la factura.
- El sistema verifica el `tipo_cliente` del cliente seleccionado y aplica el `descuento_porcentaje` correspondiente si es `mayorista` [1].
- El sistema calcula el `descuento_valor` y el `total` final de la factura.
- El sistema consume el endpoint `POST /api/v1/facturas` con los datos de la factura.
- El sistema registra la nueva factura en la base de datos y actualiza el stock de los productos involucrados.
- El sistema confirma la creación exitosa de la factura.
- En caso de errores (cliente/producto no encontrado, stock insuficiente, datos inválidos), el sistema notifica el error.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe permitir registrar una factura asociándola a un `cliente_id` existente y una lista de `productos` con sus `cantidades`.
- [ ] El sistema debe validar que el `cliente_id` y los `producto_id` existan en la base de datos.
- [ ] El sistema debe validar que haya suficiente `cantidad` de cada producto en stock antes de registrar la factura.
- [ ] El sistema debe calcular automáticamente el `subtotal`, `descuento_porcentaje`, `descuento_valor` y `total` de la factura, aplicando la lógica de descuentos para clientes `mayoristas` [1].
- [ ] El sistema debe generar un `id` único para cada factura registrada.
- [ ] El sistema debe confirmar cuando la factura fue registrada exitosamente.
- [ ] El sistema debe mostrar un mensaje de error claro si el cliente o algún producto no existe, si el stock es insuficiente o si los datos son inválidos.
- [ ] Solo usuarios autenticados (con roles de `administrador` o `vendedor`) pueden registrar facturas.

### 2. 📆 Estructura de la información
- [ ] La solicitud `POST` para registrar una factura debe incluir `cliente_id` y una lista de `productos` (con `producto_id` y `cantidad`) en formato JSON.
- [ ] La respuesta exitosa (código `201 Created`) debe incluir el `id` de la factura, detalles del `cliente`, `productos` facturados, `subtotal`, `descuento_porcentaje`, `descuento_valor`, `total`, `estado` y `fecha` de la factura, y un `mensaje` de éxito.
- [ ] La respuesta de error por datos inválidos (código `400 Bad Request`) debe incluir un `mensaje` descriptivo (ej. stock insuficiente, cantidad inválida).
- [ ] La respuesta de error por cliente o producto no encontrado (código `404 Not Found`) debe incluir un `mensaje` descriptivo.

## 🔧 Notas Técnicas
- La lógica de registro de facturas, incluyendo la validación de existencia de cliente/productos, cálculo de totales, aplicación de descuentos y actualización de stock, debe residir en la capa de servicio (`Service Layer`) [2].
- La operación de registro de factura y actualización de stock debe ser una **transacción atómica** en la base de datos para garantizar la consistencia de los datos (ACID).
- La autenticación del usuario debe ser verificada mediante el JWT proporcionado en el encabezado de la solicitud, y se debe validar que el rol del usuario tenga permisos para acceder a esta funcionalidad.

## 🚀 Endpoint – Registrar Factura
- **Método HTTP:** `POST`
- **Ruta:** `/api/v1/facturas` (propuesto)

## 📤 Ejemplo de Estructura JSON

### Request (lo que se envía)
```json
{
  "cliente_id": 1,
  "productos": [
    {
      "producto_id": 101,
      "cantidad": 5
    },
    {
      "producto_id": 102,
      "cantidad": 2
    }
  ]
}
```

### Response exitoso (201 Created)
```json
{
  "codigo": 201,
  "id_factura": 12345,
  "cliente": {
    "id": 1,
    "nombre": "María López",
    "tipo_cliente": "mayorista"
  },
  "productos": [
    {
      "id": 101,
      "nombre": "Jabón líquido",
      "cantidad": 5,
      "precio_unitario": 5000
    },
    {
      "id": 102,
      "nombre": "Desinfectante",
      "cantidad": 2,
      "precio_unitario": 8000
    }
  ],
  "subtotal": 41000,
  "descuento_porcentaje": 10,
  "descuento_valor": 4100,
  "total": 36900,
  "estado": "pendiente",
  "fecha": "2026-05-30",
  "mensaje": "Factura registrada exitosamente"
}
```

### Response error (400 Bad Request)
```json
{
  "codigo": 400,
  "mensaje": "Stock insuficiente para el producto: Jabón líquido"
}
```

### Response error (404 Not Found)
```json
{
  "codigo": 404,
  "mensaje": "Cliente no encontrado con ID: 999"
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
  "mensaje": "Usuario no autorizado para registrar facturas"
}
```

### Response error (500 Internal Server Error)
```json
{
  "codigo": 500,
  "mensaje": "Error interno del servidor al registrar la factura"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Registro exitoso de factura para cliente minorista
- **Precondición:** Existe `cliente_id: 1` (minorista). Existen `producto_id: 101` (stock 10) y `producto_id: 102` (stock 5).
- **Acción:** Enviar `POST` a `/api/v1/facturas` con `cliente_id: 1`, `productos: [{producto_id: 101, cantidad: 2}, {producto_id: 102, cantidad: 1}]`.
- **Resultado esperado:**
  - Código HTTP `201 Created`.
  - Respuesta JSON con `id_factura`, `total` calculado sin descuento, `estado: "pendiente"` y `mensaje: "Factura registrada exitosamente"`.
  - Stock de `producto_id: 101` se reduce a 8, `producto_id: 102` a 4.

### ✅ Caso 2: Registro exitoso de factura para cliente mayorista con descuento
- **Precondición:** Existe `cliente_id: 2` (mayorista con 10% de descuento). Existen `producto_id: 103` (stock 20) y `producto_id: 104` (stock 15).
- **Acción:** Enviar `POST` a `/api/v1/facturas` con `cliente_id: 2`, `productos: [{producto_id: 103, cantidad: 10}, {producto_id: 104, cantidad: 5}]`.
- **Resultado esperado:**
  - Código HTTP `201 Created`.
  - Respuesta JSON con `id_factura`, `total` calculado con 10% de descuento, `estado: "pendiente"` y `mensaje: "Factura registrada exitosamente"`.
  - Stock de `producto_id: 103` se reduce a 10, `producto_id: 104` a 10.

### ❌ Caso 3: Intento de registrar factura con stock insuficiente
- **Precondición:** Existe `cliente_id: 1`. Existe `producto_id: 101` con stock actual de 3.
- **Acción:** Enviar `POST` a `/api/v1/facturas` con `cliente_id: 1`, `productos: [{producto_id: 101, cantidad: 5}]`.
- **Resultado esperado:**
  - Código HTTP `400 Bad Request`.
  - Respuesta JSON con `mensaje`: "Stock insuficiente para el producto: [Nombre del producto]".
  - No se registra la factura y el stock no se modifica.

### ❌ Caso 4: Intento de registrar factura con cliente inexistente
- **Precondición:** No existe `cliente_id: 999`.
- **Acción:** Enviar `POST` a `/api/v1/facturas` con `cliente_id: 999`, `productos: [{producto_id: 101, cantidad: 1}]`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - Respuesta JSON con `mensaje`: "Cliente no encontrado con ID: 999".
  - No se registra la factura.

### ❌ Caso 5: Intento de registrar factura con producto inexistente
- **Precondición:** Existe `cliente_id: 1`. No existe `producto_id: 999`.
- **Acción:** Enviar `POST` a `/api/v1/facturas` con `cliente_id: 1`, `productos: [{producto_id: 999, cantidad: 1}]`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - Respuesta JSON con `mensaje`: "Producto no encontrado con ID: 999".
  - No se registra la factura.

### ❌ Caso 6: Intento de registrar factura sin autenticación
- **Precondición:** El usuario no está autenticado.
- **Acción:** Enviar `POST` a `/api/v1/facturas` con datos válidos sin un token de autenticación.
- **Resultado esperado:**
  - Código HTTP `401 Unauthorized`.
  - Respuesta JSON con `mensaje`: "Usuario no autenticado".

### ❌ Caso 7: Intento de registrar factura por usuario no autorizado (ej. cliente final)
- **Precondición:** El usuario está autenticado como `mayorista`.
- **Acción:** Enviar `POST` a `/api/v1/facturas` con datos válidos.
- **Resultado esperado:**
  - Código HTTP `403 Forbidden`.
  - Respuesta JSON con `mensaje`: "Usuario no autorizado para registrar facturas".

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema permite el registro de facturas asociadas a clientes y productos.
- [ ] El sistema valida la existencia de clientes y productos, y la disponibilidad de stock.
- [ ] El sistema calcula automáticamente subtotales, descuentos y totales, aplicando la lógica de descuentos por tipo de cliente.
- [ ] El sistema actualiza el stock de productos tras el registro de una factura.
- [ ] El sistema maneja correctamente los casos de errores de validación y acceso no autorizado.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la lógica de cálculo de factura, aplicación de descuentos y actualización de stock.
- [ ] Se cubrieron los casos de registro exitoso de facturas para clientes minoristas y mayoristas.
- [ ] Se cubrieron los casos de error por stock insuficiente, cliente/producto inexistente, datos inválidos y usuarios no autorizados.
- [ ] Las pruebas funcionales para el endpoint de registro de facturas están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de registro de facturas está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Campos de entrada y salida (modelos JSON).
  - Ejemplos de respuestas exitosas y de error.
- [ ] La estructura de la tabla `facturas` y su relación con `clientes` y `productos` está documentada.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `400 Bad Request` para datos inválidos o stock insuficiente.
- [ ] Se devuelve código HTTP `401 Unauthorized` si el usuario no está autenticado.
- [ ] Se devuelve código HTTP `403 Forbidden` si el usuario autenticado no tiene permisos para registrar facturas.
- [ ] Se devuelve código HTTP `404 Not Found` si el cliente o algún producto no existe.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] HU-XXX_Aplicar_Descuento_v2.md - Sección "Tabla de descuentos por volumen"
[2] API Layer.txt - Sección "Service Layer"
