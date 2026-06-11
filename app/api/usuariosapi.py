from fastapi import APIRouter, HTTPException, status, Header
from typing import Optional
from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse, UsuarioListItem
from app.services.usuariosservices import usuarios_service

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Usuarios"],
)


@router.post("/", response_model=UsuarioResponse,
             status_code=status.HTTP_201_CREATED)
def registrar_usuario(datos: UsuarioCreate):
    try:
        return usuarios_service.registrar(datos)
    except ValueError as e:
        mensaje = str(e)
        if "ya esta registrado" in mensaje:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"codigo": 409, "mensaje": mensaje}
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"codigo": 400, "mensaje": mensaje}
        )


# ── GET /api/v1/users  — Listar usuarios ──────────────────────
@router.get("/")
def listar_usuarios(
    rol: Optional[str] = None,
    x_user_role: Optional[str] = Header(default=None)
):
    # Validar autenticacion (simulada via header X-User-Role)
    if x_user_role is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"codigo": 401, "mensaje": "Usuario no autenticado"}
        )

    # Validar autorizacion (solo administrador)
    if x_user_role.lower() != "administrador":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"codigo": 403, "mensaje": "No tiene permisos para listar usuarios"}
        )

    try:
        usuarios = usuarios_service.listar(rol)
        return {
            "codigo": 200,
            "usuarios": [u.model_dump() for u in usuarios]
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"codigo": 404, "mensaje": str(e)}
        )
