from typing import List, Optional
from app.domain.productosdomain import Product, ProductCreate

class ProductRepository:
    def __init__(self):
        self._db = {}
        self._next_id = 1

    def get_all(self) -> List[Product]:
        return list(self._db.values())

    def create(self, data: ProductCreate) -> Product:
        product = Product(id=self._next_id, **data.model_dump())
        self._db[self._next_id] = product
        self._next_id += 1
        return product
