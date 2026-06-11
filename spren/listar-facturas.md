# HU-07: Listar Facturas

## 📖 Historia de Usuario
Como **administrador del sistema**,
Quiero **listar todas las facturas registradas en el sistema**,
Para **consultar y gestionar el historial de compras realizadas**.

## 🔁 Flujo Esperado
- El administrador autenticado accede a la sección de facturas del sistema.
- El sistema realiza una consulta a la base de datos para obtener las facturas, aplicando filtros si se especifican (fecha, cliente, estado).
- Para cada factura, el sistema recupera sus detalles, incluyendo información del cliente (tipo de cliente) y los productos asociados.
- Si el cliente es `mayorista`, el sistema calcula y muestra el descuento aplicado.
- El sistema presenta la lista de facturas al administrador.
- Si no hay facturas registradas o no se encuentran resultados con los filtros aplicados, el sistema muestra un mensaje informativo.
- Si el usuario no está autenticado, el sistema deniega el acceso.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe mostrar todas las facturas registradas con sus detalles completos (id, cliente, productos, subtotal, descuento, total, estado, fecha).
- [ ] El sistema debe permitir filtrar facturas por `fecha` (rango o específica), `cliente` (por ID o nombre) o `estado` (ej. "pendiente", "pagada", "cancelada").
- [ ] El sistema debe mostrar el `descuento_porcentaje` y `descuento_valor` aplicado si el cliente asociado a la factura es `mayorista` [1].
- [ ] El sistema debe mostrar un mensaje claro si no hay facturas registradas o si la búsqueda no arroja resultados.
- [ ] Solo usuarios autenticados pueden listar las facturas.

