# app/repositories/facturasrepositories.py
from app.domain.facturasdomain import FacturaEntidad
from typing import Optional

class FacturasRepositories:

    def __init__(self):
        self._datos: list[FacturaEntidad] = []
        self._siguiente_id: int = 1

    def obtener_todos(self) -> list[FacturaEntidad]:
        return self._datos.copy()

    def obtener_por_id(self, id: int) -> Optional[FacturaEntidad]:
        return next((f for f in self._datos if f.id == id), None)

    def crear(self, cliente: str, total: float,
              estado: str = "pendiente") -> FacturaEntidad:
        nueva = FacturaEntidad(
            id=self._siguiente_id,
            cliente=cliente,
            total=total,
            estado=estado,
        )
        self._datos.append(nueva)
        self._siguiente_id += 1
        return nueva

    def eliminar(self, id: int) -> bool:
        factura = self.obtener_por_id(id)
        if not factura:
            return False
        self._datos.remove(factura)
        return True

factura_repository = FacturasRepositories()