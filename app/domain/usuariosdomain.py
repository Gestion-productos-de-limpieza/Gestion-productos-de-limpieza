from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

# ── SCHEMAS PARA LA API (FastAPI) ──
class UsuarioBase(BaseModel):
    correo: EmailStr = Field(..., description="Correo electrónico")
    nombre: str = Field(..., description="Nombre completo")
    rol: str = Field("cliente", description="Rol asignado")
    estado: str = Field("activo", description="Estado de la cuenta")

class UsuarioCreate(UsuarioBase):
    contrasena: str = Field(..., min_length=8, description="Contraseña segura")

class UsuarioResponse(BaseModel):
    id: int
    correo: EmailStr
    nombre: str
    rol: str
    estado: str
    model_config = ConfigDict(from_attributes=True)

class Usuario(UsuarioBase): # Esto es lo que busca el Router
    id: int
    model_config = ConfigDict(from_attributes=True)

class UsuarioLogin(BaseModel):
    correo: EmailStr
    contrasena: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    correo: Optional[str] = None

# ── CLASE PARA EL REPOSITORIO ──
class UsuarioEntidad: # Esto es lo que busca el Repositorio
    def __init__(self, id: int, nombre: str, correo: str, 
                 contrasena: str, rol: str, estado: str = "activo"):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        self.estado = estado

    def to_response(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "rol": self.rol,
            "estado": self.estado
        }
