# Historia de Usuario: Definir Roles

## Descripción
**Como** administrador del sistema,
**quiero** definir los roles disponibles en el sistema,
**para** controlar los permisos y accesos de cada usuario según su función.

## Criterios de aceptación
- El sistema debe permitir crear roles con un nombre y descripción.
- El sistema debe tener por defecto los roles: administrador, operador, vendedor y mayorista.
- El mayorista debe poder recibir descuentos automáticos según el volumen de su compra.
- El sistema no debe permitir crear roles duplicados.
- El sistema debe confirmar cuando el rol fue creado exitosamente.
- El sistema debe mostrar un mensaje de error si el rol ya existe.

## Estructura JSON

### Request (lo que se envía)
```json
{
  "nombre": "mayorista",
  "descripcion": "Cliente con acceso a descuentos por volumen de compra",
  "descuento_porcentaje": 15
}
```

### Response exitoso (201)
```json
{
  "codigo": 201,
  "id": 1,
  "nombre": "mayorista",
  "descripcion": "Cliente con acceso a descuentos por volumen de compra",
  "descuento_porcentaje": 15,
  "mensaje": "Rol creado exitosamente"
}
```

### Response error (409)
```json
{
  "codigo": 409,
  "mensaje": "El rol ya existe en el sistema"
}
```

## Códigos de respuesta
| Código | Descripción |
|--------|-------------|
| 201 | Rol creado exitosamente |
| 409 | El rol ya existe |
| 400 | Datos inválidos o campos vacíos |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos