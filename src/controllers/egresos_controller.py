from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

database = {
    "egresos": [],
}

class Egreso(BaseModel):
    fecha: str
    descripcion: str
    valor: float
    categoria: str

@router.post("/")
async def crear_egreso(egreso: Egreso):
    database["egresos"].append(egreso)
    return {"mensaje": "Egreso creado correctamente"}

@router.get("/")
async def listar_egresos():
    return database["egresos"]

@router.delete("/{egreso_id}")
async def eliminar_egreso(egreso_id: int):
    try:
        del database["egresos"][egreso_id]
        return {"mensaje": "Egreso eliminado correctamente"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Egreso no encontrado")
