from fastapi import APIRouter, HTTPException, status, Header
from typing import Optional
from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse, UsuarioListItem
from app.services.usuariosservices import usuarios_service

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Usuarios"],
)


# ── POST /api/v1/users — Registrar usuario ────────────────────
@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def registrar_usuario(datos: UsuarioCreate):
    try:
        u_resp = usuarios_service.registrar(datos)
        return {
            "mensaje": "Usuario registrado exitosamente",
            "usuario": u_resp,
            "success": True
        }
    except ValueError as e:
        mensaje = str(e)
        if "ya está registrado" in mensaje:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"codigo": 409, "mensaje": mensaje}
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"codigo": 400, "mensaje": mensaje}
        )


# ── GET /api/v1/users — Listar usuarios ───────────────────────
@router.get("/")
def listar_usuarios(
    rol: Optional[str] = None,
    x_user_role: Optional[str] = Header(default=None)
):
    if x_user_role is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"codigo": 401, "mensaje": "Usuario no autenticado"}
        )

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


# ── DELETE /api/v1/users/{id} — Eliminar usuario ──────────────
@router.delete("/{id}", response_model=dict)
def eliminar_usuario(
    id: int,
    x_user_role: Optional[str] = Header(default=None),
    current_user_id: int = 1
):
    if x_user_role is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"codigo": 401, "mensaje": "Usuario no autenticado"}
        )

    if x_user_role.lower() != "administrador":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"codigo": 403, "mensaje": "No tiene permisos para eliminar usuarios"}
        )

    try:
        return usuarios_service.eliminar(id, current_user_id)
    except PermissionError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"codigo": 403, "mensaje": str(e)}
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"codigo": 404, "mensaje": str(e)}
        )