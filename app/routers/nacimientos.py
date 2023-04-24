from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from typing import Optional
from enum import Enum
from datetime import date, time


router = router = APIRouter()

class Nacimiento(BaseModel):
    id: int
    correlativo: str
    fecha: date
    