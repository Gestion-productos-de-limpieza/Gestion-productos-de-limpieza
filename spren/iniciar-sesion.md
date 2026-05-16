# Historia de Usuario: Iniciar Sesión

## Descripción
**Como** usuario del sistema,
**quiero** iniciar sesión con mis credenciales,
**para** acceder al sistema según mi rol asignado.

## Criterios de aceptación
- El sistema debe permitir ingresar correo y contraseña para iniciar sesión.
- El sistema debe validar que el correo y contraseña sean correctos.
- El sistema debe generar un token de acceso al iniciar sesión exitosamente.
- El sistema debe redirigir al usuario según su rol (administrador, operador, vendedor, mayorista).
- El sistema debe mostrar un mensaje de error si las credenciales son incorrectas.
- El sistema debe bloquear el acceso si el usuario no está registrado.

## Estructura JSON

### Request (lo que se envía)
```json
{
  "correo": "juan@email.com",
  "contraseña": "12345678"
}
```

### Response exitoso (200)
```json
{
  "codigo": 200,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "usuario": {
    "id": 1,
    "nombre": "Juan Pérez",
    "correo": "juan@email.com",
    "rol": "administrador"
  },
  "mensaje": "Inicio de sesión exitoso"
}
```

### Response error (401)
```json
{
  "codigo": 401,
  "mensaje": "Correo o contraseña incorrectos"
}
```

### Response error (403)
```json
{
  "codigo": 403,
  "mensaje": "Usuario no autorizado para acceder al sistema"
}
```

## Códigos de respuesta
| Código | Descripción |
|--------|-------------|
| 200 | Inicio de sesión exitoso |
| 401 | Credenciales incorrectas |
| 403 | Usuario no autorizado |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Definir roles
- Registrar usuario