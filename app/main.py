from fastapi import FastAPI
from app.api.productosapi import router as productos_router

app = FastAPI(
    title="Gestion-productos-de-limpieza",
    version="1.0.0",
)

app.include_router(productos_router)

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)