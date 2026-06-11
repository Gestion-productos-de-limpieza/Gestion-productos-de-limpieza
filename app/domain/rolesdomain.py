from pydantic import BaseModel, ConfigDict
from typing import Optional

ROLES_DEFAULT = {"administrador", "operador", "vendedor", "mayorista", "cliente"}


# ── SCHEMAS PYDANTIC ──────────────────────────────────────────
class RolBase(BaseModel):
    nombre: str
    descripcion: str
    descuento_porcentaje: Optional[int] = 0


class RolCreate(RolBase):
    pass


class RolResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    descuento_porcentaje: int
    model_config = ConfigDict(from_attributes=True)


# ── ENTIDAD DE DOMINIO ────────────────────────────────────────
class RolEntidad:
    def __init__(self, id: int, nombre: str,
                 descripcion: str, descuento_porcentaje: int = 0):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.descuento_porcentaje = descuento_porcentaje

    def to_response(self) -> dict:
        return {
            "id":                   self.id,
            "nombre":               self.nombre,
            "descripcion":          self.descripcion,
            "descuento_porcentaje": self.descuento_porcentaje,
        }