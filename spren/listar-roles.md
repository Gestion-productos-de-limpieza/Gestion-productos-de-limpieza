HU-14: Listar Roles
📖 Historia de Usuario
Como administrador del sistema,
Quiero listar los roles disponibles en el sistema,
Para conocer los roles existentes y gestionar los permisos de los usuarios.
🔁 Flujo Esperado

El administrador accede a la interfaz de gestión de roles.
El sistema consume el endpoint GET /api/v1/roles con el header x-user-role.
El sistema retorna la lista de todos los roles registrados.
En caso de que no haya roles o los datos sean inválidos, el sistema notifica el error.

✅ Criterios de Aceptación
1. 🔍 Estructura y lógica del servicio

 El sistema debe retornar todos los roles existentes en el sistema.
 El sistema debe confirmar cuando la lista fue obtenida exitosamente.
 El sistema debe mostrar un mensaje de error claro si no hay roles registrados.
 Solo el administrador autenticado puede listar los roles.

2. 📆 Estructura de la información

 La solicitud GET para listar roles debe incluir el header x-user-role para validar permisos.
 La respuesta exitosa (código 200 OK) debe retornar una lista de strings con los nombres de los roles.
 La respuesta de error por validación (código 422 Unprocessable Entity) debe incluir el detalle del error.

🔧 Notas Técnicas

La gestión de roles debe implementarse en la capa de servicio (Service Layer) para encapsular la lógica de negocio.
El rol del usuario se envía en el header x-user-role para validar permisos en el endpoint.

🚀 Endpoint – Listar Roles

Método HTTP: GET
Ruta: /api/v1/roles
Header requerido: x-user-role: administrador

📤 Ejemplo de Estructura JSON
Response exitoso (200 OK)
json[
  "administrador",
  "operador",
  "vendedor",
  "mayorista"
]
Response error (422 Unprocessable Entity)
json{
  "detail": [
    {
      "loc": ["header", "x-user-role"],
      "msg": "field required",
      "type": "value_error.missing",
      "input": "string",
      "ctx": {}
    }
  ]
}
Response error (500 Internal Server Error)
json{
  "codigo": 500,
  "mensaje": "Error interno del servidor al listar los roles"
}
🧪 Requisitos de Pruebas
🔍 Casos de Prueba Funcional
✅ Caso 1: Listado exitoso de roles

Precondición: Existen roles registrados en el sistema. El usuario está autenticado como administrador.
Acción: Enviar una solicitud GET a /api/v1/roles con el header x-user-role: administrador.
Resultado esperado:

Código HTTP 200 OK.
La respuesta JSON contiene la lista de nombres de roles registrados.



❌ Caso 2: Intento de listar roles sin el header requerido

Precondición: El usuario no envía el header x-user-role.
Acción: Enviar una solicitud GET a /api/v1/roles sin el header.
Resultado esperado:

Código HTTP 422 Unprocessable Entity.
La respuesta JSON contiene el detalle del campo faltante.



❌ Caso 3: Error interno del servidor al listar roles

Precondición: La base de datos no está disponible o ocurre un error inesperado.
Acción: Enviar una solicitud GET a /api/v1/roles bajo condiciones simuladas de fallo.
Resultado esperado:

Código HTTP 500 Internal Server Error.
La respuesta JSON contiene mensaje: "Error interno del servidor al listar los roles".



✅ Definición de Hecho
📦 Alcance Funcional

 El sistema permite listar todos los roles existentes.
 El sistema valida el header x-user-role para controlar el acceso.
 El sistema maneja correctamente los casos de errores de validación y errores internos.

🧪 Pruebas Completadas

 Se ejecutaron pruebas unitarias para la validación del header y el listado de roles.
 Se cubrieron los casos de listado exitoso de roles.
 Se cubrieron los casos de error por header faltante y errores internos.
 Las pruebas funcionales para el endpoint de listado de roles están documentadas y pasadas.

📄 Documentación Técnica

 El endpoint de listado de roles está documentado en Swagger / OpenAPI.
 Se describe:

Propósito del endpoint.
Header requerido x-user-role.
Campos de salida (modelos JSON).
Ejemplos de respuestas exitosas y de error.



🔐 Manejo de Errores

 Se devuelve código HTTP 422 Unprocessable Entity para errores de validación del header.
 Se devuelve código HTTP 500 Internal Server Error para errores inesperados del servidor.
 El campo mensaje en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

Referencias
[1] API Layer.txt - Sección "Service Layer"