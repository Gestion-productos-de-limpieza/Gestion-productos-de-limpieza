# Historia de Usuario: Listar Facturas

## Descripción
**Como** administrador del sistema,
**quiero** listar todas las facturas registradas en el sistema,
**para** consultar y gestionar el historial de compras realizadas.

## Criterios de aceptación
- El sistema debe mostrar todas las facturas registradas con sus detalles.
- El sistema debe permitir filtrar facturas por fecha, cliente o estado.
- El sistema debe mostrar el descuento aplicado si el cliente es mayorista.
- El sistema debe mostrar un mensaje si no hay facturas registradas.
- Solo usuarios autenticados pueden listar las facturas.

## Estructura JSON

### Response exitoso (200)
```json
{
  "codigo": 200,
  "facturas": [
    {
      "id": 1,
      "cliente": "Juan Pérez",
      "tipo_cliente": "mayorista",
      "productos": [
        {
          "id": 1,
          "nombre": "Jabón líquido",
          "cantidad": 10,
          "precio_unitario": 5000
        }
      ],
      "subtotal": 50000,
      "descuento_porcentaje": 15,
      "descuento_valor": 7500,
      "total": 42500,
      "estado": "pendiente",
      "fecha": "2026-04-28"
    }
  ]
}
```

### Response error (404)
```json
{
  "codigo": 404,
  "mensaje": "No hay facturas registradas"
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
| 200 | Facturas listadas exitosamente |
| 401 | Usuario no autenticado |
| 404 | No hay facturas registradas |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Iniciar sesión
- Registrar factura
- Registrar cliente
- Definir roles