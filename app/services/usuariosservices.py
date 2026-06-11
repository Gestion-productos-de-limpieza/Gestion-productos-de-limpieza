# ─────────────────────────────────────────────────────────────
# CAPA SERVICIO — Orquestación de lógica de negocio
# ─────────────────────────────────────────────────────────────

from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse
from app.repositories.usuariosrepositories import usuario_repository
from app.core.usuarioscore import obtener_hash_contrasena

class UsuariosServices:

    def __init__(self, repo):
        self.repo = repo

    def registrar(self, datos: UsuarioCreate) -> UsuarioResponse:
        """Registro de usuarios con validación de duplicados y hasheo."""
        if self.repo.obtener_por_correo(datos.correo):
            raise ValueError("El correo ya está registrado")

        hashed_pw = obtener_hash_contrasena(datos.contrasena)
        
        u = self.repo.crear(
            nombre=datos.nombre,
            correo=datos.correo,
            contrasena=hashed_pw,
            rol=datos.rol or "cliente"
        )
        return UsuarioResponse.model_validate(u.to_response())

    def listar(self) -> list[UsuarioResponse]:
        """Obtiene la lista de todos los usuarios registrados."""
        return [UsuarioResponse.model_validate(u.to_response()) 
                for u in self.repo.obtener_todos()]

    def eliminar(self, id_a_eliminar: int, id_admin_activo: int) -> dict:
        """Eliminación segura validando que el admin no se borre a sí mismo."""
        if id_a_eliminar == id_admin_activo:
            raise PermissionError("No puedes eliminar tu propia cuenta mientras está activa")

        ok = self.repo.eliminar(id_a_eliminar)
        if not ok:
            raise ValueError(f"El usuario con ID {id_a_eliminar} no existe")
            
        return {
            "mensaje": "Usuario eliminado exitosamente",
            "success": True
        }

    def actualizar(self, id: int, datos: UsuarioCreate) -> UsuarioResponse:
        """Actualización de datos de usuario."""
        u = self.repo.actualizar(id, datos.nombre, datos.correo, datos.rol)
        if not u:
            raise ValueError(f"Usuario con ID {id} no encontrado")
        return UsuarioResponse.model_validate(u.to_response())

# ── INSTANCIA CRÍTICA ──
# Esta es la línea que falta y causa el ImportError
usuarios_service = UsuariosServices(usuario_repository)
