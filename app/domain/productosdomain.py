<<<<<<< HEAD
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional

class ProductoCreate(BaseModel):
    nombre:    str   = Field(..., min_length=2, description="Nombre del producto")
    precio:    float = Field(..., gt=0,         description="Precio mayor a 0")
    stock:     int   = Field(..., ge=0,         description="Stock no negativo")
    categoria: str   = Field(..., min_length=2)

    @field_validator("nombre")
    @classmethod
    def nombre_sin_numeros(cls, v: str) -> str:
        if any(c.isdigit() for c in v):
            raise ValueError("El nombre no puede contener números")
        return v.strip().title()

    @field_validator("precio")
    @classmethod
    def precio_valido(cls, v: float) -> float:
        return round(v, 2)


class ProductoResponse(BaseModel):
    id:         int
    nombre:     str
    precio:     float
    stock:      int
    categoria:  str
    disponible: bool

    # Configuración correcta para Pydantic v2 (quitará el error rojo)
    model_config = ConfigDict(from_attributes=True)


class Producto:
    """Clase de entidad para lógica interna y base de datos"""
    def __init__(self, id: int, nombre: str, precio: float,
                 stock: int, categoria: str):
        self.id        = id
        self.nombre    = nombre
        self.precio    = precio
        self.stock     = stock
        self.categoria = categoria

    def tiene_stock(self, cantidad: int = 1) -> bool:
        return self.stock >= cantidad

    def aplicar_descuento(self, porcentaje: float) -> float:
        # Nota: La HU dice que el descuento aplica a compras mayores a $50.000
        if self.precio < 50000:
            raise ValueError("Descuento solo aplica a precios mayores a $50.000")
        return round(self.precio * (1 - porcentaje / 100), 2)

    def to_response(self) -> dict:
        return {
            "id":         self.id,
            "nombre":     self.nombre,
            "precio":     self.precio,
            "stock":      self.stock,
            "categoria":  self.categoria,
            "disponible": self.stock > 0,
        }
=======
from app.domain.usuariosdomain import Usuario
from typing import Optional


class UsuariosRepositories:

    def __init__(self):
        self._datos: list[Usuario] = []
        self._siguiente_id: int = 1

    def obtener_todos(self) -> list[Usuario]:
        return self._datos.copy()

    def obtener_por_id(self, id: int) -> Optional[Usuario]:
        return next((u for u in self._datos if u.id == id), None)

    def obtener_por_correo(self, correo: str) -> Optional[Usuario]:
        return next((u for u in self._datos
                     if u.correo.lower() == correo.lower()), None)

    def crear(self, nombre: str, correo: str,
              contrasena: str, rol: str) -> Usuario:
        nuevo = Usuario(
            id         = self._siguiente_id,
            nombre     = nombre,
            correo     = correo,
            contrasena = contrasena,
            rol        = rol,
        )
        self._datos.append(nuevo)
        self._siguiente_id += 1
        return nuevo


# Instancia única compartida
usuario_repository = UsuariosRepositories()
>>>>>>> b2a11d8ea970c53180ef488dce1a7e3bdacb3e55
