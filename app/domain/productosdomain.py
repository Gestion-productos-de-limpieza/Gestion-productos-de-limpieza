from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional

# ── 1. SCHEMAS DE PYDANTIC (Para la API) ──

class ProductoBase(BaseModel):
    nombre:      str   = Field(..., min_length=2, description="Nombre del producto")
    descripcion: Optional[str] = Field(None, description="Descripción opcional")
    precio:      float = Field(..., gt=0,        description="Precio mayor a 0")
    stock:       int   = Field(..., ge=0,        description="Stock no negativo")
    categoria:   str   = Field(..., min_length=2)

    # REGLA DE NEGOCIO: El nombre no puede contener números
    @field_validator("nombre")
    @classmethod
    def nombre_sin_numeros(cls, v):
        if any(c.isdigit() for c in v):
            raise ValueError("El nombre no puede contener números")
        return v.strip().title()

    # REGLA DE NEGOCIO: Precio con dos decimales máximo
    @field_validator("precio")
    @classmethod
    def precio_valido(cls, v):
        return round(v, 2)

class ProductoCreate(ProductoBase): # <--- ESTO ES LO QUE BUSCA EL IMPORT
    """Schema para la creación de productos"""
    pass

class ProductoResponse(BaseModel):
    """Schema para la salida de la API"""
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    categoria: str
    disponible: bool
    
model_config = ConfigDict(from_attributes=True)


# ── 2. CLASE DE ENTIDAD (Para el Repositorio) ──

class Producto:
    """Clase de entidad para lógica interna y base de datos"""
    def __init__(self, id: int, nombre: str, precio: float,
                 stock: int, categoria: str, descripcion: Optional[str] = None):
        self.id          = id
        self.nombre      = nombre
        self.precio      = precio
        self.stock       = stock
        self.categoria   = categoria
        self.descripcion = descripcion

    def tiene_stock(self, cantidad: int = 1) -> bool:
        return self.stock >= cantidad

    def aplicar_descuento(self, porcentaje: float) -> float:
        if self.precio > 50000:
            raise ValueError("Descuento solo aplica a precios mayores a $50.000")
        return round(self.precio * (1 - porcentaje / 100), 2)

    def to_response(self) -> dict:
        return {
            "id":          self.id,
            "nombre":      self.nombre,
            "descripcion": self.descripcion,
            "precio":      self.precio,
            "stock":       self.stock,
            "categoria":   self.categoria,
            "disponible":  self.stock > 0,
        }
