# ─────────────────────────────────────────────────────────────
# CAPA API — rutas HTTP con FastAPI
# Solo recibe peticiones y llama al servicio.
# Aquí NO hay lógica de negocio.
# ─────────────────────────────────────────────────────────────

from fastapi import APIRouter, HTTPException, status
from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse
from app.services.usuariosservices import usuarios_service

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Usuarios"],
)


# ── POST /api/v1/users/ ───────────────────────────────────────
@router.post("/", response_model=UsuarioResponse,
             status_code=status.HTTP_201_CREATED)
def registrar_usuario(datos: UsuarioCreate):
    try:
        return usuarios_service.registrar(datos)
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