# ─────────────────────────────────────────────────────────────
# CAPA SERVICIO — orquesta dominio + repositorio
# Contiene las reglas de negocio complejas y el flujo.
# No importa nada de FastAPI aquí.
# ─────────────────────────────────────────────────────────────

from app.domain.productosdomain import ProductoCreate, ProductoResponse
from app.repositories.productosrepositories import ProductosRepositories


class ProductosServices:

    def __init__(self, repo: ProductosRepositories):
        self.repo = repo

    def listar(self) -> list[ProductoResponse]:
        return [ProductoResponse(**p.to_response())
                for p in self.repo.obtener_todos()]

    def obtener(self, id: int) -> ProductoResponse:
        p = self.repo.obtener_por_id(id)
        if not p:
            raise ValueError(f"Producto con id {id} no encontrado")
        return ProductoResponse(**p.to_response())

    def crear(self, datos: ProductoCreate) -> ProductoResponse:
        if datos.stock == 0:
            raise ValueError("No se puede registrar un producto sin stock inicial")
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
            raise ValueError(f"No hay productos en la categoría '{categoria}'")
        return [ProductoResponse(**p.to_response()) for p in productos]


# Instancia única compartida
from app.repositories.productosrepositories import producto_repository
productos_service = ProductosServices(producto_repository)