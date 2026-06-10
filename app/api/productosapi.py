from fastapi import APIRouter, HTTPException, status
from typing import List
from app.domain.productosdomain import ProductoCreate, ProductoResponse
from app.services.productosservices import productos_service

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(datos: ProductoCreate):
    try:
        return productos_service.registrar(datos)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[ProductoResponse])
def listar_productos():
    return productos_service.listar_todos()
