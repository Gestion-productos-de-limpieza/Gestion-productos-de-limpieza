# Constantes de negocio para Productos (HU-030 y HU-031)

# Categorías oficiales permitidas en el sistema
CATEGORIAS_PERMITIDAS = [
    "limpieza personal",
    "limpieza del hogar",
    "desinfectantes",
    "lavandería",
    "accesorios de limpieza"
]

# Configuración de alertas de inventario
STOCK_MINIMO_ALERTA = 10  # El sistema podría avisar si queda menos de esta cantidad

def validar_categoria(categoria: str) -> bool:
    """Valida si la categoría ingresada es oficial (HU-Registrar Producto)"""
    return categoria.lower() in CATEGORIAS_PERMITIDAS
