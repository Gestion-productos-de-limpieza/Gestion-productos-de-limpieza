from fastapi import APIRouter, Depends, status
from typing import List
from app.domain.productosdomain import Product, ProductCreate
from app.services.productosservices import ProductService
from app.repositories.productosrepositories import ProductRepository

router = APIRouter(prefix="/api/v1/products", tags=["products"])

# Instanciamos el repositorio y el servicio (Inyección manual para este ejemplo)
repo = ProductRepository()
service = ProductService(repo)

@router.get("/", response_model=List[Product])
def list_products():
    return service.repo.get_all()

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreate):
    return service.create_product(data)
