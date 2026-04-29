# Historia de Usuario: Eliminar Usuario

## Descripción
**Como** administrador del sistema,
**quiero** eliminar usuarios registrados en el sistema,
**para** revocar el acceso de usuarios que ya no deben tener permisos.

## Criterios de aceptación
- El administrador debe poder seleccionar un usuario existente para eliminarlo.
- El sistema debe pedir confirmación antes de eliminar el usuario.
- El sistema debe confirmar cuando el usuario fue eliminado exitosamente.
- El sistema no debe permitir eliminar el propio usuario administrador activo.
- El sistema debe mostrar un mensaje de error si el usuario a eliminar no existe.

## Estructura JSON

### Request (lo que se envía)
```json
{
  "id": 1
}
```

### Response exitoso (200)
```json
{
  "codigo": 200,
  "mensaje": "Usuario eliminado exitosamente"
}
```

### Response error (404)
```json
{
  "codigo": 404,
  "mensaje": "El usuario no existe"
}
```

### Response error (403)
```json
{
  "codigo": 403,
  "mensaje": "No puedes eliminar tu propio usuario activo"
}
```

## Códigos de respuesta
| Código | Descripción |
|--------|-------------|
| 200 | Usuario eliminado exitosamente |
| 403 | No se puede eliminar el usuario activo |
| 404 | Usuario no encontrado |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Registrar usuario
- Listar usuarios
- Iniciar sesión