from fastapi import APIRouter, HTTPException, status
from app.domain.descuentosdomain import DescuentoRequest, DescuentoResponse
from app.services.descuentosservices import descuentos_service

router = APIRouter(
    prefix="/api/v1/sales",
    tags=["Descuentos"],
)


@router.post("/apply-discount", response_model=DescuentoResponse)
def aplicar_descuento(datos: DescuentoRequest):
    try:
        return descuentos_service.aplicar_descuento(datos)
    except LookupError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"codigo": 404, "mensaje": str(e)}
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"codigo": 400, "mensaje": str(e)}
        )
