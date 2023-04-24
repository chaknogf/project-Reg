from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from typing import Optional
from enum import Enum
from datetime import date, time
from database import database
import mysql.connector


router = router = APIRouter()

db = database.get_database_connection()


class Genero(str, Enum):
    Masculino = 'M'
    Femenino = 'F'
 
class Emergnecia(BaseModel):
    #id: int
    hoja: str
    fecha: date 
    hora: time = "00:00"
    nombre: str
    apellido: str
    fecha_nacimiento: date
    sexo: Genero
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
    #db
    cursor = db.cursor()
    cursor.execute("SELECT * FROM emergencias")
    emergencias = cursor.fetchall()
    #db.close()
    return {"emeregencias": emergencias}
   # return hojas_list

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
        #hojas_list.append(Emergency)
        cursor = db.cursor()
        query = "INSERT INTO emergencias (hoja, fecha, hora, nombre, apellido, fecha_nacimiento, sexo, telefono, dpi, direccion, acompañante, parentesco, comentario, user) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            
            Emergency.hoja,
            Emergency.fecha, 
            Emergency.hora, 
            Emergency.nombre, 
            Emergency.apellido, 
            Emergency.fecha_nacimiento, 
            Emergency.sexo, 
            Emergency.telefono, 
            Emergency.dpi,
            Emergency.direccion,
            Emergency.acompañante,
            Emergency.parentesco,
            Emergency.comentario,
            Emergency.user
        )
        cursor.execute(query, values)
        db.commit()
        return {"message:" "Se agrego consulta con exito"}
    except mysql.connector.Error as error:
        return {"message": f"Error al insertar la emergencia: {error}"}
    finally:
        if db.is_connected():
            cursor.close()
            

#Put conectado a SQL
@router.put("/emergencia/", tags=["Hoja de Emergencias"])
async def actualizar_consulta(Emergency: Emergnecia, hoja: str):

    try:
        
        find_emergency(hoja)
        cursor = db.cursor()
        query = "UPDATE emergencias SET fecha = %s, hora = %s, nombre = %s, apellido = %s, fecha_nacimiento = %s, sexo = %s, telefono = %s, dpi = %s, direccion = %s, acompañante = %s, parentesco = %s, comentario = %s, user = %s"
        value = (Emergency.fecha,
                Emergency.hora,
                Emergency.nombre,
                Emergency.apellido,
                Emergency.fecha_nacimiento,
                Emergency.sexo,
                Emergency.telefono,
                Emergency.dpi,
                Emergency.direccion,
                Emergency.acompañante,
                Emergency.parentesco,
                Emergency.comentario,
                Emergency.user
                )
        cursor.execute(query, value)
        if cursor.rowcount == 0:
             HTTPException(status_code=404,detail=f"No existen datos{hoja}")
        db.commit()
        return {"hoja": hoja, **Emergency.dict(), "message": "Registro actualizado" }
    except mysql.connector.Error as error:
        return {"message": f"Error al consultar la emergencia: {error}"}
    
    finally:
        if db.is_connected():
            cursor.close

@router.delete("/emergencia/{hoja}", tags=["Hoja de Emergencias"])
async def eliminar_hoja(hoja: str):
    try:
        cursor = db.cursor()
        path = "DELETE FROM  emergencias WHERE hoja = %s"
        value = [hoja]
        cursor.execute(path, value)
        db.commit()
        if cursor.rowcount == 0:
            HTTPException(status_code=404,detail=f"No existen datos que eliminar{hoja}")
            print ("No hay datos")
        else:
            return {"message": "Registro eliminado correctamente"}
    except mysql.connector.Error as error:
        return {"message": f"Error al eliminar la emergencia: {error}"}
        
    finally:
        if db.is_connected():
            cursor.close()
            print("Conexión a MySQL cerrada.")


        
def find_emergency(hoja: str):
    try:
        
        cursor = db.cursor()
        value = [hoja]
        path = "SELECT * FROM emergencias WHERE hoja = %s"
        cursor.execute(path, value)
       
        emergencia = cursor.fetchone() 
        if emergencia == None:
            raise HTTPException(status_code=404, detail="No existe el registro")     
        else:  
            return {"emeregencia": emergencia}
            
    except mysql.connector.Error as error:
        return {"message": f"Error al consultar la emergencia: {error}"}
        #db.close()
    finally:
        if db.is_connected():
            cursor.close()
    
        
def buscarx_id(idx: int):
    try:
        cursor = db.cursor()
        value = [idx]
        path = "SELECT * FROM emergencias WHERE id = %s"
        
        cursor.execute(path, value)
        emergencia = cursor.fetchall()
        if emergencia == []:
            return {"message": "No existe registros"}     
        else:  
            return {"emeregencia": emergencia}
        
    except mysql.connector.Error as error:
        return {"message": f"Error al consultar la emergencia: {error}"}
        #db.close()
    finally:
        if db.is_connected():
            cursor.close()
