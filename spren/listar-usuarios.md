# Historia de Usuario: Listar Usuarios

## Descripción
**Como** administrador del sistema,
**quiero** listar todos los usuarios registrados en el sistema,
**para** gestionar y controlar el acceso de cada usuario según su rol.

## Criterios de aceptación
- El sistema debe mostrar todos los usuarios registrados con sus detalles.
- El sistema debe permitir filtrar usuarios por rol (administrador, operador, vendedor, mayorista).
- El sistema debe mostrar el estado del usuario (activo/inactivo).
- El sistema debe mostrar un mensaje si no hay usuarios registrados.
- Solo el administrador autenticado puede listar los usuarios.

## Estructura JSON

### Response exitoso (200)
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

### Response error (404)
```json
{
  "codigo": 404,
  "mensaje": "No hay usuarios registrados"
}
```

### Response error (401)
```json
{
  "codigo": 401,
  "mensaje": "Usuario no autenticado"
}
```

## Códigos de respuesta
| Código | Descripción |
|--------|-------------|
| 200 | Usuarios listados exitosamente |
| 401 | Usuario no autenticado |
| 403 | No tiene permisos para listar usuarios |
| 404 | No hay usuarios registrados |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Definir roles
- Registrar usuario
- Iniciar sesión