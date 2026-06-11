from typing import List, Optional
from datetime import date

from app.domain.facturasdomain import FacturaCreate, FacturaResponse, FacturaInDB, ProductoFacturaResponse
from app.repositories.facturasrepositories import FacturaRepository
from app.services.clientesservices import ClienteService
from app.services.productosservices import ProductoService

class FacturaService:
    def __init__(self, factura_repository: FacturaRepository, cliente_service: ClienteService, producto_service: ProductoService):
        self.factura_repository = factura_repository
        self.cliente_service = cliente_service
        self.producto_service = producto_service

    async def register_factura(self, factura_data: FacturaCreate) -> Optional[FacturaResponse]:
        # HU-XXX: Registrar Factura
        cliente = await self.cliente_service.get_cliente_by_id(factura_data.cliente_id)
        if not cliente:
            return None # Cliente no encontrado

        productos_facturados = []
        subtotal = 0.0

        for item in factura_data.productos:
            producto = await self.producto_service.get_producto_by_id(item.producto_id)
            if not producto:
                return None # Producto no encontrado
            if producto.cantidad < item.cantidad:
                return None # Stock insuficiente
            
            # Actualizar stock (simulado, en un sistema real sería parte de la transacción)
            await self.producto_service.update_producto_stock(item.producto_id, -item.cantidad)

            productos_facturados.append(ProductoFacturaResponse(
                id=producto.id,
                nombre=producto.nombre,
                cantidad=item.cantidad,
                precio_unitario=producto.precio
            ))
            subtotal += producto.precio * item.cantidad

        descuento_porcentaje = 0
        descuento_valor = 0.0
        total = subtotal

        if cliente.tipo_cliente == "mayorista":
            # Lógica de aplicación de descuento basada en HU-XXX_Aplicar_Descuento_v2.md
            if subtotal >= 500000:
                descuento_porcentaje = 25
            elif subtotal >= 200000:
                descuento_porcentaje = 20
            elif subtotal >= 100000:
                descuento_porcentaje = 15
            elif subtotal >= 50000:
                descuento_porcentaje = 10
            
            descuento_valor = subtotal * (descuento_porcentaje / 100)
            total = subtotal - descuento_valor

        factura_in_db = FacturaInDB(
            id_factura=0, # Se asignará en el repositorio
            cliente=cliente.model_dump(),
            productos=[p.model_dump() for p in productos_facturados],
            subtotal=subtotal,
            descuento_porcentaje=descuento_porcentaje,
            descuento_valor=descuento_valor,
            total=total,
            estado="pendiente",
            fecha=date.today(),
            mensaje="Factura registrada exitosamente"
        )
        new_factura = await self.factura_repository.create_factura(factura_in_db)
        return FacturaResponse(**new_factura.model_dump())

    async def get_all_facturas(self, fecha: Optional[date] = None, cliente_id: Optional[int] = None, estado: Optional[str] = None) -> List[FacturaResponse]:
        # HU-XXX: Listar Facturas - Filtrar por fecha, cliente o estado
        facturas_in_db = await self.factura_repository.get_all_facturas(fecha, cliente_id, estado)
        return [FacturaResponse(**factura.model_dump()) for factura in facturas_in_db]

    async def delete_factura(self, factura_id: int) -> bool:
        # HU-XXX: Eliminar Factura - No permitir eliminar factura pagada
        factura = await self.factura_repository.get_factura_by_id(factura_id)
        if not factura:
            return False # Factura no existe
        if factura.estado == "pagada": # Asumiendo que existe un estado 'pagada'
            return False # No se puede eliminar una factura ya pagada
        
        return await self.factura_repository.delete_factura(factura_id)
