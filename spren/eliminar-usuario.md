# HU-09: Eliminar Usuario

## 📖 Historia de Usuario
Como **administrador del sistema**,
Quiero **eliminar usuarios registrados en el sistema**,
Para **revocar el acceso de usuarios que ya no deben tener permisos**.

## 🔁 Flujo Esperado
- El administrador autenticado selecciona un usuario existente para eliminarlo, proporcionando su `id`.
- El sistema solicita una confirmación al administrador antes de proceder con la eliminación.
- El sistema verifica que el `id` del usuario a eliminar no corresponda al `id` del administrador activo que realiza la operación.
- El sistema verifica que el usuario con el `id` proporcionado exista en la base de datos.
- Si el usuario existe y no es el administrador activo, el sistema procede a eliminarlo de la base de datos.
- El sistema confirma la eliminación exitosa del usuario.
- Si el usuario a eliminar no existe, el sistema notifica al administrador.
- Si el administrador intenta eliminarse a sí mismo, el sistema impide la acción y notifica el error.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe permitir al administrador seleccionar un usuario existente por su `id` para eliminarlo.
- [ ] El sistema debe requerir una confirmación explícita antes de ejecutar la eliminación del usuario.
- [ ] El sistema debe confirmar cuando el usuario fue eliminado exitosamente.
- [ ] El sistema **no debe permitir eliminar el propio usuario administrador activo** que realiza la operación.
- [ ] El sistema debe mostrar un mensaje de error claro si el usuario a eliminar no existe.

### 2. 📆 Estructura de la información
- [ ] La solicitud para eliminar un usuario debe incluir el `id` del usuario en el path o cuerpo de la solicitud.
- [ ] La respuesta exitosa (código `200 OK`) debe incluir un `mensaje` de confirmación.
- [ ] La respuesta de error por usuario no encontrado (código `404 Not Found`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por intentar eliminar el propio usuario activo (código `403 Forbidden`) debe incluir un `mensaje` descriptivo.

## 🔧 Notas Técnicas
- La lógica de eliminación de usuarios, incluyendo la verificación de identidad del administrador activo y la existencia del usuario, debe residir en la capa de servicio (`Service Layer`) [2].
- Se debe implementar un mecanismo de confirmación (ej. un diálogo en la UI o un parámetro `confirm=true` en la API) para evitar eliminaciones accidentales.
- La eliminación de un usuario podría implicar la eliminación en cascada de registros asociados (ej. facturas, pedidos) o la anonimización de datos, lo cual debe ser manejado por la lógica de negocio y las políticas de privacidad.

## 🚀 Endpoint – Eliminar Usuario
- **Método HTTP:** `DELETE`
- **Ruta:** `/api/v1/users/{id}` (propuesto)

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
  "mensaje": "Usuario eliminado exitosamente"
}
```

### Response error (404 Not Found)
```json
{
  "codigo": 404,
  "mensaje": "El usuario no existe"
}
```

### Response error (403 Forbidden)
```json
{
  "codigo": 403,
  "mensaje": "No puedes eliminar tu propio usuario activo"
}
```

### Response error (500 Internal Server Error)
```json
{
  "codigo": 500,
  "mensaje": "Error interno del servidor al intentar eliminar el usuario"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Eliminación exitosa de un usuario
- **Precondición:** Existe un usuario con `id: 5` (no es el administrador activo).
- **Acción:** El administrador activo (ej. `id: 1`) envía una solicitud `DELETE` a `/api/v1/users/5`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene `mensaje`: "Usuario eliminado exitosamente".
  - El usuario con `id: 5` ya no existe en la base de datos.

### ❌ Caso 2: Intento de eliminar el propio usuario administrador activo
- **Precondición:** El administrador activo tiene `id: 1`.
- **Acción:** El administrador activo envía una solicitud `DELETE` a `/api/v1/users/1`.
- **Resultado esperado:**
  - Código HTTP `403 Forbidden`.
  - La respuesta JSON contiene `mensaje`: "No puedes eliminar tu propio usuario activo".
  - El usuario con `id: 1` persiste en la base de datos.

### ❌ Caso 3: Intento de eliminar un usuario inexistente
- **Precondición:** No existe un usuario con `id: 999` en el sistema.
- **Acción:** El administrador activo envía una solicitud `DELETE` a `/api/v1/users/999`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - La respuesta JSON contiene `mensaje`: "El usuario no existe".

### ❌ Caso 4: Error interno del servidor durante la eliminación
- **Precondición:** Existe un usuario con `id: 6` (no es el administrador activo), pero la base de datos no está disponible o ocurre un error inesperado.
- **Acción:** El administrador activo envía una solicitud `DELETE` a `/api/v1/users/6` bajo condiciones simuladas de fallo de BD.
- **Resultado esperado:**
  - Código HTTP `500 Internal Server Error`.
  - La respuesta JSON contiene `mensaje`: "Error interno del servidor al intentar eliminar el usuario".
  - El usuario con `id: 6` persiste en la base de datos.

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema permite la eliminación de usuarios por su `id`.
- [ ] El sistema valida que el usuario a eliminar no sea el administrador activo.
- [ ] El sistema maneja correctamente los casos de usuarios no encontrados.
- [ ] El sistema proporciona retroalimentación clara sobre el éxito o fracaso de la operación.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la lógica de verificación de identidad del administrador activo y existencia del usuario.
- [ ] Se cubrieron los casos de eliminación exitosa de usuarios.
- [ ] Se cubrieron los casos de error por intentar eliminar el propio usuario activo o usuarios inexistentes.
- [ ] Las pruebas funcionales para el endpoint de eliminación de usuarios están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de eliminación de usuarios está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Parámetros de entrada (`id`).
  - Ejemplos de respuestas exitosas y de error.
- [ ] La estructura de la tabla `usuarios` en la base de datos está documentada.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `403 Forbidden` cuando se intenta eliminar el propio usuario activo.
- [ ] Se devuelve código HTTP `404 Not Found` cuando el usuario no existe.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] ENTREGABLE WEB SERVICE (1).pdf - Sección "1. API del Módulo de Usuarios"
[2] API Layer.txt - Sección "Service Layer"
