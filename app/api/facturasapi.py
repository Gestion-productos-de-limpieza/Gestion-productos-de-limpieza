from fastapi import APIRouter, HTTPException, status, Header
from typing import Optional
from app.domain.facturasdomain import FacturaCreate, FacturaResponse, FacturaListItem
from app.services.facturasservices import facturas_service

router = APIRouter(
    prefix="/api/v1/facturas",
    tags=["Facturas"],
)


# ── POST /api/v1/facturas/ — Registrar factura ────────────────
@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def registrar_factura(datos: FacturaCreate):
    try:
        f_resp = facturas_service.registrar(datos)
        return {
            "mensaje": "Factura registrada exitosamente",
            "factura": f_resp,
            "success": True
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"codigo": 400, "mensaje": str(e)}
        )


# ── GET /api/v1/facturas/ — Listar facturas ───────────────────
@router.get("/")
def listar_facturas(
    x_user_role: Optional[str] = Header(default=None)
):
    if x_user_role is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"codigo": 401, "mensaje": "Usuario no autenticado"}
        )
    if x_user_role.lower() != "administrador":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"codigo": 403, "mensaje": "No tiene permisos para listar facturas"}
        )
    try:
        facturas = facturas_service.listar()
        return {
            "codigo": 200,
            "facturas": [f.model_dump() for f in facturas]
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"codigo": 404, "mensaje": str(e)}
        )


# ── DELETE /api/v1/facturas/{id} — Eliminar factura ───────────
@router.delete("/{id}", response_model=dict)
def eliminar_factura(
    id: int,
    x_user_role: Optional[str] = Header(default=None)
):
    if x_user_role is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"codigo": 401, "mensaje": "Usuario no autenticado"}
        )
    if x_user_role.lower() != "administrador":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"codigo": 403, "mensaje": "No tiene permisos para eliminar facturas"}
        )
    try:
        return facturas_service.eliminar(id)
    except PermissionError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"codigo": 403, "mensaje": str(e)}
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"codigo": 404, "mensaje": str(e)}
        )