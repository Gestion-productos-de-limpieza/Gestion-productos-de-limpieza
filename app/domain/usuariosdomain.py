from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

# ── CONSTANTES ────────────────────────────────────────────────
ROLES_PERMITIDOS = {"administrador", "operador", "vendedor", "mayorista", "cliente"}


# ── SCHEMAS PYDANTIC (FastAPI) ────────────────────────────────
class UsuarioBase(BaseModel):
    correo: EmailStr = Field(..., description="Correo electrónico del usuario")
    nombre: str      = Field(..., description="Nombre completo del usuario")
    rol:    str      = Field("cliente", description="Rol: administrador, operador, vendedor, mayorista o cliente")
    estado: str      = Field("activo",  description="Estado de la cuenta")


class UsuarioCreate(UsuarioBase):
    contrasena: str = Field(..., min_length=8, description="Contraseña segura")


class UsuarioResponse(BaseModel):
    id:     int
    correo: EmailStr
    nombre: str
    rol:    str
    estado: str
    model_config = ConfigDict(from_attributes=True)


class UsuarioListItem(BaseModel):
    id:     int
    nombre: str
    correo: EmailStr
    rol:    str
    estado: str
    model_config = ConfigDict(from_attributes=True)


class UsuarioLogin(BaseModel):
    correo:     str
    contrasena: str


class Token(BaseModel):
    access_token: str
    token_type:   str


class TokenData(BaseModel):
    correo: Optional[str] = None


# ── ENTIDAD DE DOMINIO (Repositorio) ─────────────────────────
class UsuarioEntidad:
    def __init__(self, id: int, nombre: str, correo: str,
                 contrasena: str, rol: str, estado: str = "activo"):
        self.id         = id
        self.nombre     = nombre
        self.correo     = correo
        self.contrasena = contrasena
        self.rol        = rol
        self.estado     = estado

    def to_response(self) -> dict:
        return {
            "id":     self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "rol":    self.rol,
            "estado": self.estado,
        }

    def to_list_item(self) -> dict:
        return {
            "id":     self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "rol":    self.rol,
            "estado": self.estado,
        }