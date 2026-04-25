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