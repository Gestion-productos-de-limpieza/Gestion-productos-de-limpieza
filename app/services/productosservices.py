from app.repositories.productosrepositories import ProductRepository
from app.domain.productosdomain import ProductCreate
from fastapi import HTTPException

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def create_product(self, data: ProductCreate):
        if data.price < 0:
            raise HTTPException(status_code=400, detail="El precio no puede ser negativo")
        return self.repo.create(data)
