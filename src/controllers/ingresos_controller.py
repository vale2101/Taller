from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

database = {
    "ingresos": [],
}

class Ingreso(BaseModel):
    fecha: str
    descripcion: str
    valor: float
    categoria: str

@router.post("/")
async def crear_ingreso(ingreso: Ingreso):
    database["ingresos"].append(ingreso)
    return {"mensaje": "Ingreso creado correctamente"}

@router.get("/")
async def listar_ingresos():
    return database["ingresos"]

@router.delete("/{ingreso_id}")
async def eliminar_ingreso(ingreso_id: int):
    try:
        del database["ingresos"][ingreso_id]
        return {"mensaje": "Ingreso eliminado correctamente"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
