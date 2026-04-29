# Historia de Usuario: Eliminar Factura

## Descripción
**Como** administrador del sistema,
**quiero** eliminar facturas registradas en el sistema,
**para** mantener la base de datos limpia y libre de registros incorrectos o innecesarios.

## Criterios de aceptación
- El administrador debe poder seleccionar una factura existente para eliminarla.
- El sistema debe pedir confirmación antes de eliminar la factura.
- El sistema debe confirmar cuando la factura fue eliminada exitosamente.
- El sistema no debe permitir eliminar una factura que ya fue pagada.
- El sistema debe mostrar un mensaje de error si la factura a eliminar no existe.

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
  "mensaje": "Factura eliminada exitosamente"
}
```

### Response error (404)
```json
{
  "codigo": 404,
  "mensaje": "La factura no existe"
}
```

### Response error (403)
```json
{
  "codigo": 403,
  "mensaje": "No se puede eliminar una factura ya pagada"
}
```

## Códigos de respuesta
| Código | Descripción |
|--------|-------------|
| 200 | Factura eliminada exitosamente |
| 403 | No se puede eliminar una factura pagada |
| 404 | Factura no encontrada |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Registrar factura
- Listar facturas
- Iniciar sesión