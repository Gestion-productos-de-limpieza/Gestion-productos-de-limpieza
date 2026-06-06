from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

class UsuarioBase(BaseModel):
    correo: EmailStr = Field(..., description="Correo electrónico del usuario")
    nombre: str = Field(..., description="Nombre completo del usuario")
    rol: str = Field(..., description="Rol asignado (administrador, operador, vendedor, mayorista)")
    estado: str = Field("activo", description="Estado de la cuenta")

class UsuarioCreate(UsuarioBase):
    contrasena: str = Field(..., min_length=8, description="Contraseña segura")

class UsuarioLogin(BaseModel):
    correo: EmailStr
    contrasena: str

class Usuario(UsuarioBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    correo: Optional[str] = None

class UsuarioInDB(Usuario):
    hashed_contrasena: str

class UsuarioResponse(BaseModel):
    id: int
    correo: str
    nombre: str
    rol: str
    estado: str

    model_config = ConfigDict(from_attributes=True)
