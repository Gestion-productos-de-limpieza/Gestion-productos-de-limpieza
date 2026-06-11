HU-12: Obtener Producto
📖 Historia de Usuario
Como administrador del sistema,
Quiero obtener la información de un producto específico por su ID,
Para consultar sus detalles sin necesidad de listar todos los productos.
🔁 Flujo Esperado

El administrador proporciona el ID del producto que desea consultar.
El sistema busca el producto en la base de datos por su ID.
Si el producto existe, el sistema retorna su información completa.
Si el producto no existe, el sistema notifica al administrador.

✅ Criterios de Aceptación
1. 🔍 Estructura y lógica del servicio

 Se expone un endpoint GET con parámetro id en el path.
 Se valida que el ID recibido corresponda a un producto existente.
 La lógica de búsqueda reside en la capa de servicio.

2. 📆 Estructura de la información

 Se responde con la siguiente estructura en JSON:

json{
  "codigo": 200,
  "producto": {
    "id": 1,
    "nombre": "Jabón líquido",
    "precio": 5000.0,
    "categoria": "limpieza",
    "cantidad": 100
  },
  "success": true
}

 Si no existe el producto, el backend retorna:

json{
  "codigo": 404,
  "mensaje": "Producto con ID 999 no encontrado",
  "success": false
}
🔧 Notas Técnicas

La lógica de búsqueda debe residir en la capa de servicio (Service Layer).
El endpoint debe ser de solo lectura, sin modificar datos.

🚀 Endpoint — Obtener Producto

Método HTTP: GET
Ruta: /productos/{id}

📤 Ejemplo de Respuesta JSON
json{
  "codigo": 200,
  "producto": {
    "id": 1,
    "nombre": "Jabón líquido",
    "precio": 5000.0,
    "categoria": "limpieza",
    "cantidad": 100
  },
  "success": true
}
🧪 Requisitos de Pruebas
🔍 Casos de Prueba Funcional
✅ Caso 1: Obtener producto existente

Precondición: Existe un producto con id: 1 en el sistema.
Acción: Ejecutar GET /productos/1.
Resultado esperado:

Código HTTP 200 OK
La respuesta JSON contiene todos los campos del producto
El campo success es true



❌ Caso 2: Obtener producto inexistente

Precondición: No existe un producto con id: 999.
Acción: Ejecutar GET /productos/999.
Resultado esperado:

Código HTTP 404 Not Found
Campo mensaje contiene: "Producto con ID 999 no encontrado"
El campo success es false



❌ Caso 3: ID con formato inválido

Precondición: El usuario envía un ID no numérico.
Acción: Ejecutar GET /productos/abc.
Resultado esperado:

Código HTTP 422 Unprocessable Entity
Campo mensaje contiene texto descriptivo del error de validación



❌ Caso 4: Error interno del servidor

Precondición: El repositorio no está disponible.
Acción: Ejecutar GET /productos/1 bajo condiciones de fallo.
Resultado esperado:

Código HTTP 500 Internal Server Error
Campo mensaje contiene: "Error interno al obtener el producto"



✅ Definición de Hecho
📦 Alcance Funcional

 El endpoint retorna correctamente un producto por su ID
 Se maneja correctamente el caso de producto no encontrado
 La respuesta JSON cumple con el contrato definido

🧪 Pruebas Completadas

 Se cubrió el caso de producto existente
 Se cubrió el caso de producto inexistente
 Se cubrió el caso de ID inválido
 Las pruebas funcionales están documentadas y pasadas

📄 Documentación Técnica

 Endpoint documentado en Swagger / OpenAPI
 Se describe:

Propósito del endpoint
Parámetro de entrada (id)
Ejemplo de respuesta exitosa
Ejemplo de error



🔐 Manejo de Errores

 Se devuelve código HTTP 404 cuando el producto no existe
 Se devuelve código HTTP 422 cuando el ID tiene formato inválido
 Se devuelve código HTTP 500 para errores inesperados del servidor
 El campo mensaje incluye texto claro y descriptivoHU-XXX: Obtener Producto
