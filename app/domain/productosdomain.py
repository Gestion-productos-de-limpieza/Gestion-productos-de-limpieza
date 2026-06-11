from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional


class ProductoCreate(BaseModel):
    nombre:    str   = Field(..., min_length=2, description="Nombre del producto")
    precio:    float = Field(..., gt=0,         description="Precio mayor a 0")
    stock:     int   = Field(..., ge=0,         description="Stock no negativo")
    categoria: str   = Field(..., min_length=2)

    @field_validator("nombre")
    @classmethod
    def nombre_sin_numeros(cls, v: str) -> str:
        if any(c.isdigit() for c in v):
            raise ValueError("El nombre no puede contener numeros")
        return v.strip().title()

    @field_validator("precio")
    @classmethod
    def precio_valido(cls, v: float) -> float:
        return round(v, 2)


class ProductoResponse(BaseModel):
    id:         int
    nombre:     str
    precio:     float
    stock:      int
    categoria:  str
    disponible: bool
    model_config = ConfigDict(from_attributes=True)


class Producto:
    def __init__(self, id: int, nombre: str, precio: float,
                 stock: int, categoria: str):
        self.id        = id
        self.nombre    = nombre
        self.precio    = precio
        self.stock     = stock
        self.categoria = categoria

    def tiene_stock(self, cantidad: int = 1) -> bool:
        return self.stock >= cantidad

    def aplicar_descuento(self, porcentaje: float) -> float:
        if self.precio < 50000:
            raise ValueError("Descuento solo aplica a precios mayores a $50.000")
        return round(self.precio * (1 - porcentaje / 100), 2)

    def to_response(self) -> dict:
        return {
            "id":         self.id,
            "nombre":     self.nombre,
            "precio":     self.precio,
            "stock":      self.stock,
            "categoria":  self.categoria,
            "disponible": self.stock > 0,
        }
