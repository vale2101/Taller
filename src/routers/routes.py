from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from src.controllers.ingresos_controller import router as ingresos_router
from src.controllers.egresos_controller import router as egresos_router

router = APIRouter()

# Incluir rutas de ingresos
router.include_router(
    ingresos_router,
    prefix="/ingresos",
    tags=["ingresos"]
)

# Incluir rutas de egresos
router.include_router(
    egresos_router,
    prefix="/egresos",
    tags=["egresos"]
)

database = {
    "ingresos": [],
    "egresos": []
}

class Ingreso(BaseModel):
    fecha: str
    descripcion: str
    valor: float
    categoria: str

class Egreso(BaseModel):
    fecha: str
    descripcion: str
    valor: float
    categoria: str

@router.get("/reporteBasico")
async def generar_reporte_basico():
    totalIngresos = sum(ingreso.valor for ingreso in database["ingresos"])
    totalEgresos = sum(egreso.valor for egreso in database["egresos"])
    balance = totalIngresos - totalEgresos
    return {
        "Total Ingresos": totalIngresos,
        "Total Egresos": totalEgresos,
        "Balance": balance
    }

@router.get("/reporteAmpliado")
async def generar_reporte_ampliado():
    categorias_ingresos = {}
    categorias_egresos = {}

    for ingreso in database["ingresos"]:
        if ingreso.categoria in categorias_ingresos:
            categorias_ingresos[ingreso.categoria] += ingreso.valor
        else:
            categorias_ingresos[ingreso.categoria] = ingreso.valor

    for egreso in database["egresos"]:
        if egreso.categoria in categorias_egresos:
            categorias_egresos[egreso.categoria] += egreso.valor
        else:
            categorias_egresos[egreso.categoria] = egreso.valor

    return {
        "Ingresos Por Categoria": categorias_ingresos,
        "Egresos Por Categoria": categorias_egresos
    }
