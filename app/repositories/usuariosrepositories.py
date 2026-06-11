# ─────────────────────────────────────────────────────────────
# CAPA REPOSITORIO — única responsabilidad: guardar y recuperar
# Solo manipula datos. Sin lógica de negocio aquí.
# ─────────────────────────────────────────────────────────────

from app.domain.usuariosdomain import Usuario
from typing import Optional


class UsuariosRepositories:

    def __init__(self):
        self._datos: list[Usuario] = []
        self._siguiente_id: int = 1

    def obtener_todos(self) -> list[Usuario]:
        return self._datos.copy()

    def obtener_por_id(self, id: int) -> Optional[Usuario]:
        return next((u for u in self._datos if u.id == id), None)

    def obtener_por_correo(self, correo: str) -> Optional[Usuario]:
        return next((u for u in self._datos
                     if u.correo.lower() == correo.lower()), None)

    def crear(self, nombre: str, correo: str,
              contrasena: str, rol: str) -> Usuario:
        nuevo = Usuario(
            id         = self._siguiente_id,
            nombre     = nombre,
            correo     = correo,
            contrasena = contrasena,
            rol        = rol,
        )
        self._datos.append(nuevo)
        self._siguiente_id += 1
        return nuevo


# Instancia única compartida
usuario_repository = UsuariosRepositories()