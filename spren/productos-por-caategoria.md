HU-15: Listar Productos por Categoría
📖 Historia de Usuario
Como administrador o vendedor del sistema,
Quiero filtrar productos por su categoría,
Para consultar rápidamente los productos de una línea específica sin listar todo el catálogo.
🔁 Flujo Esperado

El usuario proporciona el nombre de la categoría que desea consultar.
El sistema busca todos los productos que pertenecen a esa categoría.
Si existen productos, el sistema retorna la lista filtrada.
Si no existen productos en esa categoría, el sistema notifica al usuario.
Si la categoría tiene formato inválido, el sistema notifica al usuario.

✅ Criterios de Aceptación
1. 🔍 Estructura y lógica del servicio

 El sistema debe exponer un endpoint GET con parámetro categoria en el path.
 El sistema debe validar que la categoría recibida tenga productos asociados.
 La lógica de filtrado debe residir en la capa de servicio (Service Layer).
 El sistema debe confirmar cuando la consulta fue exitosa.
 El sistema debe mostrar un mensaje de error claro si no hay productos en la categoría.

2. 📆 Estructura de la información

 La solicitud debe incluir el nombre de la categoria en el path.
 La respuesta exitosa (código 200 OK) debe incluir la lista de productos filtrados y un mensaje de confirmación.
 La respuesta de error por categoría sin productos (código 404 Not Found) debe incluir un mensaje descriptivo.
 La respuesta de error por datos inválidos (código 400 Bad Request) debe incluir un mensaje descriptivo.

🔧 Notas Técnicas

La lógica de filtrado debe residir en la capa de servicio (Service Layer).
El filtro por categoría debe ser insensible a mayúsculas y minúsculas.
El parámetro categoria va en el path de la URL.

🚀 Endpoint — Listar Productos por Categoría

Método HTTP: GET
Ruta: /productos/categoria/{categoria}

📤 Ejemplo de Estructura JSON
Response exitoso (200 OK):
json{
  "codigo": 200,
  "categoria": "limpieza",
  "productos": [
    {
      "id": 1,
      "nombre": "Jabón líquido",
      "precio": 5000.0,
      "categoria": "limpieza",
      "cantidad": 100
    },
    {
      "id": 3,
      "nombre": "Desengrasante",
      "precio": 8000.0,
      "categoria": "limpieza",
      "cantidad": 50
    }
  ],
  "success": true
}
Response error (404 Not Found):
json{
  "codigo": 404,
  "mensaje": "No existen productos para la categoría: desinfectante",
  "success": false
}
Response error (500 Internal Server Error):
json{
  "codigo": 500,
  "mensaje": "Error interno del servidor al consultar productos por categoría"
}
🧪 Requisitos de Pruebas
🔍 Casos de Prueba Funcional
✅ Caso 1: Consulta exitosa de productos por categoría existente

Precondición: Existen productos con categoría "limpieza" en el sistema.
Acción: Ejecutar GET /productos/categoria/limpieza.
Resultado esperado:

Código HTTP 200 OK
La respuesta JSON contiene la lista de productos de categoría "limpieza"
Campo success es true



✅ Caso 2: Consulta insensible a mayúsculas

Precondición: Existen productos con categoría "limpieza" en el sistema.
Acción: Ejecutar GET /productos/categoria/LIMPIEZA.
Resultado esperado:

Código HTTP 200 OK
La respuesta retorna los mismos productos que con "limpieza" en minúsculas



❌ Caso 3: Consulta de categoría sin productos

Precondición: No existen productos con categoría "desinfectante".
Acción: Ejecutar GET /productos/categoria/desinfectante.
Resultado esperado:

Código HTTP 404 Not Found
Campo mensaje contiene: "No existen productos para la categoría: desinfectante"
Campo success es false



❌ Caso 4: Consulta sin autenticación

Precondición: Ninguna.
Acción: Ejecutar GET /productos/categoria/limpieza sin header x-user-role.
Resultado esperado:

Código HTTP 401 Unauthorized
Campo mensaje contiene: "Usuario no autenticado"



❌ Caso 5: Error interno del servidor

Precondición: El repositorio no está disponible.
Acción: Ejecutar GET /productos/categoria/limpieza bajo condiciones de fallo.
Resultado esperado:

Código HTTP 500 Internal Server Error
Campo mensaje contiene: "Error interno del servidor al consultar productos por categoría"



✅ Definición de Hecho
📦 Alcance Funcional

 El endpoint retorna correctamente productos filtrados por categoría
 El filtro es insensible a mayúsculas y minúsculas
 Se maneja correctamente el caso de categoría sin productos
 La respuesta JSON cumple con el contrato definido

🧪 Pruebas Completadas

 Se cubrió el caso de consulta exitosa
 Se cubrió el caso de insensibilidad a mayúsculas
 Se cubrió el caso de categoría sin productos
 Se cubrió el caso sin autenticación
 Las pruebas funcionales están documentadas y pasadas

📄 Documentación Técnica

 Endpoint documentado en Swagger / OpenAPI
 Se describe:

Propósito del endpoint
Parámetro de entrada (categoria en path)
Ejemplo de respuesta exitosa
Ejemplo de error



🔐 Manejo de Errores

 Se devuelve código HTTP 401 cuando no hay autenticación
 Se devuelve código HTTP 404 cuando no hay productos en la categoría
 Se devuelve código HTTP 500 para errores inesperados del servidor
 El campo mensaje incluye texto claro y descriptivo