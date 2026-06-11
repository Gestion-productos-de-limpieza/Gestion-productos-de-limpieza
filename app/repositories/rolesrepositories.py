# ─────────────────────────────────────────────────────────────
# CAPA REPOSITORIO — Persistencia en memoria
# ─────────────────────────────────────────────────────────────

from app.domain.rolesdomain import RolEntidad
from typing import Optional


class RolesRepositories:

    def __init__(self):
        self._datos: list[RolEntidad] = []
        self._siguiente_id: int = 1
        self._cargar_roles_default()

    def _cargar_roles_default(self):
        """Pre-carga los roles del sistema al iniciar."""
        defaults = [
            ("administrador", "Acceso total al sistema",          0),
            ("operador",      "Gestión operativa del sistema",    0),
            ("vendedor",      "Gestión de ventas",                0),
            ("mayorista",     "Descuentos por volumen de compra", 15),
            ("cliente",       "Cliente estándar del sistema",     0),
        ]
        for nombre, descripcion, descuento in defaults:
            self.crear(nombre, descripcion, descuento)

    def obtener_todos(self) -> list[RolEntidad]:
        return self._datos.copy()

    def obtener_por_id(self, id: int) -> Optional[RolEntidad]:
        return next((r for r in self._datos if r.id == id), None)

    def obtener_por_nombre(self, nombre: str) -> Optional[RolEntidad]:
        return next((r for r in self._datos
                     if r.nombre.lower() == nombre.lower()), None)

    def crear(self, nombre: str, descripcion: str,
              descuento_porcentaje: int = 0) -> RolEntidad:
        nuevo = RolEntidad(
            id=self._siguiente_id,
            nombre=nombre,
            descripcion=descripcion,
            descuento_porcentaje=descuento_porcentaje,
        )
        self._datos.append(nuevo)
        self._siguiente_id += 1
        return nuevo


# ── INSTANCIA GLOBAL ──────────────────────────────────────────
rol_repository = RolesRepositories()