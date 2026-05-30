# ─────────────────────────────────────────────────────────────
# CAPA SERVICIO — orquesta dominio + repositorio
# Contiene las reglas de negocio y el flujo.
# No importa nada de FastAPI aquí.
# ─────────────────────────────────────────────────────────────

from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse
from app.repositories.usuariosrepositories import UsuariosRepositories


class UsuariosServices:

    def __init__(self, repo: UsuariosRepositories):
        self.repo = repo

    def registrar(self, datos: UsuarioCreate) -> UsuarioResponse:
        # Verificar correo duplicado
        existente = self.repo.obtener_por_correo(datos.correo)
        if existente:
            raise ValueError("El correo ya está registrado")

        u = self.repo.crear(
            nombre     = datos.nombre,
            correo     = datos.correo,
            contrasena = datos.contrasena,
            rol        = datos.rol,
        )
        return UsuarioResponse(**u.to_response())


# Instancia única compartida
from app.repositories.usuariosrepositories import usuario_repository
usuarios_service = UsuariosServices(usuario_repository)