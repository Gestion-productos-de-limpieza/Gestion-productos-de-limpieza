# ─────────────────────────────────────────────────────────────
# CAPA SERVICIO — Lógica de negocio
# ─────────────────────────────────────────────────────────────

from app.domain.rolesdomain import RolCreate, RolResponse
from app.repositories.rolesrepositories import rol_repository


class RolesServices:

    def __init__(self, repo):
        self.repo = repo

    def crear_rol(self, datos: RolCreate) -> RolResponse:
        """Crea un nuevo rol validando que no esté duplicado."""
        existente = self.repo.obtener_por_nombre(datos.nombre)
        if existente:
            raise ValueError("El rol ya existe en el sistema")

        r = self.repo.crear(
            nombre=datos.nombre,
            descripcion=datos.descripcion,
            descuento_porcentaje=datos.descuento_porcentaje or 0
        )
        return RolResponse.model_validate(r.to_response())

    def listar(self) -> list[RolResponse]:
        """Lista todos los roles del sistema."""
        roles = self.repo.obtener_todos()
        if not roles:
            raise ValueError("No hay roles registrados")
        return [RolResponse.model_validate(r.to_response()) for r in roles]


# ── INSTANCIA GLOBAL ──────────────────────────────────────────
roles_service = RolesServices(rol_repository)