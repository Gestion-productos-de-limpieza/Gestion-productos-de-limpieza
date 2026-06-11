# ─────────────────────────────────────────────────────────────
# CAPA REPOSITORIO — Responsabilidad: Persistencia en memoria
# ─────────────────────────────────────────────────────────────

from app.domain.usuariosdomain import UsuarioEntidad
from typing import Optional

class UsuariosRepositories:

    def __init__(self):
        # Almacén de datos centralizado para la sesión activa
        self._datos: list[UsuarioEntidad] = []
        self._siguiente_id: int = 1

    def obtener_todos(self) -> list[UsuarioEntidad]:
        return self._datos.copy()

    def obtener_por_id(self, id: int) -> Optional[UsuarioEntidad]:
        return next((u for u in self._datos if u.id == id), None)

    def obtener_por_correo(self, correo: str) -> Optional[UsuarioEntidad]:
        return next((u for u in self._datos 
                     if u.correo.lower() == correo.lower()), None)

    def crear(self, nombre: str, correo: str, 
              contrasena: str, rol: str) -> UsuarioEntidad:
        nuevo = UsuarioEntidad(
            id=self._siguiente_id, 
            nombre=nombre, 
            correo=correo, 
            contrasena=contrasena, 
            rol=rol
        )
        self._datos.append(nuevo)
        self._siguiente_id += 1
        return nuevo

    # MÉTODO CRÍTICO: Soluciona el AttributeError detectado
    def eliminar(self, id: int) -> bool:
        """Elimina la entidad del repositorio si existe."""
        usuario = self.obtener_por_id(id)
        if not usuario:
            return False
        self._datos.remove(usuario)
        return True

    def actualizar(self, id: int, nombre: str, correo: str, rol: str) -> Optional[UsuarioEntidad]:
        u = self.obtener_por_id(id)
        if not u:
            return None
        u.nombre, u.correo, u.rol = nombre, correo, rol
        return u

# Instancia global para la inyección de dependencias en el servicio
usuario_repository = UsuariosRepositories()

