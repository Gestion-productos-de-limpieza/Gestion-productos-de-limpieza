# ─────────────────────────────────────────────────────────────
# CAPA SERVICIO — Lógica de negocio
# ─────────────────────────────────────────────────────────────

from app.domain.facturasdomain import FacturaCreate, FacturaResponse, FacturaListItem
from app.repositories.facturasrepositories import factura_repository


class FacturasServices:

    def __init__(self, repo):
        self.repo = repo

    def registrar(self, datos: FacturaCreate) -> FacturaResponse:
        """Crea una nueva factura en estado pendiente."""
        f = self.repo.crear(
            cliente=datos.cliente,
            total=datos.total,
            estado=datos.estado or "pendiente"
        )
        return FacturaResponse.model_validate(f.to_response())

    def listar(self) -> list[FacturaListItem]:
        """Lista todas las facturas registradas."""
        facturas = self.repo.obtener_todos()
        if not facturas:
            raise ValueError("No hay facturas registradas")
        return [FacturaListItem(**f.to_list_item()) for f in facturas]

    def eliminar(self, id: int) -> dict:
        """
        Elimina una factura solo si está en estado pendiente.
        - 404 si no existe
        - 403 si ya fue pagada
        """
        factura = self.repo.obtener_por_id(id)

        if not factura:
            raise ValueError("La factura no existe")

        if factura.estado == "pagada":
            raise PermissionError("No se puede eliminar una factura ya pagada")

        self.repo.eliminar(id)
        return {
            "codigo": 200,
            "mensaje": "Factura eliminada exitosamente"
        }


# ── INSTANCIA GLOBAL ──────────────────────────────────────────
facturas_service = FacturasServices(factura_repository)