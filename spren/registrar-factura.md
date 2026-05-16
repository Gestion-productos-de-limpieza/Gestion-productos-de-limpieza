# Historia de Usuario: Registrar Factura

## Descripción
**Como** administrador o vendedor del sistema,
**quiero** registrar una nueva factura en el sistema,
**para** documentar las compras realizadas por los clientes y aplicar
descuentos automáticos a los mayoristas.

## Criterios de aceptación
- El sistema debe permitir registrar una factura con los productos comprados.
- El sistema debe asociar la factura a un cliente registrado.
- El sistema debe aplicar automáticamente el descuento si el cliente es mayorista.
- El sistema debe calcular el subtotal, descuento y total automáticamente.
- El sistema debe confirmar cuando la factura fue registrada exitosamente.
- El sistema debe mostrar un mensaje de error si el cliente no existe.
- El sistema debe mostrar un mensaje de error si algún producto no existe.

## Estructura JSON

### Request (lo que se envía)
```json
{
  "cliente_id": 2,
  "productos": [
    {
      "id": 1,
      "cantidad": 10
    },
    {
      "id": 2,
      "cantidad": 5
    }
  ]
}
```

### Response exitoso (201)
```json
{
  "codigo": 201,
  "factura": {
    "id": 1,
    "cliente": "María López",
    "tipo_cliente": "mayorista",
    "productos": [
      {
        "id": 1,
        "nombre": "Jabón líquido",
        "cantidad": 10,
        "precio_unitario": 5000
      },
      {
        "id": 2,
        "nombre": "Desinfectante",
        "cantidad": 5,
        "precio_unitario": 8000
      }
    ],
    "subtotal": 90000,
    "descuento_porcentaje": 15,
    "descuento_valor": 13500,
    "total": 76500,
    "estado": "pendiente",
    "fecha": "2026-04-28"
  },
  "mensaje": "Factura registrada exitosamente"
}
```

### Response error (404) cliente no existe
```json
{
  "codigo": 404,
  "mensaje": "El cliente no existe en el sistema"
}
```

### Response error (404) producto no existe
```json
{
  "codigo": 404,
  "mensaje": "El producto no existe en el sistema"
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
| 201 | Factura registrada exitosamente |
| 401 | Usuario no autenticado |
| 403 | No tiene permisos para registrar facturas |
| 404 | Cliente o producto no encontrado |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Iniciar sesión
- Registrar cliente
- Registrar producto
- Definir roles
- Aplicar descuento