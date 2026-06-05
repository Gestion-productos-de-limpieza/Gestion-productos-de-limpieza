from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

# Configuración de seguridad (HU-028)
SECRET_KEY = "tu_clave_secreta_super_segura_para_el_proyecto"  # Cambiar en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Contexto para encriptar contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def obtener_hash_contrasena(contrasena: str) -> str:
    """Encripta la contraseña para guardarla de forma segura (HU-027)"""
    return pwd_context.hash(contrasena)

def verificar_contrasena(contrasena_plana: str, contrasena_hasheada: str) -> bool:
    """Compara la contraseña ingresada con la guardada (HU-028)"""
    return pwd_context.verify(contrasena_plana, contrasena_hasheada)

def crear_token_acceso(data: dict, expires_delta: Optional[timedelta] = None):
    """Genera el token JWT para el inicio de sesión exitoso (HU-028)"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
