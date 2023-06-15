from pydantic import BaseModel, EmailStr
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import func,select
from sqlalchemy.exc import SQLAlchemyError
from datetime import date, datetime
from database import database
import mysql.connector
from .enums import GeneroEnum, EstadoEnum
from database.database import engine, Session, Base
from models.pacientes import PacienteModel


router = APIRouter()


db = database.get_database_connection()
cursor = db.cursor()


ultimo_expediente = 0

def actualizar_ultimo_exp():
    try:
        Db = Session()
        max_exp = Db.execute(select(func.max(PacienteModel.expediente))).scalar()
        New_exp = max_exp + 1
        Db.close()
        return New_exp
        
    except SQLAlchemyError as error:
        return {"message": f"error al consultar paciente: {error}"}
    finally:
        print(f"Ultimo expediente generado no. {max_exp}")
            
            
cont: int 


class Paciente(BaseModel):
    #id: int
    expediente: int
    nombre: str | None = None
    apellido: str| None = None
    dpi: int | None = None
    pasaporte: str | None = None
    sexo: GeneroEnum | None = None
    nacimiento: date | None = None
    nacionalidad: int = 1
    lugar_nacimiento: int | None = None
    estado_civil: int | None = None
    educacion: int | None = None
    pueblo: int | None = None
    idioma: str | None = None
    ocupacion: str | None = None
    direccion: str | None = None
    telefono: int | None = None
    email: EmailStr | None = None
    padre: str | None = None
    madre: str | None = None
    responsable: str | None = None
    parentesco: int | None = None
    dpi_responsable: int | None = None
    telefono_responsable: int | None = None
    estado: EstadoEnum| None = None
    exp_madre: int | None = None
    user: str | None = None
    fechaDefuncion: str | None = None
    

        

    
#Db.metadata.create_all(bind=engine)

@router.get("/expediente")
async def obtener_ultimo_expediente():
    result = actualizar_ultimo_exp()
    return result


#Get conectado a SQL
@router.get("/pacientes", tags=["Pacientes"])
async def retornar_pacientes():
    try:
        #ultimo_expediente()
        Db = Session()
        result = Db.query(PacienteModel).all()
        print(f"** datetime: {now} CONSULTA - GET **")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except SQLAlchemyError as error:
        return {"message": f"error al consultar paciente: {error}"}
    finally:
        print(f"CONSULTADO datetime: {now} ")
    
        

#Get conectado a SQL
@router.get("/paciente/{exp}", tags=["Pacientes"])
async def obtener_paciente(exp: int):
    return buscar_paciente(exp)

#Get conectado a SQL
@router.get("/paciente/", tags=["Pacientes"])
async def obtener_paciente_id(id: int):
    return buscar_id(id)

#Post conectado a SQL
@router.post("/paciente/", tags=["Pacientes"])
async def crear_paciente(Pacient: Paciente ):
    try:
        Db = Session()
        nuevo_paciente = PacienteModel(**Pacient.dict())
        Db.add(nuevo_paciente)
        Db.commit()  
        actualizar_ultimo_exp()
        cursor.close()
        return JSONResponse(status_code=201, content={"message": "Se ha registrado el paciente"})
    except SQLAlchemyError as error:
         return {"message": f"error al crear paciente: {error}"}
        
        


#Put conectado a SQL
@router.put("/paciente/{exp}", tags=["Pacientes"])
async def actualizar_paciente( Pacient: Paciente, exp: int):
    try:
        Db = Session()
        result = Db.query(PacienteModel).filter(PacienteModel.expediente == exp).first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "No encontrado"})
        #result.expediente = Pacient.expediente
        result.nombre = Pacient.nombre
        result.apellido = Pacient.apellido
        result.dpi = Pacient.dpi
        result.pasaporte = Pacient.pasaporte
        result.sexo = Pacient.sexo
        result.nacimiento = Pacient.nacimiento
        result.nacionalidad = Pacient.nacionalidad
        result.lugar_nacimiento = Pacient.lugar_nacimiento
        result.estado_civil = Pacient.estado_civil
        result.educacion = Pacient.educacion
        result.pueblo = Pacient.pueblo
        result.idioma = Pacient.idioma
        result.ocupacion = Pacient.ocupacion
        result.direccion = Pacient.direccion
        result.telefono = Pacient.telefono
        result.email = Pacient.email
        result.padre = Pacient.padre
        result.madre = Pacient.madre
        result.responsable = Pacient.responsable
        result.parentesco = Pacient.parentesco
        result.dpi_responsable = Pacient.dpi_responsable
        result.telefono_responsable = Pacient.telefono_responsable
        result.estado = Pacient.estado
        result.exp_madre = Pacient.exp_madre
        result.user = Pacient.user
        result.fechaDefuncion = Pacient.fechaDefuncion
        
      
        Db.commit()
        return JSONResponse(status_code=201, content={"message": "Actualización Realizada"})
    except SQLAlchemyError as error:
        return {"message": f"Error al consultar paciente: {error}"}
    finally: 
            print(f"expediente: {exp} datetime: {now} ACTUALIZADO")

#Delete conectado a SQL
@router.delete("/paciente/{exp}", tags=["Pacientes"])
async def eliminar_paciente(exp: int):
    try:
        Db = Session()
        result = Db.query(PacienteModel).filter(PacienteModel.expediente == exp).first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "No encontrado"})
        Db.delete(result)
        Db.commit()
        return JSONResponse(status_code=200, content={"message": "Eliminado con exito"})
    except SQLAlchemyError as error:
        return {"message": f"Error al consultar paciente: {error}"}
    finally:
            print(f"Expediente: {exp} datetime:{now} ELIMINADO realizado")



def buscar_paciente(expe: int):
    try:
        Db = Session()
        result = Db.query(PacienteModel).filter(PacienteModel.expediente == expe).first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "No encontrado"})
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except SQLAlchemyError as error:
        return {"message": f"Error al consultar paciente: {error}"}
    finally:
        print(f"Expediente: {expe} datetime:{now} CONSULTADO")
   
   
   
def buscar_id(id: int):
    try:
        Db = Session()
        result = Db.query(PacienteModel).filter(PacienteModel.id == id).first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "No encontrado"})
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except SQLAlchemyError as error:
        return {"message": f"Error al consultar paciente: {error}"}
    finally:
        print(f"id: {id} datetime:{now} CONSULTADO")
           


now = datetime.now()

