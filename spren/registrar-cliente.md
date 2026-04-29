# Historia de Usuario: Registrar Cliente

## Descripción
**Como** administrador o vendedor del sistema,
**quiero** registrar nuevos clientes en el sistema,
**para** gestionar sus compras y aplicar descuentos según su tipo
(mayorista o minorista).

## Criterios de aceptación
- El sistema debe permitir ingresar nombre, correo, teléfono y tipo de cliente.
- El tipo de cliente debe ser mayorista o minorista.
- El sistema debe validar que el correo no esté registrado previamente.
- El sistema debe confirmar cuando el cliente fue registrado exitosamente.
- El sistema debe mostrar un mensaje de error si algún campo obligatorio está vacío.
- Solo usuarios autenticados pueden registrar clientes.

## Estructura JSON

### Request (lo que se envía)
```json
{
  "nombre": "María López",
  "correo": "maria@email.com",
  "telefono": "3001234567",
  "tipo_cliente": "mayorista"
}
```

### Response exitoso (201)
```json
{
  "codigo": 201,
  "cliente": {
    "id": 1,
    "nombre": "María López",
    "correo": "maria@email.com",
    "telefono": "3001234567",
    "tipo_cliente": "mayorista",
    "descuento_porcentaje": 15
  },
  "mensaje": "Cliente registrado exitosamente"
}
```

### Response error (409)
```json
{
  "codigo": 409,
  "mensaje": "El correo ya está registrado en el sistema"
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
| 201 | Cliente registrado exitosamente |
| 400 | Datos inválidos o campos vacíos |
| 401 | Usuario no autenticado |
| 409 | El correo ya está registrado |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Iniciar sesión
- Definir roles