from passlib.context import CryptContext

# 1. Configuración de encriptación
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. Funciones de seguridad
def obtener_hash_contrasena(contrasena: str) -> str:
    """Encripta la contraseña para guardarla de forma segura (HU-01)"""
    return pwd_context.hash(contrasena)

def verificar_contrasena(contrasena_plana: str, contrasena_hasheada: str) -> bool:
    """Compara la contraseña ingresada con la guardada"""
    return pwd_context.verify(contrasena_plana, contrasena_hasheada)
