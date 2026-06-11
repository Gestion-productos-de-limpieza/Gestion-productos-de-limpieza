from pydantic import BaseModel, ConfigDict
from typing import Optional

ESTADOS_FACTURA = {"pendiente", "pagada", "cancelada"}


# ── SCHEMAS PYDANTIC ──────────────────────────────────────────
class FacturaBase(BaseModel):
    cliente: str
    total: float
    estado: str = "pendiente"


class FacturaCreate(FacturaBase):
    pass


class FacturaResponse(BaseModel):
    id: int
    cliente: str
    total: float
    estado: str
    model_config = ConfigDict(from_attributes=True)


class FacturaListItem(BaseModel):
    id: int
    cliente: str
    total: float
    estado: str
    model_config = ConfigDict(from_attributes=True)


# ── ENTIDAD DE DOMINIO ────────────────────────────────────────
class FacturaEntidad:
    def __init__(self, id: int, cliente: str,
                 total: float, estado: str = "pendiente"):
        self.id = id
        self.cliente = cliente
        self.total = total
        self.estado = estado

    def to_response(self) -> dict:
        return {
            "id":      self.id,
            "cliente": self.cliente,
            "total":   self.total,
            "estado":  self.estado,
        }

    def to_list_item(self) -> dict:
        return self.to_response()