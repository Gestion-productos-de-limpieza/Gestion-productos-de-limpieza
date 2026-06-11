from app.domain.descuentosdomain import DescuentoResponse, calcular_porcentaje, DescuentoRequest
from app.repositories.clientesrepositories import ClientesRepositories


class DescuentosServices:

    def __init__(self, clientes_repo: ClientesRepositories):
        self.clientes_repo = clientes_repo

    def aplicar_descuento(self, datos: DescuentoRequest) -> DescuentoResponse:
        cliente = self.clientes_repo.obtener_por_id(datos.cliente_id)

        if not cliente:
            raise LookupError("El cliente no existe en el sistema")

        if cliente.tipo_cliente.lower() != "mayorista":
            raise ValueError("El cliente no aplica para descuento")

        porcentaje = calcular_porcentaje(datos.subtotal)

        if porcentaje == 0:
            raise ValueError("El cliente no aplica para descuento")

        descuento_valor = round(datos.subtotal * (porcentaje / 100), 2)
        total = round(datos.subtotal - descuento_valor, 2)

        return DescuentoResponse(
            codigo=200,
            cliente=cliente.nombre,
            tipo_cliente=cliente.tipo_cliente,
            subtotal=datos.subtotal,
            descuento_porcentaje=porcentaje,
            descuento_valor=descuento_valor,
            total=total,
            mensaje="Descuento aplicado exitosamente",
        )


from app.repositories.clientesrepositories import cliente_repository
descuentos_service = DescuentosServices(cliente_repository)
