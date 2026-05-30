HU-XXX: Crear Tablas en Base de Datos

📖 Historia de Usuario

Como desarrollador del sistema,
Quiero crear las tablas necesarias en la base de datos,
Para almacenar y gestionar la información del sistema correctamente.

🔁 Flujo Esperado

•
El desarrollador ejecuta un script de inicialización o una migración de base de datos.

•
El sistema intenta conectarse a la base de datos configurada.

•
El sistema verifica la existencia de las tablas usuarios, roles, facturas y productos.

•
Si las tablas no existen, el sistema procede a crearlas con sus respectivas estructuras, llaves primarias y foráneas.

•
El sistema confirma la creación exitosa de todas las tablas.

•
En caso de error (ej. conexión fallida, permisos insuficientes), el sistema registra el error y notifica la falla.

✅ Criterios de Aceptación

1. 🔍 Estructura y lógica del servicio




El sistema debe crear la tabla usuarios con campos como id (PK), nombre, email (UNIQUE), password_hash, rol_id (FK a roles).




El sistema debe crear la tabla roles con campos como id (PK), nombre_rol (UNIQUE).




El sistema debe crear la tabla productos con campos como id (PK), nombre, descripcion, precio, stock, categoria.




El sistema debe crear la tabla facturas con campos como id (PK), usuario_id (FK a usuarios), fecha, total, estado.




Todas las tablas deben tener correctamente definidas sus llaves primarias (PK) y foráneas (FK) para asegurar la integridad referencial.




El sistema debe confirmar explícitamente cuando las tablas fueron creadas exitosamente.

2. 📆 Estructura de la información




En caso de creación exitosa, el sistema responde con un código 201 Created y un cuerpo JSON que lista las tablas creadas.




En caso de error, el sistema responde con un código 500 Internal Server Error y un cuerpo JSON con un mensaje descriptivo del problema.

🔧 Notas Técnicas

•
Se recomienda el uso de un sistema de migración de base de datos (ej. Alembic para SQLAlchemy, Flyway para Java) para gestionar la creación y evolución del esquema de la base de datos de forma controlada.

•
Las contraseñas de los usuarios deben almacenarse como hashes (ej. password_hash) y no en texto plano.

•
La definición precisa de los tipos de datos para cada campo (ej. VARCHAR, INT, FLOAT, BOOLEAN, DATETIME) debe ser especificada en el script de creación o migración.

🚀 Endpoint – Inicialización de Base de Datos (Opcional, para entornos de desarrollo/administración)

•
Método HTTP: POST

•
Ruta: /api/v1/admin/init-db (propuesto, con autenticación de administrador)

📤 Ejemplo de Estructura JSON

Response exitoso (201 Created)

JSON


{
  "codigo": 201,
  "mensaje": "Tablas creadas exitosamente",
  "tablas": [
    "usuarios",
    "roles",
    "productos",
    "facturas"
  ]
}



Response error (500 Internal Server Error)

JSON


{
  "codigo": 500,
  "mensaje": "Error al crear las tablas en la base de datos: [Detalle del error técnico]"
}



🧪 Requisitos de Pruebas

🔍 Casos de Prueba Funcional

✅ Caso 1: Creación exitosa de todas las tablas en una base de datos vacía

•
Precondición: La base de datos está accesible y vacía (no contiene las tablas del sistema).

•
Acción: Ejecutar el script de inicialización de la base de datos o llamar al endpoint /api/v1/admin/init-db.

•
Resultado esperado:

•
Código HTTP 201 Created (si es un endpoint) o mensaje de éxito en la consola.

•
La respuesta JSON lista todas las tablas creadas (usuarios, roles, productos, facturas).

•
Verificación en la base de datos de que todas las tablas existen con sus esquemas correctos (PKs y FKs).



❌ Caso 2: Error de conexión a la base de datos

•
Precondición: La base de datos no está disponible o las credenciales de conexión son incorrectas.

•
Acción: Ejecutar el script de inicialización de la base de datos o llamar al endpoint /api/v1/admin/init-db.

•
Resultado esperado:

•
Código HTTP 500 Internal Server Error (si es un endpoint) o error en la consola.

•
La respuesta JSON contiene un mensaje indicando un error de conexión a la base de datos.

•
Ninguna tabla del sistema ha sido creada o modificada.



❌ Caso 3: Permisos insuficientes para crear tablas

•
Precondición: La base de datos está accesible, pero el usuario de la base de datos no tiene permisos para crear tablas.

•
Acción: Ejecutar el script de inicialización de la base de datos o llamar al endpoint /api/v1/admin/init-db.

•
Resultado esperado:

•
Código HTTP 500 Internal Server Error (si es un endpoint) o error en la consola.

•
La respuesta JSON contiene un mensaje indicando un error de permisos.

•
Ninguna tabla del sistema ha sido creada o modificada.



❌ Caso 4: Intentar crear tablas que ya existen

•
Precondición: Las tablas usuarios, roles, productos y facturas ya existen en la base de datos.

•
Acción: Ejecutar el script de inicialización de la base de datos o llamar al endpoint /api/v1/admin/init-db.

•
Resultado esperado:

•
El sistema debe manejar la situación sin errores críticos (ej. ignorar la creación si ya existen, o lanzar un error específico si la política es no permitir re-creación).

•
Si el script/endpoint está diseñado para ser idempotente, debería retornar éxito o un mensaje informativo.

•
Si no es idempotente, podría retornar un 500 Internal Server Error con un mensaje de "tablas ya existen". (Se debe definir el comportamiento esperado).



✅ Definición de Hecho

📦 Alcance Funcional




El script/proceso de inicialización de la base de datos puede ser ejecutado exitosamente.




Todas las tablas requeridas (usuarios, roles, productos, facturas) son creadas con sus esquemas definidos.




Las llaves primarias y foráneas están correctamente configuradas para mantener la integridad de los datos.




El sistema proporciona retroalimentación clara sobre el éxito o fracaso de la operación.

🧪 Pruebas Completadas




Se ejecutaron pruebas unitarias/de integración para la creación de cada tabla individualmente.




Se cubrieron los casos de éxito y los diferentes escenarios de error (conexión, permisos, tablas existentes).




Las pruebas funcionales para la inicialización de la base de datos están documentadas y pasadas.

📄 Documentación Técnica




El esquema de la base de datos (diagrama ER, definición de tablas y campos) está documentado.




El script o proceso para la creación de tablas está documentado, incluyendo requisitos de entorno y permisos.




Si existe, el endpoint de inicialización de base de datos está documentado en Swagger / OpenAPI.

🔐 Manejo de Errores




Se devuelve código HTTP 500 Internal Server Error para fallos de conexión, permisos o errores inesperados durante la creación de tablas.




Los mensajes de error son claros y proporcionan suficiente información para el diagnóstico.




El sistema no expone detalles sensibles de la base de datos en los mensajes de error al usuario final.

Referencias

[[1] ENTREGABLE WEB SERVICE (1).pdf - Sección "1. API del Módulo de Usuarios", "2. API del Módulo de Productos", "6. API del Módulo de Facturación" (para referencia de módulos que requieren tablas).](https://github.com/orgs/Gestion-productos-de-limpieza/projects/3/views/1?pane=issue&itemId=181647137&issue=Gestion-productos-de-limpieza%7CGestion-productos-de-limpieza%7C30#)