from fastapi import APIRouter, HTTPException, status
from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse
from app.services.usuariosservices import usuarios_service

router = APIRouter(prefix="/api/v1/users", tags=["Usuarios"])

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
        raise HTTPException(status_code=400, detail=str(e))
