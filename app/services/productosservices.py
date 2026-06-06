from app.domain.productosdomain import ProductoCreate
from app.core.productoscore import validar_categoria

class ProductosService:
    def __init__(self):
        self.db_productos = []

    def registrar(self, datos: ProductoCreate):
        if not validar_categoria(datos.categoria):
            raise ValueError(f"Categoría '{datos.categoria}' no permitida")
        
        nuevo_prod = {
            "id": len(self.db_productos) + 1,
            **datos.model_dump()
        }
        self.db_productos.append(nuevo_prod)
        return nuevo_prod

    def listar_todos(self):
        return self.db_productos

productos_service = ProductosService()
