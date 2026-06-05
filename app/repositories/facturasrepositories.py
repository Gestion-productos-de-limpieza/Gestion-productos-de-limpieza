from typing import List, Optional
from datetime import date
from app.domain.facturasdomain import FacturaInDB

class FacturaRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection # Placeholder para la conexión a la base de datos
        self.facturas_db = [] # Simulación de base de datos en memoria
        self.next_id = 1

    async def create_factura(self, factura: FacturaInDB) -> FacturaInDB:
        # Lógica para guardar la factura en la base de datos
        factura.id_factura = self.next_id
        self.next_id += 1
        self.facturas_db.append(factura)
        return factura

    async def get_factura_by_id(self, factura_id: int) -> Optional[FacturaInDB]:
        # Lógica para obtener una factura por ID de la base de datos
        for factura in self.facturas_db:
            if factura.id_factura == factura_id:
                return factura
        return None

    async def get_all_facturas(self, fecha: Optional[date] = None, cliente_id: Optional[int] = None, estado: Optional[str] = None) -> List[FacturaInDB]:
        # Lógica para obtener todas las facturas, opcionalmente filtradas
        filtered_facturas = self.facturas_db
        if fecha:
            filtered_facturas = [f for f in filtered_facturas if f.fecha == fecha]
        if cliente_id:
            filtered_facturas = [f for f in filtered_facturas if f.cliente['id'] == cliente_id]
        if estado:
            filtered_facturas = [f for f in filtered_facturas if f.estado == estado]
        return filtered_facturas

    async def delete_factura(self, factura_id: int) -> bool:
        # Lógica para eliminar una factura de la base de datos
        initial_len = len(self.facturas_db)
        self.facturas_db = [f for f in self.facturas_db if f.id_factura != factura_id]
        return len(self.facturas_db) < initial_len
