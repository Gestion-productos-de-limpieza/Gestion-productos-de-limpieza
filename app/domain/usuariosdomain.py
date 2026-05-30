# ─────────────────────────────────────────────────────────────
# CAPA DOMINIO — define la entidad y sus reglas de negocio
# No importa nada de FastAPI ni de base de datos aquí.
# ─────────────────────────────────────────────────────────────

from pydantic import BaseModel, Field, field_validator
from typing import Optional


# ── Roles permitidos ──────────────────────────────────────────
ROLES_PERMITIDOS = {"administrador", "operador", "vendedor"}


# ── Schema de ENTRADA (lo que recibe la API del cliente) ──────
class UsuarioCreate(BaseModel):
    nombre:     str = Field(..., min_length=2, description="Nombre completo del usuario")
    correo:     str = Field(..., description="Correo electrónico único")
    contrasena: str = Field(..., min_length=4, description="Contraseña del usuario")
    rol:        str = Field(..., description="Rol: administrador, operador o vendedor")

    @field_validator("correo")
    @classmethod
    def correo_valido(cls, v):
        v = v.strip().lower()
        if "@" not in v or "." not in v.split("@")[-1]:
            raise ValueError("El correo no tiene un formato válido")
        return v

    @field_validator("rol")
    @classmethod
    def rol_valido(cls, v):
        v = v.strip().lower()
        if v not in ROLES_PERMITIDOS:
            raise ValueError(f"El rol debe ser uno de: {', '.join(ROLES_PERMITIDOS)}")
        return v

    @field_validator("nombre")
    @classmethod
    def nombre_valido(cls, v):
        return v.strip().title()


# ── Schema de SALIDA (lo que devuelve la API — sin contraseña) ─
class UsuarioResponse(BaseModel):
    id:      int
    nombre:  str
    correo:  str
    rol:     str
    mensaje: str = "Usuario registrado exitosamente"

    class Config:
        from_attributes = True


# ── Modelo interno del dominio (entidad real) ─────────────────
class Usuario:
    def __init__(self, id: int, nombre: str, correo: str,
                 contrasena: str, rol: str):
        self.id         = id
        self.nombre     = nombre
        self.correo     = correo
        self.contrasena = contrasena  # en producción iría hasheada
        self.rol        = rol

    def to_response(self) -> dict:
        return {
            "id":      self.id,
            "nombre":  self.nombre,
            "correo":  self.correo,
            "rol":     self.rol,
            "mensaje": "Usuario registrado exitosamente",
        }