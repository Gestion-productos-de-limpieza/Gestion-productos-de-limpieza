# HU-XXX: Aplicar Descuento

## 📖 Historia de Usuario
Como **sistema de ventas**,
Quiero **aplicar descuentos automáticamente a los clientes mayoristas**,
Para **incentivar las compras por volumen y fidelizar a los clientes**.

## 🔁 Flujo Esperado
- El sistema recibe una solicitud para calcular el total de una venta, incluyendo el `cliente_id` y el `subtotal`.
- El sistema verifica el `tipo_cliente` asociado al `cliente_id`.
- Si el cliente es `mayorista`, el sistema evalúa el `subtotal` de la compra.
- El sistema consulta la tabla de descuentos por volumen para determinar el porcentaje de descuento aplicable.
- El sistema calcula el `descuento_valor` y el `total` final de la compra.
- El sistema genera una respuesta con los detalles del descuento aplicado.
- Si el cliente es `minorista` o no cumple con el `subtotal` mínimo, el sistema no aplica descuento y notifica al usuario.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe identificar si un cliente es `mayorista` o `minorista`.
- [ ] El sistema debe aplicar descuentos automáticamente solo a clientes `mayoristas`.
- [ ] El descuento debe calcularse según el `subtotal` de la compra del cliente, basándose en la tabla de descuentos por volumen [1].
- [ ] El sistema no debe aplicar descuento a clientes `minoristas`.
- [ ] El sistema debe confirmar el descuento aplicado exitosamente en la respuesta.

### 2. 📆 Estructura de la información
- [ ] La solicitud para aplicar descuento debe incluir `cliente_id` y `subtotal` en formato JSON.
- [ ] La respuesta exitosa (código `200 OK`) debe incluir `cliente`, `tipo_cliente`, `subtotal`, `descuento_porcentaje`, `descuento_valor`, `total` y `mensaje`.
- [ ] La respuesta de error por cliente no aplicable (código `400 Bad Request`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por cliente no encontrado (código `404 Not Found`) debe incluir un `mensaje` descriptivo.

## Tabla de descuentos por volumen

| Compra mínima | Descuento |
|---------------|-----------|
| $50.000       | 10%       |
| $100.000      | 15%       |
| $200.000      | 20%       |
| $500.000      | 25%       |

## 🔧 Notas Técnicas
- La lógica de aplicación de descuentos debe residir en la capa de servicio (`Service Layer`) para mantener la separación de responsabilidades [2].
- El `subtotal` debe ser un valor numérico (`float` o `int`) para permitir cálculos precisos.
- La identificación del `tipo_cliente` puede requerir una consulta al módulo de usuarios o a la base de datos de clientes.

## 🚀 Endpoint – Aplicar Descuento
- **Método HTTP:** `POST`
- **Ruta:** `/api/v1/sales/apply-discount` (propuesto)

## 📤 Ejemplo de Estructura JSON

### Request (lo que se envía)
```json
{
  "cliente_id": 1,
  "subtotal": 200000
}
```

### Response exitoso (200 OK)
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

### Response error (400 Bad Request)
```json
{
  "codigo": 400,
  "mensaje": "El cliente no aplica para descuento"
}
```

### Response error (404 Not Found)
```json
{
  "codigo": 404,
  "mensaje": "El cliente no existe en el sistema"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Aplicar 10% de descuento a cliente mayorista con compra de $50.000
- **Precondición:** Cliente 1 es `mayorista`. `subtotal` = $50.000.
- **Acción:** Enviar `POST` a `/api/v1/sales/apply-discount` con `cliente_id: 1`, `subtotal: 50000`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - `descuento_porcentaje`: 10.
  - `descuento_valor`: 5000.
  - `total`: 45000.
  - `mensaje`: "Descuento aplicado exitosamente".

### ✅ Caso 2: Aplicar 15% de descuento a cliente mayorista con compra de $100.000
- **Precondición:** Cliente 2 es `mayorista`. `subtotal` = $100.000.
- **Acción:** Enviar `POST` a `/api/v1/sales/apply-discount` con `cliente_id: 2`, `subtotal: 100000`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - `descuento_porcentaje`: 15.
  - `descuento_valor`: 15000.
  - `total`: 85000.
  - `mensaje`: "Descuento aplicado exitosamente".

### ✅ Caso 3: Aplicar 25% de descuento a cliente mayorista con compra de $500.000
- **Precondición:** Cliente 3 es `mayorista`. `subtotal` = $500.000.
- **Acción:** Enviar `POST` a `/api/v1/sales/apply-discount` con `cliente_id: 3`, `subtotal: 500000`.
- **Resultado esperado:**
  - Código HTTP `200 OK`.
  - `descuento_porcentaje`: 25.
  - `descuento_valor`: 125000.
  - `total`: 375000.
  - `mensaje`: "Descuento aplicado exitosamente".

### ❌ Caso 4: Cliente minorista no aplica para descuento
- **Precondición:** Cliente 4 es `minorista`.
- **Acción:** Enviar `POST` a `/api/v1/sales/apply-discount` con `cliente_id: 4`, `subtotal: 150000`.
- **Resultado esperado:**
  - Código HTTP `400 Bad Request`.
  - `mensaje`: "El cliente no aplica para descuento".

### ❌ Caso 5: Cliente mayorista con compra inferior a $50.000
- **Precondición:** Cliente 5 es `mayorista`. `subtotal` = $40.000.
- **Acción:** Enviar `POST` a `/api/v1/sales/apply-discount` con `cliente_id: 5`, `subtotal: 40000`.
- **Resultado esperado:**
  - Código HTTP `400 Bad Request`.
  - `mensaje`: "El cliente no aplica para descuento" (o similar, indicando que no cumple el mínimo).

### ❌ Caso 6: Cliente no existente
- **Precondición:** No existe el `cliente_id: 999` en el sistema.
- **Acción:** Enviar `POST` a `/api/v1/sales/apply-discount` con `cliente_id: 999`, `subtotal: 100000`.
- **Resultado esperado:**
  - Código HTTP `404 Not Found`.
  - `mensaje`: "El cliente no existe en el sistema".

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema puede identificar el tipo de cliente (`mayorista`/`minorista`).
- [ ] El sistema calcula el descuento correctamente según el `subtotal` y la tabla de descuentos.
- [ ] El sistema genera una respuesta JSON con los detalles del descuento o el motivo de no aplicación.
- [ ] El sistema maneja los casos de clientes no existentes o no elegibles para descuento.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la lógica de cálculo de descuentos.
- [ ] Se cubrieron los casos de aplicación de descuento para diferentes volúmenes de compra.
- [ ] Se cubrieron los casos de no aplicación de descuento (cliente minorista, compra mínima no alcanzada).
- [ ] Se cubrieron los casos de error (cliente no existente).
- [ ] Las pruebas funcionales para el endpoint de aplicación de descuento están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de aplicación de descuento está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Campos de entrada y salida (modelos JSON).
  - Ejemplos de respuestas exitosas y de error.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `400 Bad Request` cuando el cliente no aplica para descuento o el `subtotal` es inválido.
- [ ] Se devuelve código HTTP `404 Not Found` cuando el `cliente_id` no existe.
- [ ] Se devuelve código HTTP `401 Unauthorized` si se requiere autenticación y el usuario no está autenticado.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] Tabla de descuentos por volumen (proporcionada en la descripción de la HU).
[2] API Layer.txt - Sección "Service Layer"
