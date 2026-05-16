# Historia de Usuario: Crear Tablas en Base de Datos

## Descripción
**Como** desarrollador del sistema,
**quiero** crear las tablas necesarias en la base de datos,
**para** almacenar y gestionar la información del sistema correctamente.

## Criterios de aceptación
- El sistema debe crear la tabla de usuarios con sus campos requeridos.
- El sistema debe crear la tabla de roles con sus campos requeridos.
- El sistema debe crear la tabla de facturas con sus campos requeridos.
- El sistema debe crear la tabla de productos con sus campos requeridos.
- Las tablas deben tener correctamente definidas sus llaves primarias y foráneas.
- El sistema debe confirmar cuando las tablas fueron creadas exitosamente.

## Estructura JSON

### Response exitoso (201)
```json
{
  "codigo": 201,
  "mensaje": "Tablas creadas exitosamente",
  "tablas": [
    "usuarios",
    "roles",
    "facturas",
    "productos"
  ]
}
```

### Response error (500)
```json
{
  "codigo": 500,
  "mensaje": "Error al crear las tablas en la base de datos"
}
```

## Códigos de respuesta
| Código | Descripción |
|--------|-------------|
| 201 | Tablas creadas exitosamente |
| 500 | Error interno del servidor |

## Dependencias
- No tiene dependencias, es la base de todo el sistema