from fastapi import APIRouter, HTTPException, status
from typing import List
from app.domain.productosdomain import ProductoCreate, ProductoResponse
from app.services.productosservices import productos_service

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.get("/", response_model=List[ProductoResponse])
def listar_productos():
    try:
        return productos_service.listar()
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{id}", response_model=ProductoResponse)
def obtener_producto(id: int):
    try:
        return productos_service.obtener(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(datos: ProductoCreate):
    try:
        return productos_service.crear(datos)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{id}", response_model=ProductoResponse)
def actualizar_producto(id: int, datos: ProductoCreate):
    try:
        return productos_service.actualizar(id, datos)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id}")
def eliminar_producto(id: int):
    try:
        return productos_service.eliminar(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/categoria/{categoria}", response_model=List[ProductoResponse])
def por_categoria(categoria: str):
    try:
        return productos_service.por_categoria(categoria)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


