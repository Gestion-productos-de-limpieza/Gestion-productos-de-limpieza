CATEGORIAS_PERMITIDAS = [
    "limpieza personal",
    "limpieza del hogar",
    "desinfectantes",
    "lavandería",
    "accesorios de limpieza"
]

def validar_categoria(categoria: str) -> bool:
    """Verifica si la categoría existe en la lista oficial"""
    return categoria.lower() in CATEGORIAS_PERMITIDAS
