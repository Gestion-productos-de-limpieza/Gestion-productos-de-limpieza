HU-11: Crear Rol
📖 Historia de Usuario
Como administrador del sistema,
Quiero crear nuevos roles en el sistema,
Para controlar los permisos y accesos de cada usuario según su función.
🔁 Flujo Esperado

El administrador accede a la interfaz de gestión de roles.
El administrador introduce el nombre y la descripcion del nuevo rol.
Opcionalmente, para roles como mayorista, el administrador puede especificar un descuento_porcentaje.
El sistema valida que el nombre del rol no esté duplicado y que los campos obligatorios estén presentes.
El sistema consume el endpoint POST /api/v1/roles con los datos del nuevo rol.
El sistema crea el nuevo rol en la base de datos.
El sistema confirma la creación exitosa del rol.
En caso de que el rol ya exista o los datos sean inválidos, el sistema notifica el error.

✅ Criterios de Aceptación
1. 🔍 Estructura y lógica del servicio

 El sistema debe permitir crear roles con un nombre (UNIQUE) y una descripcion.
 El sistema debe tener por defecto los roles: administrador, operador, vendedor y mayorista.
 El rol mayorista debe poder asociarse a un descuento_porcentaje que se aplicará automáticamente según el volumen de compra.
 El sistema no debe permitir crear roles duplicados (basado en el nombre).
 El sistema debe confirmar cuando el rol fue creado exitosamente.
 El sistema debe mostrar un mensaje de error claro si el rol ya existe o si los datos son inválidos.

2. 📆 Estructura de la información

 La solicitud POST para crear un rol debe incluir nombre, descripcion y opcionalmente descuento_porcentaje en formato JSON.
 La respuesta exitosa (código 201 Created) debe incluir el id, nombre, descripcion, descuento_porcentaje (si aplica) del rol creado y un mensaje de éxito.
 La respuesta de error por rol duplicado (código 409 Conflict) debe incluir un mensaje descriptivo.
 La respuesta de error por datos inválidos (código 400 Bad Request) debe incluir un mensaje descriptivo.

🔧 Notas Técnicas

La tabla de roles (roles) debe tener una restricción de unicidad en el campo nombre.
La gestión de roles debe implementarse en la capa de servicio (Service Layer) para encapsular la lógica de negocio y validaciones.
El rol del usuario se envía en el header x-user-role para validar permisos en el endpoint.

🚀 Endpoint – Crear Rol

Método HTTP: POST
Ruta: /api/v1/roles
Header requerido: x-user-role: administrador

📤 Ejemplo de Estructura JSON
Request (lo que se envía)
json{
  "nombre": "mayorista",
  "descripcion": "Cliente con acceso a descuentos por volumen de compra",
  "descuento_porcentaje": 15
}
Response exitoso (201 Created)
json{
  "codigo": 201,
  "id": 1,
  "nombre": "mayorista",
  "descripcion": "Cliente con acceso a descuentos por volumen de compra",
  "descuento_porcentaje": 15,
  "mensaje": "Rol creado exitosamente"
}
Response error (409 Conflict)
json{
  "codigo": 409,
  "mensaje": "El rol ya existe en el sistema"
}
Response error (400 Bad Request)
json{
  "codigo": 400,
  "mensaje": "Datos inválidos o campos vacíos: [Detalle del campo]"
}
Response error (422 Unprocessable Entity)
json{
  "detail": [
    {
      "loc": ["body", "nombre"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
Response error (500 Internal Server Error)
json{
  "codigo": 500,
  "mensaje": "Error interno del servidor al crear el rol"
}
🧪 Requisitos de Pruebas
🔍 Casos de Prueba Funcional
✅ Caso 1: Creación exitosa de un nuevo rol

Precondición: No existe un rol con el nombre "Gerente" en el sistema.
Acción: Enviar una solicitud POST a /api/v1/roles con el header x-user-role: administrador y el siguiente cuerpo JSON:

json  {
    "nombre": "Gerente",
    "descripcion": "Rol con permisos de gestión y supervisión"
  }

Resultado esperado:

Código HTTP 201 Created.
La respuesta JSON contiene el id, nombre, descripcion del rol creado y mensaje: "Rol creado exitosamente".



✅ Caso 2: Creación exitosa del rol "mayorista" con porcentaje de descuento

Precondición: No existe un rol con el nombre "mayorista" en el sistema.
Acción: Enviar una solicitud POST a /api/v1/roles con el header x-user-role: administrador y el siguiente cuerpo JSON:

json  {
    "nombre": "mayorista",
    "descripcion": "Cliente con acceso a descuentos por volumen de compra",
    "descuento_porcentaje": 10
  }

Resultado esperado:

Código HTTP 201 Created.
La respuesta JSON contiene descuento_porcentaje: 10 y mensaje: "Rol creado exitosamente".



❌ Caso 3: Intento de crear un rol con nombre duplicado

Precondición: Ya existe un rol con el nombre "administrador" en el sistema.
Acción: Enviar una solicitud POST a /api/v1/roles con nombre: "administrador".
Resultado esperado:

Código HTTP 409 Conflict.
La respuesta JSON contiene mensaje: "El rol ya existe en el sistema".



❌ Caso 4: Intento de crear un rol con campos obligatorios faltantes

Acción: Enviar una solicitud POST a /api/v1/roles sin el campo nombre.
Resultado esperado:

Código HTTP 422 Unprocessable Entity.
La respuesta JSON contiene el detalle del campo faltante.



❌ Caso 5: Error interno del servidor al crear el rol

Precondición: La base de datos no está disponible o ocurre un error inesperado.
Resultado esperado:

Código HTTP 500 Internal Server Error.
La respuesta JSON contiene mensaje: "Error interno del servidor al crear el rol".



✅ Definición de Hecho
📦 Alcance Funcional

 El sistema permite la creación de nuevos roles con nombre y descripcion.
 El sistema valida la unicidad del nombre del rol.
 El sistema puede asociar un descuento_porcentaje a roles específicos como mayorista.
 El sistema maneja correctamente los casos de roles duplicados y datos inválidos.

🧪 Pruebas Completadas

 Se ejecutaron pruebas unitarias para la validación de la unicidad del nombre del rol.
 Se cubrieron los casos de creación exitosa de roles, incluyendo el rol mayorista con descuento.
 Se cubrieron los casos de error por rol duplicado y campos faltantes/inválidos.
 Las pruebas funcionales para el endpoint de creación de roles están documentadas y pasadas.

📄 Documentación Técnica

 El endpoint de creación de roles está documentado en Swagger / OpenAPI.
 Se describe:

Propósito del endpoint.
Header requerido x-user-role.
Campos de entrada y salida (modelos JSON).
Ejemplos de respuestas exitosas y de error.


 La estructura de la tabla roles en la base de datos está documentada.

🔐 Manejo de Errores

 Se devuelve código HTTP 400 Bad Request para datos inválidos o campos vacíos.
 Se devuelve código HTTP 409 Conflict cuando se intenta crear un rol con un nombre ya existente.
 Se devuelve código HTTP 422 Unprocessable Entity para errores de validación de estructura JSON.
 Se devuelve código HTTP 500 Internal Server Error para errores inesperados del servidor.
 El campo mensaje en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

Referencias
[1] HU-XXX_Aplicar_Descuento_v2.md - Sección "Tabla de descuentos por volumen"
[2] API Layer.txt - Sección "Service L