from fastapi import FastAPI
# Importamos tu router de productos
from app.api.productosapi import router as products_router

app = FastAPI(title="Gestion-productos-de-limpieza")

# Mantenemos lo que hizo tu compañero
@app.get("/")
def root():
    return {"message": "Servidor funcionando correctamente"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "1.0.0",
        "environment": "development"
    }

# --- AGREGAMOS TU TRABAJO AQUÍ ---
# Esto conecta tus capas de Productos a la API
app.include_router(products_router)
