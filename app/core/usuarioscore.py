from passlib.context import CryptContext

# Cambiamos a PBKDF2 para eliminar el error técnico de los 72 bytes de Bcrypt
# Este método es igual de seguro y mucho más compatible
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"], 
    deprecated="auto"
)


def obtener_hash_contrasena(contrasena: str) -> str:
    """Encripta la contraseña de forma segura"""
    if not contrasena:
        return ""
    return pwd_context.hash(str(contrasena))

def verificar_contrasena(contrasena_plana: str, contrasena_hasheada: str) -> bool:
    """Compara la contraseña plana con el hash guardado"""
    try:
        if not contrasena_hasheada:
            return False
        return pwd_context.verify(str(contrasena_plana), str(contrasena_hasheada))
    except Exception:
        # Si el hash viejo era Bcrypt y falla, devolvemos False para forzar nuevo registro
        return False
