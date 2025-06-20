from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class tabla(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorials: str


@app.get("/")
def index():
    return {"message" : "Hola"}

@app.get("/tablas/{id}")
def show_tables(id: int):
    return{"data":id}

@app.post("/tablas")
def insertar_tabla(tabla:tabla):
    return{"message": f"tabla: {tabla.titulo} insertada"}