from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse
from app.repositories.usuariosrepositories import UsuariosRepositories
from app.core.usuarioscore import obtener_hash_contrasena


class UsuariosServices:

    def __init__(self, repo: UsuariosRepositories):
        self.repo = repo

    def registrar(self, datos: UsuarioCreate) -> UsuarioResponse:
        if self.repo.obtener_por_correo(datos.correo):
            raise ValueError("El correo ya está registrado")

        # Hashear antes de guardar
        hashed_pw = obtener_hash_contrasena(datos.contrasena)
        
        u = self.repo.crear(
            nombre=datos.nombre,
            correo=datos.correo,
            contrasena=hashed_pw,
            rol=datos.rol or "cliente"
        )
        return UsuarioResponse.model_validate(u.to_response())
    

from app.repositories.usuariosrepositories import usuario_repository
usuarios_service = UsuariosServices(usuario_repository)
