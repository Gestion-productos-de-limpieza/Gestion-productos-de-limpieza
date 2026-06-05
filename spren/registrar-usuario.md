# HU-01: Registrar Usuario
📖 Historia de Usuario

Como Administrador o Cliente,
Quiero registrar un nuevo usuario en el sistema,
Para poder acceder a las funcionalidades correspondientes a mi rol.

🔁 Flujo Esperado

•
El usuario accede a la interfaz de registro.

•
El usuario introduce la información requerida (ej. nombre, correo electrónico, contraseña, rol).

•
El sistema valida la información proporcionada (ej. formato de email, contraseña segura, email no duplicado).

•
El sistema consume el endpoint POST /api/v1/users con los datos del nuevo usuario.

•
El sistema registra el nuevo usuario en la base de datos, almacenando la contraseña de forma segura (hasheada).

•
El sistema devuelve una confirmación de registro exitoso.

✅ Criterios de Aceptación

1. 🔍 Estructura y lógica del servicio




Se expone un endpoint POST en /api/v1/users para el registro de usuarios 
.




El sistema valida que los campos obligatorios (ej. nombre, email, password) estén presentes y sean válidos.




El sistema valida que el email proporcionado no esté ya registrado en la base de datos.




El sistema asigna un rol por defecto al nuevo usuario (ej. "cliente") si no se especifica, o valida el rol proporcionado si el registro es realizado por un administrador.

2. 📆 Estructura de la información




La solicitud POST al endpoint /api/v1/users debe incluir un cuerpo JSON con la siguiente estructura:

JSON


{
  "nombre": "Juan Pérez",
  "email": "juan.perez@example.com",
  "password": "passwordSegura123",
  "rol": "cliente" 
}






En caso de registro exitoso, el sistema responde con un código 201 Created y un cuerpo JSON similar a:

JSON


{
  "mensaje": "Usuario registrado exitosamente",
  "usuario": {
    "id": 123,
    "nombre": "Juan Pérez",
    "email": "juan.perez@example.com",
    "rol": "cliente"
  },
  "success": true
}






En caso de error de validación (ej. campos faltantes, email ya registrado, formato incorrecto), el sistema responde con un código 400 Bad Request y un cuerpo JSON con un mensaje descriptivo y "success": false.

🔧 Notas Técnicas

•
El módulo de usuarios se encarga de administrar la información de los usuarios y controlar el acceso según el rol 
.

•
La API del módulo de usuarios utiliza la base URL /api/v1/users 
.

•
La contraseña debe ser hasheada antes de su almacenamiento en la base de datos para garantizar la seguridad.

🚀 Endpoint – Registro de Usuario

•
Método HTTP: POST

•
Ruta: /api/v1/users

🧪 Requisitos de Pruebas

🔍 Casos de Prueba Funcional

✅ Caso 1: Registro exitoso de un nuevo usuario (rol cliente por defecto)

•
Precondición: No existe un usuario con el email nuevo.usuario@example.com en el sistema.

•
Acción: Enviar una solicitud POST a /api/v1/users con el siguiente cuerpo JSON:

JSON


{
  "nombre": "Nuevo Usuario",
  "email": "nuevo.usuario@example.com",
  "password": "passwordSegura456"
}





•
Resultado esperado:

•
Código HTTP 201 Created.

•
La respuesta JSON contiene un mensaje de éxito y los datos del usuario registrado, incluyendo un id generado y rol: "cliente".

•
El usuario es persistido en la base de datos con la contraseña hasheada.



✅ Caso 2: Registro exitoso de un nuevo usuario con rol específico (realizado por administrador)

•
Precondición: Un administrador autenticado está realizando la operación. No existe un usuario con el email admin.usuario@example.com.

•
Acción: Enviar una solicitud POST a /api/v1/users con el siguiente cuerpo JSON:

JSON


{
  "nombre": "Admin Usuario",
  "email": "admin.usuario@example.com",
  "password": "passwordAdmin789",
  "rol": "administrador"
}





•
Resultado esperado:

•
Código HTTP 201 Created.

•
La respuesta JSON contiene un mensaje de éxito y los datos del usuario registrado, incluyendo rol: "administrador".

•
El usuario es persistido en la base de datos con la contraseña hasheada.



❌ Caso 3: Intento de registro con email ya existente

•
Precondición: Ya existe un usuario con el email existente@example.com en el sistema.

•
Acción: Enviar una solicitud POST a /api/v1/users con el siguiente cuerpo JSON:

JSON


{
  "nombre": "Usuario Duplicado",
  "email": "existente@example.com",
  "password": "otraPassword"
}





•
Resultado esperado:

•
Código HTTP 400 Bad Request.

•
La respuesta JSON contiene un mensaje indicando que el email ya está registrado y "success": false.



❌ Caso 4: Intento de registro con campos obligatorios faltantes

•
Precondición: Ninguna.

•
Acción: Enviar una solicitud POST a /api/v1/users con un cuerpo JSON incompleto (ej. sin email):

JSON


{
  "nombre": "Usuario Incompleto",
  "password": "passwordIncompleta"
}





•
Resultado esperado:

•
Código HTTP 400 Bad Request.

•
La respuesta JSON contiene un mensaje indicando los campos faltantes o inválidos y "success": false.



❌ Caso 5: Intento de registro con formato de email inválido

•
Precondición: Ninguna.

•
Acción: Enviar una solicitud POST a /api/v1/users con un email con formato incorrecto:

JSON


{
  "nombre": "Usuario Mal Email",
  "email": "email-invalido",
  "password": "passwordValida"
}





•
Resultado esperado:

•
Código HTTP 400 Bad Request.

•
La respuesta JSON contiene un mensaje indicando que el formato del email es inválido y "success": false.



✅ Definición de Hecho

📦 Alcance Funcional




El endpoint POST /api/v1/users permite el registro de nuevos usuarios.




La información del usuario (nombre, email, rol) se almacena correctamente.




Las contraseñas se almacenan de forma segura (hasheada).




El sistema maneja correctamente los casos de email duplicado y campos faltantes/inválidos.

🧪 Pruebas Completadas




Se ejecutaron pruebas unitarias para la validación de datos del usuario (email, password, campos obligatorios).




Se cubrieron los casos de registro exitoso y fallido (email duplicado, datos inválidos).




Las pruebas funcionales para el endpoint POST /api/v1/users están documentadas y pasadas.

📄 Documentación Técnica




El endpoint de registro de usuario está documentado en Swagger / OpenAPI.




Se describe:

•
Propósito del endpoint.

•
Campos de entrada y salida (modelos JSON).

•
Ejemplo de respuesta exitosa (201 Created).

•
Ejemplos de errores (400 Bad Request).



🔐 Manejo de Errores




Se devuelve código HTTP 400 Bad Request para errores de validación de entrada.




Se devuelve código HTTP 500 Internal Server Error para errores inesperados del servidor.




El campo mensaje en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

Referencias

[[1] ENTREGABLE WEB SERVICE (1).pdf - Sección "1. API del Módulo de Usuarios"](https://github.com/orgs/Gestion-productos-de-limpieza/projects/3/views/1?pane=issue&itemId=180265468&issue=Gestion-productos-de-limpieza%7CGestion-productos-de-limpieza%7C27#)