### 2. 📆 Estructura de la información
- [ ] La solicitud para listar facturas puede incluir parámetros de consulta para filtros (ej. `?fecha_inicio=YYYY-MM-DD&fecha_fin=YYYY-MM-DD`, `?cliente_id=X`, `?estado=Y`).
- [ ] La respuesta exitosa (código `200 OK`) debe incluir una lista de objetos `facturas`, cada uno con la estructura detallada en el ejemplo JSON.
- [ ] La respuesta de error por no haber facturas registradas (código `404 Not Found`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por usuario no autenticado (código `401 Unauthorized`) debe incluir un `mensaje` descriptivo.

## 🔧 Notas Técnicas
- La lógica de listado y filtrado de facturas debe residir en la capa de servicio (`Service Layer`) [2].
- La consulta a la base de datos debe ser eficiente, utilizando índices adecuados para los campos de filtro (fecha, cliente_id, estado).
- La información del cliente y los productos debe ser obtenida de sus respectivos módulos o tablas, posiblemente mediante joins o consultas separadas optimizadas.
- La autenticación del usuario debe ser verificada mediante el JWT proporcionado en el encabezado de la solicitud.

## 🚀 Endpoint – Listar Facturas
- **Método HTTP:** `GET`
- **Ruta:** `/api/v1/facturas` (propuesto)

## 📤 Ejemplo de Estructura JSON

### Response exitoso (200 OK)
```json
{
  "codigo": 200,
  "facturas": [
    {
      "id": 1,
      "cliente": "Juan Pérez",
      "tipo_cliente": "mayorista",
      "productos": [
        {
          "id": 1,
          "nombre": "Jabón líquido",
          "cantidad": 10,
          "precio_unitario": 5000
        }
      ],
      "subtotal": 50000,
      "descuento_porcentaje": 15,
      "descuento_valor": 7500,
      "total": 42500,
      "estado": "pendiente",
      "fecha": "2026-04-28"
    },
    {
      "id": 2,
      "cliente": "María López",
      "tipo_cliente": "minorista",
      "productos": [
        {
          "id": 2,
          "nombre": "Detergente en polvo",
          "cantidad": 2,
          "precio_unitario": 15000
        }
      ],
      "subtotal": 30000,
      "descuento_porcentaje": 0,
      "descuento_valor": 0,
      "total": 30000,
      "estado": "pagada",
      "fecha": "2026-04-27"
    }
  ]
}
```

### Response error (404 Not Found)
```json
{
  "codigo": 404,
  "mensaje": "No hay facturas registradas"
}
```

### Response error (401 Unauthorized)
```json
{
  "codigo": 401,
  "mensaje": "Usuario no autenticado"
}
```

### Response error (500 Internal Server Error)
```json
{
  "codigo": 500,
  "mensaje": "Error interno del servidor al listar facturas"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Listar todas las facturas sin filtros (usuario autenticado)
- **Precondición:** Existen múltiples facturas registradas en el sistema. El usuario está autenticado como administrador.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/facturas`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene una lista de todas las facturas, incluyendo detalles de cliente, productos y descuentos aplicados (si corresponden).

### ✅ Caso 2: Listar facturas filtradas por fecha (usuario autenticado)
- **Precondición:** Existen facturas registradas en un rango de fechas específico. El usuario está autenticado como administrador.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/facturas?fecha_inicio=2026-04-01&fecha_fin=2026-04-30`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene solo las facturas dentro del rango de fechas especificado.

### ✅ Caso 3: Listar facturas filtradas por cliente (usuario autenticado)
- **Precondición:** Existen facturas asociadas a un `cliente_id` específico. El usuario está autenticado como administrador.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/facturas?cliente_id=1`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene solo las facturas asociadas al `cliente_id: 1`.

### ✅ Caso 4: Listar facturas filtradas por estado (usuario autenticado)
- **Precondición:** Existen facturas con diferentes estados. El usuario está autenticado como administrador.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/facturas?estado=pagada`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene solo las facturas con `estado: "pagada"`.

### ❌ Caso 5: Intento de listar facturas sin autenticación
- **Precondición:** El usuario no está autenticado.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/facturas` sin un token de autenticación.
- **Resultado esperado:**
  - Código HTTP `401 Unauthorized`.
  - La respuesta JSON contiene `mensaje`: "Usuario no autenticado".

### ❌ Caso 6: No hay facturas registradas (usuario autenticado)
- **Precondición:** No existen facturas en el sistema. El usuario está autenticado como administrador.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/facturas`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - La respuesta JSON contiene `mensaje`: "No hay facturas registradas".

### ❌ Caso 7: No hay facturas que coincidan con los filtros (usuario autenticado)
- **Precondición:** Existen facturas, pero ninguna coincide con los filtros aplicados (ej. fecha futura). El usuario está autenticado como administrador.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/facturas?fecha_inicio=2030-01-01`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - La respuesta JSON contiene `mensaje`: "No hay facturas registradas" (o "No se encontraron facturas con los filtros aplicados").

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema permite listar todas las facturas con sus detalles completos.
- [ ] El sistema soporta el filtrado de facturas por `fecha`, `cliente` y `estado`.
- [ ] El sistema muestra correctamente los descuentos aplicados a clientes `mayoristas`.
- [ ] El sistema maneja los casos donde no hay facturas o no se encuentran resultados con los filtros.
- [ ] El acceso al listado de facturas está protegido por autenticación.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la lógica de filtrado y la recuperación de detalles de factura.
- [ ] Se cubrieron los casos de listado exitoso con y sin filtros.
- [ ] Se cubrieron los casos de error por falta de autenticación y ausencia de facturas.
- [ ] Las pruebas funcionales para el endpoint de listado de facturas están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de listado de facturas está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Parámetros de consulta para filtros.
  - Ejemplos de respuestas exitosas y de error.
- [ ] La estructura de la tabla `facturas` y su relación con `clientes` y `productos` está documentada.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `401 Unauthorized` si el usuario no está autenticado.
- [ ] Se devuelve código HTTP `404 Not Found` si no hay facturas registradas o no se encuentran resultados con los filtros.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] HU-XXX_Aplicar_Descuento_v2.md - Sección "Tabla de descuentos por volumen"
[2] API Layer.txt - Sección "Service Layer"
