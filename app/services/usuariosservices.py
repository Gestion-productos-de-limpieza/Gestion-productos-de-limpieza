from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse, UsuarioListItem
from app.repositories.usuariosrepositories import UsuariosRepositories


class UsuariosServices:

    def __init__(self, repo: UsuariosRepositories):
        self.repo = repo

    def registrar(self, datos: UsuarioCreate) -> UsuarioResponse:
        existente = self.repo.obtener_por_correo(datos.correo)
        if existente:
            raise ValueError("El correo ya esta registrado")

        u = self.repo.crear(
            nombre     = datos.nombre,
            correo     = datos.correo,
            contrasena = datos.contrasena,
            rol        = datos.rol,
        )
        return UsuarioResponse(**u.to_response())

    def listar(self, rol: str = None) -> list[UsuarioListItem]:
        if rol:
            usuarios = self.repo.obtener_por_rol(rol)
        else:
            usuarios = self.repo.obtener_todos()

        if not usuarios:
            raise ValueError("No hay usuarios registrados")

        return [UsuarioListItem(**u.to_list_item()) for u in usuarios]


from app.repositories.usuariosrepositories import usuario_repository
usuarios_service = UsuariosServices(usuario_repository)
