HU-08: Eliminar Producto
📖 Historia de Usuario
Como administrador del sistema,
Quiero eliminar un producto existente del catálogo,
Para mantener el inventario limpio y libre de productos obsoletos o incorrectos.
🔁 Flujo Esperado

El administrador selecciona un producto existente proporcionando su id.
El sistema verifica que el producto exista en el sistema.
Si el producto existe, el sistema procede a eliminarlo.
El sistema confirma la eliminación exitosa del producto.
Si el producto no existe, el sistema notifica al administrador.

✅ Criterios de Aceptación
1. 🔍 Estructura y lógica del servicio

 El sistema debe permitir eliminar un producto existente por su id.
 El sistema debe validar que el producto exista antes de eliminarlo.
 El sistema debe confirmar cuando el producto fue eliminado exitosamente.
 El sistema debe mostrar un mensaje de error claro si el producto no existe.

2. 📆 Estructura de la información

 La solicitud para eliminar un producto debe incluir el id en el path.
 La respuesta exitosa (código 200 OK) debe incluir un mensaje de confirmación.
 La respuesta de error por producto no encontrado (código 404 Not Found) debe incluir un mensaje descriptivo.
 La respuesta de error por error interno (código 500) debe incluir un mensaje descriptivo.

🔧 Notas Técnicas

La lógica de eliminación debe residir en la capa de servicio (Service Layer).
La eliminación es permanente, no se implementa borrado lógico.
Solo el administrador puede eliminar productos.

🚀 Endpoint — Eliminar Producto

Método HTTP: DELETE
Ruta: /productos/{id}

📤 Ejemplo de Estructura JSON
Response exitoso (200 OK):
json{
  "codigo": 200,
  "mensaje": "Producto eliminado exitosamente",
  "success": true
}
Response error (404 Not Found):
json{
  "codigo": 404,
  "mensaje": "Producto con ID 999 no encontrado"
}
Response error (500 Internal Server Error):
json{
  "codigo": 500,
  "mensaje": "Error interno del servidor al eliminar el producto"
}
🧪 Requisitos de Pruebas
🔍 Casos de Prueba Funcional
✅ Caso 1: Eliminación exitosa de un producto existente

Precondición: Existe un producto con id: 1 en el sistema.
Acción: Enviar una solicitud DELETE a /productos/1 con header x-user-role: administrador.
Resultado esperado:

Código HTTP 200 OK
Campo mensaje contiene: "Producto eliminado exitosamente"
Campo success es true
El producto con id: 1 ya no existe en el sistema



❌ Caso 2: Intento de eliminar un producto inexistente

Precondición: No existe un producto con id: 999.
Acción: Enviar una solicitud DELETE a /productos/999 con header x-user-role: administrador.
Resultado esperado:

Código HTTP 404 Not Found
Campo mensaje contiene: "Producto con ID 999 no encontrado"



❌ Caso 3: Intento de eliminar sin autenticación

Precondición: Ninguna.
Acción: Enviar una solicitud DELETE a /productos/1 sin header x-user-role.
Resultado esperado:

Código HTTP 401 Unauthorized
Campo mensaje contiene: "Usuario no autenticado"



❌ Caso 4: Intento de eliminar sin permisos

Precondición: Ninguna.
Acción: Enviar una solicitud DELETE a /productos/1 con header x-user-role: vendedor.
Resultado esperado:

Código HTTP 403 Forbidden
Campo mensaje contiene: "No tiene permisos para eliminar productos"



❌ Caso 5: ID con formato inválido

Precondición: Ninguna.
Acción: Enviar una solicitud DELETE a /productos/abc.
Resultado esperado:

Código HTTP 422 Unprocessable Entity
Campo mensaje contiene texto descriptivo del error de validación



❌ Caso 6: Error interno del servidor

Precondición: El repositorio no está disponible.
Acción: Enviar una solicitud DELETE a /productos/1 bajo condiciones de fallo.
Resultado esperado:

Código HTTP 500 Internal Server Error
Campo mensaje contiene: "Error interno del servidor al eliminar el producto"



✅ Definición de Hecho
📦 Alcance Funcional

 El sistema permite eliminar un producto por su id
 El sistema valida que el producto exista antes de eliminarlo
 Solo el administrador puede eliminar productos
 La respuesta JSON cumple con el contrato definido

🧪 Pruebas Completadas

 Se cubrió el caso de eliminación exitosa
 Se cubrió el caso de producto inexistente
 Se cubrió el caso sin autenticación
 Se cubrió el caso sin permisos
 Se cubrió el caso de ID con formato inválido
 Las pruebas funcionales están documentadas y pasadas

📄 Documentación Técnica

 Endpoint documentado en Swagger / OpenAPI
 Se describe:

Propósito del endpoint
Parámetro de entrada (id en path)
Ejemplo de respuesta exitosa
Ejemplo de error



🔐 Manejo de Errores

 Se devuelve código HTTP 401 cuando no hay autenticación
 Se devuelve código HTTP 403 cuando no hay permisos
 Se devuelve código HTTP 404 cuando el producto no existe
 Se devuelve código HTTP 422 cuando el ID tiene formato inválido
 Se devuelve código HTTP 500 para errores inesperados del servidor
 El campo mensaje incluye texto claro y descriptivo