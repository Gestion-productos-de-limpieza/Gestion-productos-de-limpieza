# Historia de Usuario: Registrar Producto

## Descripción
**Como** administrador del sistema,
**quiero** registrar nuevos productos de limpieza en el sistema,
**para** tener un inventario actualizado de los productos disponibles para la venta.

## Criterios de aceptación
- El sistema debe permitir ingresar nombre, descripción, precio y cantidad del producto.
- El sistema debe validar que el producto no esté registrado previamente.
- El sistema debe confirmar cuando el producto fue registrado exitosamente.
- El sistema debe mostrar un mensaje de error si algún campo obligatorio está vacío.
- Solo el administrador autenticado puede registrar productos.

## Estructura JSON

### Request (lo que se envía)
```json
{
  "nombre": "Jabón líquido",
  "descripcion": "Jabón antibacterial para manos",
  "precio": 5000,
  "cantidad": 100,
  "categoria": "limpieza personal"
}
```

### Response exitoso (201)
```json
{
  "codigo": 201,
  "producto": {
    "id": 1,
    "nombre": "Jabón líquido",
    "descripcion": "Jabón antibacterial para manos",
    "precio": 5000,
    "cantidad": 100,
    "categoria": "limpieza personal"
  },
  "mensaje": "Producto registrado exitosamente"
}
```

### Response error (409)
```json
{
  "codigo": 409,
  "mensaje": "El producto ya está registrado en el sistema"
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
| 201 | Producto registrado exitosamente |
| 400 | Datos inválidos o campos vacíos |
| 401 | Usuario no autenticado |
| 409 | El producto ya existe |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Iniciar sesión
- Definir roles