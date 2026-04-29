# Historia de Usuario: Registrar Usuario

## Descripción
**Como** administrador del sistema,
**quiero** registrar nuevos usuarios asignándoles un rol específico,
**para** controlar y gestionar el acceso al sistema.

## Criterios de aceptación
- El sistema debe permitir ingresar nombre, correo y contraseña del usuario.
- El administrador debe poder asignar un rol al usuario (ej: administrador, operador, vendedor).
- El sistema debe validar que el correo no esté registrado previamente.
- El sistema debe confirmar cuando el usuario fue registrado exitosamente.
- El sistema debe mostrar un mensaje de error si algún campo obligatorio está vacío.

## Estructura JSON

### Request (lo que se envía)
```json
{
  "nombre": "Juan Pérez",
  "correo": "juan@email.com",
  "contraseña": "12345678",
  "rol": "operador"
}
```

### Response exitoso (201)
```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "correo": "juan@email.com",
  "rol": "operador",
  "mensaje": "Usuario registrado exitosamente"
}
```

### Response error (409)
```json
{
  "codigo": 409,
  "mensaje": "El correo ya está registrado"
}
```

## Códigos de respuesta
| Código | Descripción |
|--------|-------------|
| 201 | Usuario registrado exitosamente |
| 400 | Datos inválidos o campos vacíos |
| 409 | El correo ya está registrado |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Definir roles
