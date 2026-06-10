from app.domain.usuariosdomain import UsuarioEntidad
from typing import Optional


class UsuariosRepositories:

    def __init__(self):
        self._datos: list[UsuarioEntidad] = []
        self._siguiente_id = 1

    def crear(self, nombre: str, correo: str, contrasena: str, rol: str) -> UsuarioEntidad:
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

    def obtener_por_correo(self, correo: str) -> Optional[UsuarioEntidad]:
        return next((u for u in self._datos if u.correo.lower() == correo.lower()), None)
usuario_repository = UsuariosRepositories()
