# HU-04: Registrar Cliente

## 📖 Historia de Usuario
Como **administrador o vendedor del sistema**,
Quiero **registrar nuevos clientes en el sistema**,
Para **gestionar sus compras y aplicar descuentos según su tipo (mayorista o minorista)**.

## 🔁 Flujo Esperado
- El usuario autenticado (administrador o vendedor) accede a la interfaz de registro de clientes.
- El usuario introduce el `nombre`, `correo`, `telefono` y selecciona el `tipo_cliente` (mayorista o minorista).
- El sistema valida que el `correo` no esté registrado previamente en la base de datos.
- El sistema valida que todos los campos obligatorios estén presentes y sean válidos.
- El sistema consume el endpoint `POST /api/v1/clientes` con los datos del nuevo cliente.
- El sistema registra el nuevo cliente en la base de datos, asignando un `descuento_porcentaje` inicial si es `mayorista`.
- El sistema confirma la creación exitosa del cliente.
- En caso de que el correo ya exista o los datos sean inválidos, el sistema notifica el error.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema debe permitir ingresar `nombre`, `correo` (UNIQUE), `telefono` y `tipo_cliente` (mayorista/minorista).
- [ ] El `tipo_cliente` debe ser validado para aceptar solo "mayorista" o "minorista".
- [ ] El sistema debe validar que el `correo` no esté registrado previamente.
- [ ] El sistema debe asignar automáticamente un `descuento_porcentaje` inicial al cliente si su `tipo_cliente` es "mayorista" (ej. 10% para nuevos mayoristas) [1].
- [ ] El sistema debe confirmar cuando el cliente fue registrado exitosamente.
- [ ] El sistema debe mostrar un mensaje de error claro si algún campo obligatorio está vacío o si el `correo` ya está registrado.
- [ ] Solo usuarios autenticados (con roles de `administrador` o `vendedor`) pueden registrar clientes.

### 2. 📆 Estructura de la información
- [ ] La solicitud `POST` para registrar un cliente debe incluir `nombre`, `correo`, `telefono` y `tipo_cliente` en formato JSON.
- [ ] La respuesta exitosa (código `201 Created`) debe incluir el `id`, `nombre`, `correo`, `telefono`, `tipo_cliente` y `descuento_porcentaje` (si aplica) del cliente creado, y un `mensaje` de éxito.
- [ ] La respuesta de error por correo duplicado (código `409 Conflict`) debe incluir un `mensaje` descriptivo.
- [ ] La respuesta de error por datos inválidos o campos vacíos (código `400 Bad Request`) debe incluir un `mensaje` descriptivo.

## 🔧 Notas Técnicas
- La lógica de registro de clientes, incluyendo la validación de unicidad del correo y la asignación del descuento inicial, debe residir en la capa de servicio (`Service Layer`) [2].
- La tabla de clientes (`clientes`) debe tener una restricción de unicidad en el campo `correo`.
- La autenticación del usuario debe ser verificada mediante el JWT proporcionado en el encabezado de la solicitud, y se debe validar que el rol del usuario tenga permisos para acceder a esta funcionalidad.

## 🚀 Endpoint – Registrar Cliente
- **Método HTTP:** `POST`
- **Ruta:** `/api/v1/clientes` (propuesto)

## 📤 Ejemplo de Estructura JSON

### Request (lo que se envía)
```json
{
  "nombre": "María López",
  "correo": "maria@email.com",
  "telefono": "3001234567",
  "tipo_cliente": "mayorista"
}
```

### Response exitoso (201 Created)
```json
{
  "codigo": 201,
  "cliente": {
    "id": 1,
    "nombre": "María López",
    "correo": "maria@email.com",
    "telefono": "3001234567",
    "tipo_cliente": "mayorista",
    "descuento_porcentaje": 10
  },
  "mensaje": "Cliente registrado exitosamente"
}
```

### Response error (409 Conflict)
```json
{
  "codigo": 409,
  "mensaje": "El correo ya está registrado en el sistema"
}
```

### Response error (400 Bad Request)
```json
{
  "codigo": 400,
  "mensaje": "Datos inválidos o campos vacíos: [Detalle del campo]"
}
```

### Response error (401 Unauthorized)
```json
{
  "codigo": 401,
  "mensaje": "Usuario no autenticado"
}
```

### Response error (403 Forbidden)
```json
{
  "codigo": 403,
  "mensaje": "Usuario no autorizado para registrar clientes"
}
```

### Response error (500 Internal Server Error)
```json
{
  "codigo": 500,
  "mensaje": "Error interno del servidor al registrar el cliente"
}
```

## 🧪 Requisitos de Pruebas

