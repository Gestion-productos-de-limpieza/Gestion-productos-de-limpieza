from fastapi import FastAPI

app = FastAPI(title="Gestión Productos de Limpieza")

@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}