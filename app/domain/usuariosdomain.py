from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

ROLES_PERMITIDOS = {"administrador", "operador", "vendedor"}

class UsuarioBase(BaseModel):
    correo: str = Field(..., description="Correo electronico del usuario")
    nombre: str = Field(..., description="Nombre completo del usuario")
    rol:    str = Field(..., description="Rol: administrador, operador o vendedor")
    estado: str = Field("activo", description="Estado de la cuenta")

class UsuarioCreate(BaseModel):
    nombre:     str = Field(..., min_length=2)
    correo:     str = Field(..., description="Correo electronico unico")
    contrasena: str = Field(..., min_length=4)
    rol:        str = Field(..., description="Rol: administrador, operador o vendedor")

class UsuarioResponse(BaseModel):
    id:      int
    nombre:  str
    correo:  str
    rol:     str
    mensaje: str = "Usuario registrado exitosamente"
    model_config = ConfigDict(from_attributes=True)

class UsuarioLogin(BaseModel):
    correo: str
    contrasena: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    correo: Optional[str] = None

<<<<<<< HEAD
class Usuario:
    def __init__(self, id: int, nombre: str, correo: str,
                 contrasena: str, rol: str):
        self.id         = id
        self.nombre     = nombre
        self.correo     = correo
        self.contrasena = contrasena
        self.rol        = rol

    def to_response(self) -> dict:
        return {
            "id":      self.id,
            "nombre":  self.nombre,
            "correo":  self.correo,
            "rol":     self.rol,
            "mensaje": "Usuario registrado exitosamente",
        }
=======
class UsuarioInDB(Usuario):
    hashed_contrasena: str

class UsuarioResponse(BaseModel):
    id: int
    correo: str
    nombre: str
    rol: str
    estado: str

    model_config = ConfigDict(from_attributes=True)
>>>>>>> feat-modulo-productos
