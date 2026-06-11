# HU-10: Eliminar Factura

## 📖 Historia de Usuario
Como **administrador del sistema**,
Quiero **eliminar facturas registradas en el sistema**,
Para **mantener la base de datos limpia y libre de registros incorrectos o innecesarios**.

## 🔁 Flujo Esperado
- El administrador selecciona una factura existente para eliminarla, proporcionando su `id`.
- El sistema solicita una confirmación al administrador antes de proceder con la eliminación.
- El sistema verifica el estado de pago de la factura asociada al `id` proporcionado.
- Si la factura no ha sido pagada, el sistema procede a eliminarla de la base de datos.
- El sistema confirma la eliminación exitosa de la factura.
- Si la factura ya fue pagada, el sistema impide la eliminación y notifica al administrador.
- Si la factura no existe, el sistema notifica al administrador.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe permitir al administrador seleccionar una factura existente por su `id` para eliminarla.
- [ ] El sistema debe requerir una confirmación explícita antes de ejecutar la eliminación de la factura.
- [ ] El sistema debe confirmar cuando la factura fue eliminada exitosamente.
- [ ] El sistema **no debe permitir eliminar una factura que ya fue pagada**.
- [ ] El sistema debe mostrar un mensaje de error claro si la factura a eliminar no existe.

### 2. 📆 Estructura de la información
- [ ] La solicitud para eliminar una factura debe incluir el `id` de la factura en el path o cuerpo de la solicitud.
- [ ] La respuesta exitosa (código `200 OK`) debe incluir un `mensaje` de confirmación.
- [ ] La respuesta de error por factura no encontrada (código `404 Not Found`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por factura ya pagada (código `403 Forbidden`) debe incluir un `mensaje` descriptivo.

## 🔧 Notas Técnicas
- La lógica de eliminación de facturas, incluyendo la verificación del estado de pago, debe residir en la capa de servicio (`Service Layer`) [2].
- Se debe implementar un mecanismo de confirmación (ej. un diálogo en la UI o un parámetro `confirm=true` en la API) para evitar eliminaciones accidentales.
- La eliminación de una factura podría implicar la eliminación en cascada de ítems de línea asociados o la actualización de inventario, lo cual debe ser manejado por la lógica de negocio.

## 🚀 Endpoint – Eliminar Factura
- **Método HTTP:** `DELETE`
- **Ruta:** `/api/v1/facturas/{id}` (propuesto)

## 📤 Ejemplo de Estructura JSON

### Request (lo que se envía)
```json
{
  "id": 1
}
```

### Response exitoso (200 OK)
```json
{
  "codigo": 200,
  "mensaje": "Factura eliminada exitosamente"
}
```

### Response error (404 Not Found)
```json
{
  "codigo": 404,
  "mensaje": "La factura no existe"
}
```

### Response error (403 Forbidden)
```json
{
  "codigo": 403,
  "mensaje": "No se puede eliminar una factura ya pagada"
}
```

### Response error (500 Internal Server Error)
```json
{
  "codigo": 500,
  "mensaje": "Error interno del servidor al intentar eliminar la factura"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Eliminación exitosa de una factura no pagada
- **Precondición:** Existe una factura con `id: 1` y su `estado` es "pendiente" o "no pagada".
- **Acción:** Enviar una solicitud `DELETE` a `/api/v1/facturas/1`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene `mensaje`: "Factura eliminada exitosamente".
  - La factura con `id: 1` ya no existe en la base de datos.

### ❌ Caso 2: Intento de eliminar una factura ya pagada
- **Precondición:** Existe una factura con `id: 2` y su `estado` es "pagada".
- **Acción:** Enviar una solicitud `DELETE` a `/api/v1/facturas/2`.
- **Resultado esperado:**
  - Código HTTP `403 Forbidden`.
  - La respuesta JSON contiene `mensaje`: "No se puede eliminar una factura ya pagada".
  - La factura con `id: 2` persiste en la base de datos.

### ❌ Caso 3: Intento de eliminar una factura inexistente
- **Precondición:** No existe una factura con `id: 999` en el sistema.
- **Acción:** Enviar una solicitud `DELETE` a `/api/v1/facturas/999`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - La respuesta JSON contiene `mensaje`: "La factura no existe".

### ❌ Caso 4: Error interno del servidor durante la eliminación
- **Precondición:** Existe una factura con `id: 3` y su `estado` es "pendiente", pero la base de datos no está disponible o ocurre un error inesperado.
- **Acción:** Enviar una solicitud `DELETE` a `/api/v1/facturas/3` bajo condiciones simuladas de fallo de BD.
- **Resultado esperado:**
  - Código HTTP `500 Internal Server Error`.
  - La respuesta JSON contiene `mensaje`: "Error interno del servidor al intentar eliminar la factura".
  - La factura con `id: 3` persiste en la base de datos (o su estado no se modifica).

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema permite la eliminación de facturas por su `id`.
- [ ] El sistema valida el estado de pago de la factura antes de eliminarla.
- [ ] El sistema maneja correctamente los casos de facturas no encontradas o ya pagadas.
- [ ] El sistema proporciona retroalimentación clara sobre el éxito o fracaso de la operación.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la lógica de verificación del estado de pago y eliminación.
- [ ] Se cubrieron los casos de eliminación exitosa de facturas no pagadas.
- [ ] Se cubrieron los casos de error por intentar eliminar facturas pagadas o inexistentes.
- [ ] Las pruebas funcionales para el endpoint de eliminación de facturas están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de eliminación de facturas está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Parámetros de entrada (`id`).
  - Ejemplos de respuestas exitosas y de error.
- [ ] La estructura de la tabla `facturas` en la base de datos está documentada, incluyendo el campo `estado`.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `403 Forbidden` cuando se intenta eliminar una factura ya pagada.
- [ ] Se devuelve código HTTP `404 Not Found` cuando la factura no existe.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] ENTREGABLE WEB SERVICE (1).pdf - Sección "6. API del Módulo de Facturación"
[2] API Layer.txt - Sección "Service Layer"
