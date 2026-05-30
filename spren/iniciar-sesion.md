# HU-XXX: Iniciar Sesión

## 📖 Historia de Usuario
Como **usuario del sistema**,
Quiero **iniciar sesión con mis credenciales**,
Para **acceder al sistema según mi rol asignado**.

## 🔁 Flujo Esperado
- El usuario accede a la interfaz de inicio de sesión.
- El usuario introduce su `correo` y `contraseña`.
- El sistema recibe las credenciales y las valida contra la base de datos (verificando el hash de la contraseña).
- Si las credenciales son correctas, el sistema genera un **Token Web JSON (JWT)** de acceso.
- El sistema consulta el `rol` asignado al usuario.
- El sistema devuelve el JWT y la información básica del usuario, incluyendo su `rol`.
- El sistema redirige al usuario a la interfaz correspondiente a su `rol` (ej. panel de administrador, vista de cliente).
- Si las credenciales son incorrectas o el usuario no está registrado, el sistema muestra un mensaje de error.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe permitir ingresar `correo` y `contraseña` para iniciar sesión.
- [ ] El sistema debe validar que el `correo` y la `contraseña` sean correctos (comparando el hash de la contraseña ingresada con el almacenado).
- [ ] El sistema debe generar un **Token Web JSON (JWT)** al iniciar sesión exitosamente, que contenga información del usuario (ej. `id`, `rol`).
- [ ] El sistema debe redirigir al usuario a la interfaz adecuada según su `rol` (administrador, operador, vendedor, mayorista).
- [ ] El sistema debe mostrar un mensaje de error claro si las credenciales son incorrectas.
- [ ] El sistema debe bloquear el acceso si el usuario no está registrado o si sus credenciales no coinciden.

### 2. 📆 Estructura de la información
- [ ] La solicitud de inicio de sesión debe incluir `correo` y `contraseña` en formato JSON.
- [ ] La respuesta exitosa (código `200 OK`) debe incluir un `token` JWT, la información del `usuario` (sin la contraseña) y un `mensaje` de éxito.
- [ ] La respuesta de error por credenciales incorrectas (código `401 Unauthorized`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por usuario no autorizado (código `403 Forbidden`) debe incluir un `mensaje` descriptivo (ej. si el rol no tiene acceso al sistema).

## 🔧 Notas Técnicas
- La autenticación y generación de JWT debe implementarse en la capa de servicio (`Service Layer`) para encapsular la lógica de seguridad [2].
- Las contraseñas deben ser almacenadas como hashes (ej. bcrypt) y nunca en texto plano. La comparación de contraseñas debe hacerse con el hash.
- El JWT debe tener un tiempo de expiración (`exp`) y puede incluir el `id` y `rol` del usuario para facilitar la autorización en futuras solicitudes.
- El endpoint de inicio de sesión debe ser público, sin requerir autenticación previa.

## 🚀 Endpoint – Iniciar Sesión
- **Método HTTP:** `POST`
- **Ruta:** `/api/v1/auth/login` (propuesto)

## 📤 Ejemplo de Estructura JSON

### Request (lo que se envía)
```json
{
  "correo": "juan@email.com",
  "contraseña": "12345678"
}
```

### Response exitoso (200 OK)
```json
{
  "codigo": 200,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "usuario": {
    "id": 1,
    "nombre": "Juan Pérez",
    "correo": "juan@email.com",
    "rol": "administrador"
  },
  "mensaje": "Inicio de sesión exitoso"
}
```

### Response error (401 Unauthorized)
```json
{
  "codigo": 401,
  "mensaje": "Correo o contraseña incorrectos"
}
```

### Response error (403 Forbidden)
```json
{
  "codigo": 403,
  "mensaje": "Usuario no autorizado para acceder al sistema"
}
```

### Response error (500 Internal Server Error)
```json
{
  "codigo": 500,
  "mensaje": "Error interno del servidor al intentar iniciar sesión"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Inicio de sesión exitoso con credenciales válidas
- **Precondición:** Existe un usuario registrado con `correo: "admin@example.com"` y `contraseña: "passwordAdmin"` (hasheada en BD), con `rol: "administrador"`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/auth/login` con `correo: "admin@example.com"` y `contraseña: "passwordAdmin"`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - La respuesta JSON contiene un `token` JWT válido y la información del `usuario` con `rol: "administrador"`.
  - El sistema está listo para redirigir al usuario al panel de administrador.

### ❌ Caso 2: Intento de inicio de sesión con contraseña incorrecta
- **Precondición:** Existe un usuario registrado con `correo: "user@example.com"` y `contraseña: "passwordCorrecta"`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/auth/login` con `correo: "user@example.com"` y `contraseña: "passwordIncorrecta"`.
- **Resultado esperado:**
  - Código HTTP `401 Unauthorized`.
  - La respuesta JSON contiene `mensaje`: "Correo o contraseña incorrectos".

### ❌ Caso 3: Intento de inicio de sesión con correo no registrado
- **Precondición:** No existe un usuario con `correo: "noregistrado@example.com"`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/auth/login` con `correo: "noregistrado@example.com"` y `contraseña: "cualquierPassword"`.
- **Resultado esperado:**
  - Código HTTP `401 Unauthorized`.
  - La respuesta JSON contiene `mensaje`: "Correo o contraseña incorrectos".

### ❌ Caso 4: Intento de inicio de sesión de usuario no autorizado (ej. rol deshabilitado)
- **Precondición:** Existe un usuario con `correo: "deshabilitado@example.com"` pero su `rol` está deshabilitado o no tiene permisos para acceder al sistema.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/auth/login` con `correo: "deshabilitado@example.com"` y `contraseña: "passwordValida"`.
- **Resultado esperado:**
  - Código HTTP `403 Forbidden`.
  - La respuesta JSON contiene `mensaje`: "Usuario no autorizado para acceder al sistema".

### ❌ Caso 5: Error interno del servidor durante el inicio de sesión
- **Precondición:** La base de datos no está disponible o ocurre un error inesperado en el servidor durante el proceso de autenticación.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/auth/login` con credenciales válidas bajo condiciones simuladas de fallo de BD.
- **Resultado esperado:**
  - Código HTTP `500 Internal Server Error`.
  - La respuesta JSON contiene `mensaje`: "Error interno del servidor al intentar iniciar sesión".

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema permite la autenticación de usuarios mediante `correo` y `contraseña`.
- [ ] El sistema genera un JWT válido tras un inicio de sesión exitoso.
- [ ] El sistema maneja correctamente los casos de credenciales incorrectas o usuarios no registrados.
- [ ] El sistema gestiona la autorización de acceso basada en el `rol` del usuario.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la validación de credenciales y el hashing de contraseñas.
- [ ] Se cubrieron los casos de inicio de sesión exitoso para diferentes roles.
- [ ] Se cubrieron los casos de error por credenciales incorrectas, usuarios no registrados y usuarios no autorizados.
- [ ] Las pruebas funcionales para el endpoint de inicio de sesión están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de inicio de sesión está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Campos de entrada (`correo`, `contraseña`).
  - Ejemplos de respuestas exitosas (con JWT) y de error.
- [ ] Se documenta el formato y la estructura del JWT generado.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `401 Unauthorized` para credenciales incorrectas o usuarios no registrados.
- [ ] Se devuelve código HTTP `403 Forbidden` para usuarios autenticados pero no autorizados a acceder al sistema.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] ENTREGABLE WEB SERVICE (1).pdf - Sección "1. API del Módulo de Usuarios"
[2] API Layer.txt - Sección "Service Layer"
