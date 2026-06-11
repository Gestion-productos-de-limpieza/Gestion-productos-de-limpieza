# ─────────────────────────────────────────────────────────────
# CAPA API — rutas HTTP con FastAPI
# Solo recibe peticiones y llama al servicio.
# ─────────────────────────────────────────────────────────────

from fastapi import APIRouter, HTTPException, status
from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse
from app.services.usuariosservices import usuarios_service

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Usuarios"]
)

# ── 1. REGISTRAR USUARIO (HU-01) ──────────────────────────────
@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def registrar_usuario(usuario: UsuarioCreate):
    try:
        u_resp = usuarios_service.registrar(usuario)
        return {
            "mensaje": "Usuario registrado exitosamente",
            "usuario": u_resp,
            "success": True
        }
    except ValueError as e:
        # Error 400 por datos inválidos o correo duplicado
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# ── 2. LISTAR USUARIOS (HU-02) ───────────────────────────────
@router.get("/", response_model=list[UsuarioResponse])
async def listar_usuarios():
    return usuarios_service.listar()

# ── 3. ACTUALIZAR USUARIO (HU-03) ────────────────────────────
@router.put("/{id}", response_model=UsuarioResponse)
async def actualizar_usuario(id: int, usuario: UsuarioCreate):
    try:
        return usuarios_service.actualizar(id, usuario)
    except ValueError as e:
        # Error 404 si el usuario no existe
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

# ── 4. ELIMINAR USUARIO (Criterios de Aceptación) ────────────
@router.delete("/{id}", response_model=dict)
async def eliminar_usuario(id: int, current_user_id: int = 1): 
    """
    Endpoint para eliminar un usuario. 
    'current_user_id' simula el ID del administrador logueado.
    """
    try:
        return usuarios_service.eliminar(id, current_user_id)
    except PermissionError as e:
        # CRITERIO: Error 403 Forbidden por intentar eliminar al propio usuario activo
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
    except ValueError as e:
        # CRITERIO: Error 404 Not Found si el usuario no existe
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