## 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Registro exitoso de un cliente minorista
- **Precondición:** El correo "nuevo.cliente@example.com" no está registrado. El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/clientes` con `nombre: "Nuevo Cliente"`, `correo: "nuevo.cliente@example.com"`, `telefono: "3101234567"`, `tipo_cliente: "minorista"`.
- **Resultado esperado:**
  - Código HTTP `201 Created`.
  - La respuesta JSON contiene los datos del cliente registrado con `descuento_porcentaje: 0` y `mensaje`: "Cliente registrado exitosamente".
  - El cliente es persistido en la base de datos.

### ✅ Caso 2: Registro exitoso de un cliente mayorista con descuento inicial
- **Precondición:** El correo "mayorista.nuevo@example.com" no está registrado. El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/clientes` con `nombre: "Mayorista Nuevo"`, `correo: "mayorista.nuevo@example.com"`, `telefono: "3201234567"`, `tipo_cliente: "mayorista"`.
- **Resultado esperado:**
  - Código HTTP `201 Created`.
  - La respuesta JSON contiene los datos del cliente registrado con `descuento_porcentaje: 10` (o el valor inicial configurado) y `mensaje`: "Cliente registrado exitosamente".
  - El cliente es persistido en la base de datos.

### ❌ Caso 3: Intento de registrar un cliente con correo ya existente
- **Precondición:** El correo "existente@example.com" ya está registrado en el sistema. El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/clientes` con `correo: "existente@example.com"` y otros datos válidos.
- **Resultado esperado:**
  - Código HTTP `409 Conflict`.
  - La respuesta JSON contiene `mensaje`: "El correo ya está registrado en el sistema".

### ❌ Caso 4: Intento de registrar un cliente con campos obligatorios faltantes
- **Precondición:** El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/clientes` con un cuerpo JSON incompleto (ej. sin `nombre`).
- **Resultado esperado:**
  - Código HTTP `400 Bad Request`.
  - La respuesta JSON contiene `mensaje`: "Datos inválidos o campos vacíos: [Detalle del campo faltante]".

### ❌ Caso 5: Intento de registrar un cliente con `tipo_cliente` inválido
- **Precondición:** El usuario está autenticado como `administrador` o `vendedor`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/clientes` con `tipo_cliente: "vip"` (valor no permitido).
- **Resultado esperado:**
  - Código HTTP `400 Bad Request`.
  - La respuesta JSON contiene `mensaje`: "Datos inválidos: El tipo de cliente debe ser 'mayorista' o 'minorista'".

### ❌ Caso 6: Intento de registrar un cliente sin autenticación
- **Precondición:** El usuario no está autenticado.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/clientes` con datos válidos sin un token de autenticación.
- **Resultado esperado:**
  - Código HTTP `401 Unauthorized`.
  - La respuesta JSON contiene `mensaje`: "Usuario no autenticado".

### ❌ Caso 7: Intento de registrar un cliente por usuario no autorizado (ej. cliente final)
- **Precondición:** El usuario está autenticado como `mayorista`.
- **Acción:** Enviar una solicitud `POST` a `/api/v1/clientes` con datos válidos.
- **Resultado esperado:**
  - Código HTTP `403 Forbidden`.
  - La respuesta JSON contiene `mensaje`: "Usuario no autorizado para registrar clientes".

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El sistema permite el registro de nuevos clientes con `nombre`, `correo`, `telefono` y `tipo_cliente`.
- [ ] El sistema valida la unicidad del `correo` del cliente.
- [ ] El sistema asigna un `descuento_porcentaje` inicial basado en el `tipo_cliente`.
- [ ] El sistema maneja correctamente los casos de correos duplicados, datos inválidos y accesos no autorizados.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias para la validación de campos, unicidad del correo y asignación de descuento.
- [ ] Se cubrieron los casos de registro exitoso para clientes minoristas y mayoristas.
- [ ] Se cubrieron los casos de error por correo duplicado, campos faltantes/inválidos y usuarios no autorizados.
- [ ] Las pruebas funcionales para el endpoint de registro de clientes están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] El endpoint de registro de clientes está documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint.
  - Campos de entrada y salida (modelos JSON).
  - Ejemplos de respuestas exitosas y de error.
- [ ] La estructura de la tabla `clientes` en la base de datos está documentada.

## 🔐 Manejo de Errores
- [ ] Se devuelve código HTTP `400 Bad Request` para datos inválidos o campos vacíos.
- [ ] Se devuelve código HTTP `401 Unauthorized` si el usuario no está autenticado.
- [ ] Se devuelve código HTTP `403 Forbidden` si el usuario autenticado no tiene permisos para registrar clientes.
- [ ] Se devuelve código HTTP `409 Conflict` cuando se intenta registrar un cliente con un correo ya existente.
- [ ] Se devuelve código HTTP `500 Internal Server Error` para errores inesperados del servidor.
- [ ] El campo `mensaje` en el JSON de respuesta incluye un texto amigable y claro para el usuario técnico o frontend.

## Referencias
[1] HU-XXX_Aplicar_Descuento_v2.md - Sección "Tabla de descuentos por volumen"
[2] API Layer.txt - Sección "Service Layer"
