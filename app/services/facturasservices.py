# app/services/facturasservices.py
from app.domain.facturasdomain import FacturaCreate, FacturaResponse, FacturaListItem
from app.repositories.facturasrepositories import factura_repository

class FacturasServices:

    def __init__(self, repo):
        self.repo = repo

    def registrar(self, datos: FacturaCreate) -> FacturaResponse:
        f = self.repo.crear(
            cliente=datos.cliente,
            total=datos.total,
            estado=datos.estado or "pendiente"
        )
        return FacturaResponse.model_validate(f.to_response())

    def listar(self) -> list[FacturaListItem]:
        facturas = self.repo.obtener_todos()
        if not facturas:
            raise ValueError("No hay facturas registradas")
        return [FacturaListItem(**f.to_list_item()) for f in facturas]

    def eliminar(self, id: int) -> dict:
        factura = self.repo.obtener_por_id(id)
        if not factura:
            raise ValueError("La factura no existe")
        if factura.estado == "pagada":
            raise PermissionError("No se puede eliminar una factura ya pagada")
        self.repo.eliminar(id)
        return {"codigo": 200, "mensaje": "Factura eliminada exitosamente"}

facturas_service = FacturasServices(factura_repository)