# Historia de Usuario: Listar Productos

## Descripción
**Como** administrador o vendedor del sistema,
**quiero** listar todos los productos de limpieza registrados en el sistema,
**para** consultar el inventario disponible y gestionar las ventas.

## Criterios de aceptación
- El sistema debe mostrar todos los productos registrados con sus detalles.
- El sistema debe permitir filtrar productos por nombre o categoría.
- El sistema debe mostrar la cantidad disponible de cada producto.
- El sistema debe mostrar un mensaje si no hay productos registrados.
- Solo usuarios autenticados pueden listar los productos.

## Estructura JSON

### Response exitoso (200)
```json
{
  "codigo": 200,
  "productos": [
    {
      "id": 1,
      "nombre": "Jabón líquido",
      "descripcion": "Jabón antibacterial para manos",
      "precio": 5000,
      "cantidad": 100,
      "categoria": "limpieza personal"
    },
    {
      "id": 2,
      "nombre": "Desinfectante",
      "descripcion": "Desinfectante multiusos para superficies",
      "precio": 8000,
      "cantidad": 50,
      "categoria": "limpieza del hogar"
    }
  ]
}
```

### Response error (404)
```json
{
  "codigo": 404,
  "mensaje": "No hay productos registrados"
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
| 200 | Productos listados exitosamente |
| 401 | Usuario no autenticado |
| 404 | No hay productos registrados |
| 500 | Error interno del servidor |

## Dependencias
- Crear tablas en base de datos
- Iniciar sesión
- Registrar producto
- Definir roles