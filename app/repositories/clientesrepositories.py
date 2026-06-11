from app.domain.clientesdomain import Cliente
from typing import Optional


class ClientesRepositories:

    def __init__(self):
        self._datos: list[Cliente] = []
        self._siguiente_id: int = 1
        self._seed()

    def _seed(self):
        iniciales = [
            Cliente(1, "Juan Perez",     "mayorista"),
            Cliente(2, "Maria Lopez",    "mayorista"),
            Cliente(3, "Carlos Ramirez", "mayorista"),
            Cliente(4, "Ana Torres",     "minorista"),
            Cliente(5, "Pedro Gomez",    "mayorista"),
        ]
        self._datos = iniciales
        self._siguiente_id = 6

    def obtener_todos(self) -> list[Cliente]:
        return self._datos.copy()

    def obtener_por_id(self, id: int) -> Optional[Cliente]:
        return next((c for c in self._datos if c.id == id), None)


cliente_repository = ClientesRepositories()
