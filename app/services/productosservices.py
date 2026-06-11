from app.domain.productosdomain import ProductoCreate, ProductoResponse
from app.repositories.productosrepositories import ProductosRepositories


class ProductosServices:

    def __init__(self, repo: ProductosRepositories):
        self.repo = repo

    def listar(self) -> list[ProductoResponse]:
        productos = self.repo.obtener_todos()
        if not productos:
            raise ValueError("No hay productos registrados")
        return [ProductoResponse(**p.to_response()) for p in productos]

    def obtener(self, id: int) -> ProductoResponse:
        p = self.repo.obtener_por_id(id)
        if not p:
            raise ValueError(f"Producto con id {id} no encontrado")
        return ProductoResponse(**p.to_response())

    def crear(self, datos: ProductoCreate) -> ProductoResponse:
        p = self.repo.crear(
            nombre    = datos.nombre,
            precio    = datos.precio,
            stock     = datos.stock,
            categoria = datos.categoria,
        )
        return ProductoResponse(**p.to_response())

    def actualizar(self, id: int, datos: ProductoCreate) -> ProductoResponse:
        p = self.repo.actualizar(
            id        = id,
            nombre    = datos.nombre,
            precio    = datos.precio,
            stock     = datos.stock,
            categoria = datos.categoria,
        )
        if not p:
            raise ValueError(f"Producto {id} no existe")
        return ProductoResponse(**p.to_response())

    def eliminar(self, id: int) -> dict:
        ok = self.repo.eliminar(id)
        if not ok:
            raise ValueError(f"Producto {id} no existe")
        return {"mensaje": f"Producto {id} eliminado correctamente"}

    def por_categoria(self, categoria: str) -> list[ProductoResponse]:
        productos = self.repo.obtener_por_categoria(categoria)
        if not productos:
            raise ValueError(f"No hay productos en la categoria '{categoria}'")
        return [ProductoResponse(**p.to_response()) for p in productos]


from app.repositories.productosrepositories import producto_repository
productos_service = ProductosServices(producto_repository)

