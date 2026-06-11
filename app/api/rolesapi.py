from fastapi import APIRouter, HTTPException, status, Header
from typing import Optional
from app.domain.rolesdomain import RolCreate, RolResponse
from app.services.rolesservices import roles_service

router = APIRouter(
    prefix="/api/v1/roles",
    tags=["Roles"],
)


# ── POST /api/v1/roles — Crear rol ────────────────────────────
@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def crear_rol(
    datos: RolCreate,
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
            detail={"codigo": 403, "mensaje": "No tiene permisos para crear roles"}
        )
    try:
        r = roles_service.crear_rol(datos)
        return {
            "codigo": 201,
            "id": r.id,
            "nombre": r.nombre,
            "descripcion": r.descripcion,
            "descuento_porcentaje": r.descuento_porcentaje,
            "mensaje": "Rol creado exitosamente"
        }
    except ValueError as e:
        mensaje = str(e)
        if "ya existe" in mensaje:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"codigo": 409, "mensaje": mensaje}
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"codigo": 400, "mensaje": mensaje}
        )


# ── GET /api/v1/roles — Listar roles ─────────────────────────
@router.get("/")
def listar_roles(
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
            detail={"codigo": 403, "mensaje": "No tiene permisos para listar roles"}
        )
    try:
        roles = roles_service.listar()
        return {
            "codigo": 200,
            "roles": [r.model_dump() for r in roles]
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"codigo": 404, "mensaje": str(e)}
        )