📖 Historia de Usuario
Como administrador del sistema,
Quiero obtener la información de un producto específico por su ID,
Para consultar sus detalles sin necesidad de listar todos los productos.
🔁 Flujo Esperado

El administrador proporciona el ID del producto que desea consultar.
El sistema busca el producto en la base de datos por su ID.
Si el producto existe, el sistema retorna su información completa.
Si el producto no existe, el sistema notifica al administrador.

✅ Criterios de Aceptación
1. 🔍 Estructura y lógica del servicio

 Se expone un endpoint GET con parámetro id en el path.
 Se valida que el ID recibido corresponda a un producto existente.
 La lógica de búsqueda reside en la capa de servicio.

2. 📆 Estructura de la información

 Se responde con la siguiente estructura en JSON:

json{
  "codigo": 200,
  "producto": {
    "id": 1,
    "nombre": "Jabón líquido",
    "precio": 5000.0,
    "categoria": "limpieza",
    "cantidad": 100
  },
  "success": true
}

 Si no existe el producto, el backend retorna:

json{
  "codigo": 404,
  "mensaje": "Producto con ID 999 no encontrado",
  "success": false
}
🔧 Notas Técnicas

La lógica de búsqueda debe residir en la capa de servicio (Service Layer).
El endpoint debe ser de solo lectura, sin modificar datos.

🚀 Endpoint — Obtener Producto

Método HTTP: GET
Ruta: /productos/{id}

📤 Ejemplo de Respuesta JSON
json{
  "codigo": 200,
  "producto": {
    "id": 1,
    "nombre": "Jabón líquido",
    "precio": 5000.0,
    "categoria": "limpieza",
    "cantidad": 100
  },
  "success": true
}
🧪 Requisitos de Pruebas
🔍 Casos de Prueba Funcional
✅ Caso 1: Obtener producto existente

Precondición: Existe un producto con id: 1 en el sistema.
Acción: Ejecutar GET /productos/1.
Resultado esperado:

Código HTTP 200 OK
La respuesta JSON contiene todos los campos del producto
El campo success es true



❌ Caso 2: Obtener producto inexistente

Precondición: No existe un producto con id: 999.
Acción: Ejecutar GET /productos/999.
Resultado esperado:

Código HTTP 404 Not Found
Campo mensaje contiene: "Producto con ID 999 no encontrado"
El campo success es false



❌ Caso 3: ID con formato inválido

Precondición: El usuario envía un ID no numérico.
Acción: Ejecutar GET /productos/abc.
Resultado esperado:

Código HTTP 422 Unprocessable Entity
Campo mensaje contiene texto descriptivo del error de validación



❌ Caso 4: Error interno del servidor

Precondición: El repositorio no está disponible.
Acción: Ejecutar GET /productos/1 bajo condiciones de fallo.
Resultado esperado:

Código HTTP 500 Internal Server Error
Campo mensaje contiene: "Error interno al obtener el producto"



✅ Definición de Hecho
📦 Alcance Funcional

 El endpoint retorna correctamente un producto por su ID
 Se maneja correctamente el caso de producto no encontrado
 La respuesta JSON cumple con el contrato definido

🧪 Pruebas Completadas

 Se cubrió el caso de producto existente
 Se cubrió el caso de producto inexistente
 Se cubrió el caso de ID inválido
 Las pruebas funcionales están documentadas y pasadas

📄 Documentación Técnica

 Endpoint documentado en Swagger / OpenAPI
 Se describe:

Propósito del endpoint
Parámetro de entrada (id)
Ejemplo de respuesta exitosa
Ejemplo de error



🔐 Manejo de Errores

 Se devuelve código HTTP 404 cuando el producto no existe
 Se devuelve código HTTP 422 cuando el ID tiene formato inválido
 Se devuelve código HTTP 500 para errores inesperados del servidor
 El campo mensaje incluye texto claro y descriptivo