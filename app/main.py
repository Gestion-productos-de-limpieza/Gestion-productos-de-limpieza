from fastapi import FastAPI

app = FastAPI(title="Gestion-productos-de-limpieza")

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