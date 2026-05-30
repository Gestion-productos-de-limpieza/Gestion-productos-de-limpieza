from pydantic import BaseModel
from typing import Optional

# ── Modelo para CREAR (lo que recibe la API) ──
class ProductoCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    categoria: Optional[str] = "General"  # Agregado porque tu API tiene ruta de categoría

# ── Modelo para RESPONDER (lo que devuelve la API) ──
class ProductoResponse(ProductoCreate):
    id: int

    class Config:
        from_attributes = True
