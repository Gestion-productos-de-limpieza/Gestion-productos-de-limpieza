# ─────────────────────────────────────────────────────────────
# CAPA REPOSITORIO — única responsabilidad: guardar y recuperar
# Solo manipula datos. Sin lógica de negocio aquí.
# ─────────────────────────────────────────────────────────────

from app.domain.usuariosdomain import UsuarioEntidad
from typing import Optional

class UsuariosRepositories:

    def __init__(self):
        # Almacén en memoria: lista de objetos UsuarioEntidad
        self._datos: list[UsuarioEntidad] = []
        self._siguiente_id: int = 1

    def obtener_todos(self) -> list[UsuarioEntidad]:
        """Recupera todos los usuarios registrados"""
        return self._datos.copy()

    def obtener_por_id(self, id: int) -> Optional[UsuarioEntidad]:
        """Busca un usuario por su ID único"""
        return next((u for u in self._datos if u.id == id), None)

    def obtener_por_correo(self, correo: str) -> Optional[UsuarioEntidad]:
        """Busca un usuario por su correo electrónico (para evitar duplicados)"""
        return next((u for u in self._datos
                     if u.correo.lower() == correo.lower()), None)

    def crear(self, nombre: str, correo: str,
              contrasena: str, rol: str) -> UsuarioEntidad:
        """Crea y persiste un nuevo usuario"""
        nuevo = UsuarioEntidad(
            id         = self._siguiente_id,
            nombre     = nombre,
            correo     = correo,
            contrasena = contrasena,
            rol        = rol,
        )
        self._datos.append(nuevo)
        self._siguiente_id += 1
        return nuevo

    def eliminar(self, id: int) -> bool:
        """Elimina un usuario del sistema por su ID"""
        usuario = self.obtener_por_id(id)
        if not usuario:
            return False
        self._datos.remove(usuario)
        return True

    def actualizar(self, id: int, nombre: str, correo: str, rol: str) -> Optional[UsuarioEntidad]:
        """Actualiza los datos de un usuario existente"""
        u = self.obtener_por_id(id)
        if not u:
            return None
        u.nombre = nombre
        u.correo = correo
        u.rol = rol
        return u

# Instancia única compartida (Singleton)
usuario_repository = UsuariosRepositories()

