from pydantic import BaseModel, ConfigDict


class Cliente:
    def __init__(self, id: int, nombre: str, tipo_cliente: str):
        self.id = id
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente

    def to_response(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo_cliente": self.tipo_cliente,
        }


class ClienteResponse(BaseModel):
    id: int
    nombre: str
    tipo_cliente: str
    model_config = ConfigDict(from_attributes=True)
