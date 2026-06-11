from fastapi import APIRouter, HTTPException, status
from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse
from app.core.usuarioscore import obtener_hash_contrasena  # Importamos del Core

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Usuarios"]
)

db_usuarios_temp = []

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def registrar_usuario(usuario: UsuarioCreate):
    # 1. Verificar duplicados
    for u in db_usuarios_temp:
        if u.get("correo") == usuario.correo:
            raise HTTPException(status_code=400, detail="El correo ya existe")
    
    # 2. Usar la función que está en el CORE
    hashed_password = obtener_hash_contrasena(usuario.contrasena)
    
    # 3. Crear usuario
    nuevo_usuario = {
        "id": len(db_usuarios_temp) + 1,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "contrasena": hashed_password,
        "rol": usuario.rol or "vendedor",
        "estado": usuario.estado or "activo"
    }

    
    db_usuarios_temp.append(nuevo_usuario)
    return nuevo_usuario

@router.get("/", response_model=list[UsuarioResponse])
async def listar_usuarios():
    return usuarios_service.listar()


@router.delete("/{id}", response_model=dict)
async def eliminar_usuario(id: int):
    try:
        return usuarios_service.eliminar(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

