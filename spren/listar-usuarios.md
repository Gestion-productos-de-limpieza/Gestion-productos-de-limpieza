# HU-XXX: Listar Usuarios

## 📖 Historia de Usuario
Como **administrador del sistema**,
Quiero **listar todos los usuarios registrados en el sistema**,
Para **gestionar y controlar el acceso de cada usuario según su rol**.

## 🔁 Flujo Esperado
- El administrador autenticado accede a la sección de gestión de usuarios del sistema.
- El sistema realiza una consulta a la base de datos para obtener los usuarios, aplicando filtros si se especifican (por `rol`).
- Para cada usuario, el sistema recupera sus detalles, incluyendo `id`, `nombre`, `correo`, `rol` y `estado` (activo/inactivo).
- El sistema presenta la lista de usuarios al administrador.
- Si no hay usuarios registrados o no se encuentran resultados con los filtros aplicados, el sistema muestra un mensaje informativo.
- Si el usuario no está autenticado o no tiene el rol de `administrador`, el sistema deniega el acceso.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe mostrar todos los usuarios registrados con sus detalles completos (`id`, `nombre`, `correo`, `rol`, `estado`).
- [ ] El sistema debe permitir filtrar usuarios por `rol` (ej. "administrador", "operador", "vendedor", "mayorista").
- [ ] El sistema debe mostrar el `estado` del usuario (activo/inactivo).
- [ ] El sistema debe mostrar un mensaje claro si no hay usuarios registrados o si la búsqueda no arroja resultados.
- [ ] Solo el `administrador` autenticado puede listar los usuarios.

### 2. 📆 Estructura de la información
- [ ] La solicitud para listar usuarios puede incluir parámetros de consulta para filtros (ej. `?rol=mayorista`).
- [ ] La respuesta exitosa (código `200 OK`) debe incluir una lista de objetos `usuarios`, cada uno con la estructura detallada en el ejemplo JSON.
- [ ] La respuesta de error por no haber usuarios registrados (código `404 Not Found`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por usuario no autenticado (código `401 Unauthorized`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por usuario no autorizado (código `403 Forbidden`) debe incluir un `mensaje` descriptivo.

## 🔧 Notas Técnicas
- La lógica de listado y filtrado de usuarios debe residir en la capa de servicio (`Service Layer`) [2].
- La consulta a la base de datos debe ser eficiente, utilizando índices adecuados para el campo de filtro (`rol`).
- La autenticación del usuario debe ser verificada mediante el JWT proporcionado en el encabezado de la solicitud, y se debe validar que el rol del usuario sea `administrador` para acceder a esta funcionalidad.

## 🚀 Endpoint – Listar Usuarios
- **Método HTTP:** `GET`
- **Ruta:** `/api/v1/users` (propuesto)

## 📤 Ejemplo de Estructura JSON

### Response exitoso (200 OK)
```json
{
  "codigo": 200,
  "usuarios": [
    {
      "id": 1,
      "nombre": "Juan Pérez",
      "correo": "juan@email.com",
      "rol": "administrador",
      "estado": "activo"
    },
    {
      "id": 2,
      "nombre": "María López",
      "correo": "maria@email.com",
      "rol": "mayorista",
      "estado": "activo"
    }
  ]
}
```

### Response error (404 Not Found)
```json
{
  "codigo": 404,
  "mensaje": "No hay usuarios registrados"
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
  "mensaje": "No tiene permisos para listar usuarios"
}
```

### Response error (500 Internal Server Error)
```json
{
  "codigo": 500,
  "mensaje": "Error interno del servidor al listar usuarios"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Listar todos los usuarios sin filtros (administrador autenticado)
- **Precondición:** Existen múltiples usuarios registrados en el sistema. El usuario está autenticado como `administrador`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/users`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene una lista de todos los usuarios con sus detalles completos (id, nombre, correo, rol, estado).

### ✅ Caso 2: Listar usuarios filtrados por rol (administrador autenticado)
- **Precondición:** Existen usuarios con el rol "mayorista". El usuario está autenticado como `administrador`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/users?rol=mayorista`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene solo los usuarios con `rol: "mayorista"`.

### ❌ Caso 3: Intento de listar usuarios sin autenticación
- **Precondición:** El usuario no está autenticado.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/users` sin un token de autenticación.
- **Resultado esperado:**
  - Código HTTP `401 Unauthorized`.
  - La respuesta JSON contiene `mensaje`: "Usuario no autenticado".

### ❌ Caso 4: Intento de listar usuarios por usuario no autorizado (ej. vendedor)
- **Precondición:** El usuario está autenticado como `vendedor`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/users`.
- **Resultado esperado:**
  - Código HTTP `403 Forbidden`.
  - La respuesta JSON contiene `mensaje`: "No tiene permisos para listar usuarios".

### ❌ Caso 5: No hay usuarios registrados (administrador autenticado)
- **Precondición:** No existen usuarios en el sistema. El usuario está autenticado como `administrador`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/users`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - La respuesta JSON contiene `mensaje`: "No hay usuarios registrados".

### ❌ Caso 6: No hay usuarios que coincidan con el rol filtrado (administrador autenticado)
- **Precondición:** Existen usuarios, pero ninguno coincide con el rol "supervisor" (rol inexistente). El usuario está autenticado como `administrador`.
- **Acción:** Enviar una solicitud `GET` a `/api/v1/users?rol=supervisor`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - La respuesta JSON contiene `mensaje`: "No hay usuarios registrados" (o "No se encontraron usuarios con el rol especificado").

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema permite listar todos los usuarios con sus detalles completos, incluyendo su rol y estado.
- [ ] El sistema soporta el filtrado de usuarios por `rol`.
- [ ] El sistema maneja los casos donde no hay usuarios o no se encuentran resultados con los filtros.
- [ ] El acceso al listado de usuarios está protegido por autenticación y restringido al rol de `administrador`.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la lógica de filtrado y la recuperación de detalles de usuario.
- [ ] Se cubrieron los casos de listado exitoso con y sin filtros.
- [ ] Se cubrieron los casos de error por falta de autenticación, usuario no autorizado y ausencia de usuarios.
- [ ] Las pruebas funcionales para el endpoint de listado de usuarios están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de listado de usuarios está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Parámetros de consulta para filtros.
  - Ejemplos de respuestas exitosas y de error.
- [ ] La estructura de la tabla `usuarios` en la base de datos está documentada.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `401 Unauthorized` si el usuario no está autenticado.
- [ ] Se devuelve código HTTP `403 Forbidden` si el usuario autenticado no tiene permisos de `administrador` para listar usuarios.
- [ ] Se devuelve código HTTP `404 Not Found` si no hay usuarios registrados o no se encuentran resultados con los filtros.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] ENTREGABLE WEB SERVICE (1).pdf - Sección "1. API del Módulo de Usuarios"
[2] API Layer.txt - Sección "Service Layer"
