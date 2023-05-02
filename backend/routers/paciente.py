from pydantic import BaseModel, EmailStr
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from datetime import date, datetime
from database import database
import mysql.connector
from .enums import GeneroEnum
from database.database import engine, Session, Base
from models.pacientes import PacienteModel


router = APIRouter()


db = database.get_database_connection()
cursor = db.cursor()


def ultimo_exp():
    try:
        
        cursor = db.cursor()
        cursor.execute("SELECT MAX(expediente) FROM pacientes")
        exp = cursor.fetchone()[0]
        if exp == None:
            exp = 0
            return exp
        else:
            return exp
    except mysql.connector.Error as error:
        return {"message": f"error de correlativo: {error}"}
    finally:
        if db.is_connected():
            #cursor.close()
            print(f"Ultimo expediente generado no. {exp}")
            
            
cont: int = (ultimo_exp()+1)


class Paciente(BaseModel):
    #id: int
    expediente: int = cont
    nombre: str
    apellido: str
    dpi: int | None = None
    pasaporte: str | None = None
    sexo: GeneroEnum
    nacimiento: datetime
    nacionalidad: int = 1
    lugar_nacimiento: int | None = None
    estado_civil: int
    educacion: int
    pueblo: int
    idioma: int
    ocupacion: str | None = None
    direccion: str | None = None
    telefono: int | None = None
    email: EmailStr | None = None
    padre: str | None = None
    madre: str | None = None
    responsable: str | None = None
    parentesco: int
    dpi_responsable: int | None = None
    telefono_responsable: int | None = None
    user: str = "admin"
    

    
#Db.metadata.create_all(bind=engine)


#Get conectado a SQL
@router.get("/pacientes", tags=["Pacientes"])
async def retornar_pacientes():
    try:
        ultimo_exp()
    # cursor.execute("SELECT * FROM pacientes")
        #paciente = cursor.fetchall()
        Db = Session()
        result = Db.query(PacienteModel).all()
        print(f"** datetime: {now} CONSULTA - GET **")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except SQLAlchemyError as error:
        return {"message": f"error al consultar paciente: {error}"}
    
        

#Get conectado a SQL
@router.get("/paciente/{exp}", tags=["Pacientes"])
async def obtener_paciente(exp: int):
    return buscar_paciente(exp)

#Get conectado a SQL
@router.get("/paciente/", tags=["Pacientes"])
async def obtener_paciente_id(id: int):
    return buscar_id(id)

#Post conectado a SQL
@router.post("/paciente/{exp}", tags=["Pacientes"])
async def crear_paciente(Pacient: Paciente ):
    try:
        Db = Session()
        nuevo_paciente = PacienteModel(**Pacient.dict())
        Db.add(nuevo_paciente)
        Db.commit()  
        return JSONResponse(status_code=201, content={"message": "Se ha registrado el paciente"})
    except SQLAlchemyError as error:
         return {"message": f"error al crear paciente: {error}"}
        
        


#Put conectado a SQL
@router.put("/paciente/", tags=["Pacientes"])
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
        result.user = Pacient.user
        
      
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

