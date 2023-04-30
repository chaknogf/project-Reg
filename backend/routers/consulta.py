from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from typing import Optional
from enum import Enum
from datetime import date, time, datetime
from database import database
import mysql.connector


router = router = APIRouter()

db = database.get_database_connection()


class Consulta(BaseModel):
    expediente: int
    fecha_hora_ingreso: datetime
    nombre_paciente: str
    especialidad: int
    servicio: int
    fecha_hora_egreso: datetime
    user: str | None = None
    
    
@router.get("/consultas", tags=["Consultas"])
async def consultas():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM consultas")
    consultas = cursor.fetchall()
    return {"consultas": consultas}
    