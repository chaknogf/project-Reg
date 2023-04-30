from pydantic import BaseModel, EmailStr
from fastapi import APIRouter, HTTPException
from typing import Optional
from enum import Enum
from datetime import date, datetime
from database import database
import mysql.connector
from .enums import GeneroEnum


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
    nacimiento: date | None = None
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
    


#Get conectado a SQL
@router.get("/pacientes", tags=["Pacientes"])
async def retornar_pacientes():
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    ultimo_exp()
    print(f"** datetime: {now} CONSULTA - GET **")
    return {"pacientes": pacientes}
    

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
        cursor = db.cursor()
        
        query = "INSERT INTO pacientes ( expediente, nombre, apellido, dpi, pasaporte, sexo, nacimiento, nacionalidad, lugar_nacimiento, estado_civil, educacion, pueblo, idioma, ocupacion, direccion, telefono, email, padre, madre, responsable, parentesco, dpi_responsable, telefono_responsable, user) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            Pacient.expediente,
            Pacient.nombre,
            Pacient.apellido,
            Pacient.dpi,
            Pacient.pasaporte,
            Pacient.sexo,
            Pacient.nacimiento,
            Pacient.nacionalidad,
            Pacient.lugar_nacimiento,
            Pacient.estado_civil,
            Pacient.educacion,
            Pacient.pueblo,
            Pacient.idioma,
            Pacient.ocupacion,
            Pacient.direccion,
            Pacient.telefono,
            Pacient.email,
            Pacient.padre,
            Pacient.madre,
            Pacient.responsable,
            Pacient.parentesco,
            Pacient.dpi_responsable,
            Pacient.telefono_responsable,
            Pacient.user
        )
        
       
        cursor.execute(query, values)
        db.commit()
        return {"message": "Se ha creado paciente con exito"}
    except mysql.connector.Error as error:
        return {"message": f"error al crear paciente: {error}"}
    finally:
        if db.is_connected():
            cursor.close()
            print(f"-- Expediente: {Pacient.expediente} datetime: {now} CREADO --")


#Put conectado a SQL
@router.put("/paciente/", tags=["Pacientes"])
async def actualizar_paciente( Pacient: Paciente, exp: int):
    try:
        #buscar_paciente(exp)
        cursor = db.cursor()
        query = "UPDATE pacientes SET nombre = %s, apellido = %s, dpi = %s, pasaporte = %s, sexo = %s, nacimiento = %s, nacionalidad = %s, lugar_nacimiento = %s, estado_civil = %s, educacion = %s, pueblo = %s, idioma = %s, ocupacion = %s, direccion = %s, telefono = %s, email = %s, padre = %s, madre = %s,responsable = %s, parentesco = %s, dpi_responsable = %s, telefono_responsable = %s, user = %s"
        values = (
            Pacient.nombre,
            Pacient.apellido,
            Pacient.dpi,
            Pacient.pasaporte,
            Pacient.sexo,
            Pacient.nacimiento,
            Pacient.nacionalidad,
            Pacient.lugar_nacimiento,
            Pacient.estado_civil,
            Pacient.educacion,
            Pacient.pueblo,
            Pacient.idioma,
            Pacient.ocupacion,
            Pacient.direccion,
            Pacient.telefono,
            Pacient.email,
            Pacient.padre,
            Pacient.madre,
            Pacient.responsable,
            Pacient.parentesco,
            Pacient.dpi_responsable,
            Pacient.telefono_responsable,
            Pacient.user
        )
        cursor.execute(query, values)
        if cursor.rowcount == 0:
            HTTPException(status_code=404, detail="No existen registros{exp}")
        db.commit()
        return {"expediente": exp, **Pacient.dict(), "message": "Actualizado Corecctamente"}
    except mysql.connector.Error as error:
        return {"message": f"Error al consultar paciente: {error}"}
    finally:
        if db.is_connected():
            cursor.close()
            print(f"expediente: {exp} datetime: {now} ACTUALIZADO")

#Delete conectado a SQL
@router.delete("/paciente/{exp}", tags=["Pacientes"])
async def eliminar_paciente(exp: int):
    try:
        cursor = db.cursor()
        path = "DELETE FROM  pacientes WHERE expediente = %s"
        value = [exp]
        cursor.execute(path, value)
        db.commit()
        if cursor.rowcount == 0:
            HTTPException(status_code=404, detail="No existen datos que eliminar {exp}")
        else:
            return {"message": "paciente eliminado correctamente"}
    except mysql.connector.Error as error:
        return {"message": f"Error al eliminar paciente: {error}"}
    finally:
        if db.is_connected():
            cursor.close()
            print(f"Expediente: {exp} datetime:{now} ELIMINADO realizado")



def buscar_paciente(expe: int):
    try:
        cursor = db.cursor()
        value = [expe]
        path = "SELECT * FROM pacientes WHERE expediente = %s"
        cursor.execute(path, value)
        paciente = cursor.fetchone()
        if paciente == None:
            raise HTTPException(status_code=404, detail="No existe registro")
        else:
            return {"paciente": paciente}
    except mysql.connector.Error as error:
        return {"message": f"Error al consultar paciente: {error}"}
    finally:
        if db.is_connected():
            cursor.close()
            print(f"Expediente: {expe} datetime:{now} CONSULTADO")
   
   
   
def buscar_id(id: int):
    try:
        cursor = db.cursor()
        value = [id]
        path = "SELECT * FROM pacientes WHERE id = %s"
        cursor.execute(path, value)
        paciente = cursor.fetchone()
        if paciente == None:
            raise HTTPException(status_code=404, detail="No existe registro")
        else:
            return {"paciente": paciente}
    except mysql.connector.Error as error:
        return {"message": f"Error al consultar paciente: {error}"}
    finally:
        if db.is_connected():
            cursor.close()
            print(f"id: {id} datetime: {now} CONSULTADO")



now = datetime.now()

