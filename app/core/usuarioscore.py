from fastapi import APIRouter, HTTPException, status
from app.domain.usuariosdomain import UsuarioCreate, UsuarioResponse
from app.core.usuarioscore import obtener_hash_contrasena  # IMPORTANTE: Conectamos con el Core

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Usuarios"]
)

# Base de datos temporal (luego usaremos Repositories)
db_usuarios_temp = []

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def registrar_usuario(usuario: UsuarioCreate):
    """
    Endpoint para registrar un nuevo usuario (HU-01)
    """
    # 1. Verificar si el usuario ya existe por email
    for u in db_usuarios_temp:
        if u["email"] == usuario.email:
            raise HTTPException(
                status_code=400, 
                detail="El correo electrónico ya está registrado"
            )
    
    # 2. ENCRIPTAR LA CONTRASEÑA (Aquí usamos el Core)
    hashed_password = obtener_hash_contrasena(usuario.password)
    
    # 3. Crear el nuevo usuario con la contraseña segura
    nuevo_usuario = {
        "id": len(db_usuarios_temp) + 1,
        "username": usuario.username,
        "email": usuario.email,
        "password": hashed_password,  # Guardamos el hash, no la clave real
        "rol": usuario.rol or "vendedor",
        "activo": True
    }
    
    db_usuarios_temp.append(nuevo_usuario)
    
    # 4. Retornar la respuesta (Pydantic filtrará la contraseña automáticamente)
    return nuevo_usuario
