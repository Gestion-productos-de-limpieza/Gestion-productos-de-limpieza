from pydantic import BaseModel, Field


class DescuentoRequest(BaseModel):
    cliente_id: int   = Field(..., description="ID del cliente")
    subtotal:   float = Field(..., gt=0, description="Subtotal de la compra")


class DescuentoResponse(BaseModel):
    codigo:               int
    cliente:              str
    tipo_cliente:         str
    subtotal:             float
    descuento_porcentaje: float
    descuento_valor:      float
    total:                float
    mensaje:              str


TABLA_DESCUENTOS = [
    (500_000, 25),
    (200_000, 20),
    (100_000, 15),
    (50_000,  10),
]


def calcular_porcentaje(subtotal: float) -> float:
    for minimo, porcentaje in TABLA_DESCUENTOS:
        if subtotal >= minimo:
            return porcentaje
    return 0
