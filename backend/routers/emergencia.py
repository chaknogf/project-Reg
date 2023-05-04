from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from .enums import GeneroEnum
from database.database import engine, Session, Base
from datetime import date, time, datetime
from database import database
import mysql.connector
from models.emergencias import EmergenciaModel


router = router = APIRouter()

db = database.get_database_connection()
Db = Session()
now = datetime.now()
 
class Emergnecia(BaseModel):
    #id: int
    hoja: str
    fecha: date 
    hora: time = "00:00"
    nombre: str
    apellido: str
    fecha_nacimiento: date
    sexo: GeneroEnum
    telefono: int
    dpi: int
    direccion: str
    acompañante: str | None = None
    parentesco: int | None = None
    comentario: str | None = None
    user: str = 'admin'


#Get conectado a SQL
@router.get('/emergencias', tags=["Hoja de Emergencias"])
async def obtener_hojas():
    try:
        result = Db.query(EmergenciaModel).all()
        print(f"** datetime: {now} CONSULTA - GET **")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except SQLAlchemyError as error:
        return {"message": f"error al consultar datos: {error}"}
    finally:
        print(f"CONSULTADO datetime: {now} ")
      

#Get conectado a SQL
@router.get('/emergencia/{hoja}', tags=["Hoja de Emergencias"])
async def obtener_hoja(hoja: str):
    return find_emergency(hoja)

#Get conectado a SQL
@router.get('/emergencia/', tags=["Hoja de Emergencias"])
async def obtener_hoja_id(id: int):
    return buscarx_id(id)
    
#Post conectado a SQL
@router.post("/emergencia/", tags=["Hoja de Emergencias"])
async def registrar_consulta(Emergency: Emergnecia ):
    try:
        nueva_hoja = EmergenciaModel(**Emergency.dict())
        Db.add(nueva_hoja)
        Db.commit()
        return JSONResponse(status_code=201, content={"message": "Se ha registrado la Emergencia"})
    except SQLAlchemyError as error:
        return {"message": f"Error al insertar la emergencia: {error}"}
    finally:
        print (f"Emergencia creada datetime {now}")

#Put conectado a SQL
@router.put("/emergencia/", tags=["Hoja de Emergencias"])
async def actualizar_consulta(Emergency: Emergnecia, hoja: str):

    try:
        result = Db.query(EmergenciaModel).filter(EmergenciaModel.hoja == hoja).first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "No encontrado"})
        result.hoja = Emergency.hoja
        result.fecha = Emergency.fecha,
        result.hora = Emergency.hora,
        result.nombre = Emergency.nombre,
        result.apellido = Emergency.apellido,
        result.fecha_nacimiento = Emergency.fecha_nacimiento,
        result.sexo = Emergency.sexo,
        result.telefono =  Emergency.telefono,
        result.dpi = Emergency.dpi,
        result.direccion = Emergency.direccion,
        result.acompañante = Emergency.acompañante,
        result.parentesco = Emergency.parentesco,
        result.comentario = Emergency.comentario,
        result.user = Emergency.user
        
        HTTPException(status_code=404,detail=f"No existen datos{hoja}")
        Db.commit()
        return JSONResponse(status_code=201, content={"message": "Actualización realizada"})
    except SQLAlchemyError as error:
        return {"message": f"Error al consultar la emergencia: {error}"}
    finally:
        print(f"Emergencia: {hoja} datetime: {now} ACTUALIZADO")

@router.delete("/emergencia/{hoja}", tags=["Hoja de Emergencias"])
async def eliminar_hoja(hoja: str):
    try:
        result = Db.query(EmergenciaModel).filter(EmergenciaModel.hoja == hoja).first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "No existen datos que eliminar"})
        Db.delete(result)
        Db.commit()
    except SQLAlchemyError as error:
        return {"message": f"Error al eliminar la emergencia: {error}"}
        
    finally:
        print(f"Emergencia: {hoja} datetime: {now} ELIMINADO")


        
def find_emergency(hoja: str):
    try:
        result = Db.query(EmergenciaModel).filter(EmergenciaModel.hoja == hoja).first()
        if not result:
            raise HTTPException(status_code=404, detail="No existe el registro")     
        else:  
            return JSONResponse(status_code=200, content=jsonable_encoder(result))
            
    except SQLAlchemyError as error:
        return {"message": f"Error al consultar la emergencia: {error}"}
    finally:
        print(f"Hoja_de_Emergencia: {hoja} datetime: {now} CONSULTADA")
    
        
def buscarx_id(idx: int):
    try:
        result = Db.query(EmergenciaModel).filter(EmergenciaModel.id == id).first()
        if not result:
            raise HTTPException(status_code=404, detail="No existe el registro")     
        else:  
            return JSONResponse(status_code=200, content=jsonable_encoder(result))
            
    except SQLAlchemyError as error:
        return {"message": f"Error al consultar la emergencia: {error}"}
    finally:
        print(f"Hoja_de_Emergencia: {id} datetime: {now} CONSULTADA")
