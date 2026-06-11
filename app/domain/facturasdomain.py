from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class ProductoFacturaBase(BaseModel):
    producto_id: int = Field(..., example=101)
    cantidad: int = Field(..., gt=0, example=5)

class ProductoFacturaResponse(BaseModel):
    id: int = Field(..., example=101)
    nombre: str = Field(..., example="Jabón líquido")
    cantidad: int = Field(..., gt=0, example=5)
    precio_unitario: float = Field(..., gt=0, example=5000.0)

class FacturaCreate(BaseModel):
    cliente_id: int = Field(..., example=1)
    productos: List[ProductoFacturaBase]

class FacturaResponse(BaseModel):
    id_factura: int = Field(..., example=12345)
    cliente: dict = Field(..., example={"id": 1, "nombre": "María López", "tipo_cliente": "mayorista"})
    productos: List[ProductoFacturaResponse]
    subtotal: float = Field(..., example=41000.0)
    descuento_porcentaje: int = Field(0, example=10)
    descuento_valor: float = Field(0.0, example=4100.0)
    total: float = Field(..., example=36900.0)
    estado: str = Field("pendiente", example="pendiente")
    fecha: date = Field(..., example="2026-05-30")
    mensaje: str = Field(..., example="Factura registrada exitosamente")

    class Config:
        from_attributes = True

class FacturaInDB(FacturaResponse):
    pass

class FacturaFilter(BaseModel):
    fecha: Optional[date] = None
    cliente_id: Optional[int] = None
    estado: Optional[str] = None
