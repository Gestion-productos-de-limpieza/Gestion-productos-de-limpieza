# Historia de Usuario: Aplicar Descuento

## Descripción
**Como** sistema de ventas,
**quiero** aplicar descuentos automáticamente a los clientes mayoristas,
**para** incentivar las compras por volumen y fidelizar a los clientes.

## Criterios de aceptación
- El sistema debe aplicar descuento automáticamente si el cliente es mayorista.
- El descuento debe calcularse según el volumen de compra del cliente.
- El sistema debe mostrar el descuento aplicado en la factura.
- El sistema no debe aplicar descuento a clientes minoristas.
- El sistema debe confirmar el descuento aplicado exitosamente.

## Tabla de descuentos por volumen

| Compra mínima | Descuento |
|---------------|-----------|
| $50.000       | 10%       |
| $100.000      | 15%       |
| $200.000      | 20%       |
| $500.000      | 25%       |

## Estructura JSON

### Request (lo que se envía)
```json
{
  "cliente_id": 1,
  "subtotal": 200000
}
```

### Response exitoso (200)
```json
{
  "codigo": 200,
  "cliente": "María López",
  "tipo_cliente": "mayorista",
  "subtotal": 200000,
  "descuento_porcentaje": 20,
  "descuento_valor": 40000,
  "total": 160000,
  "mensaje": "Descuento aplicado exitosamente"
}
```

### Response error (400)
```json
{
  "codigo": 400,
  "mensaje": "El cliente no aplica para descuento"
}
```

### Response error (404)
```json
{
  "codigo": 404,
  "mensaje": "El cliente no existe en el sistema"
}
```

## Códigos de respuesta
| Código | Descripción |
|--------|-------------|
| 200 | Descuento aplicado exitosamente |
| 400 | Cliente no aplica para descuento |
| 401 | Usuario no autenticado |
| 404 | Cliente no encontrado |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Registrar cliente
- Registrar factura
- Definir roles
- Iniciar sesión