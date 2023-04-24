from fastapi import FastAPI
from routers import paciente, emergencia
#from fastapi.staticfiles import StaticFiles
from models import pacientes, emergencias




app = FastAPI()


@app.get('/crearTablas')
def crear_tablas():
    p = pacientes.crear_tabla()
    e = emergencias.crear_tabla()
    return {f"{p} {e}"}

#importacion de routers

app.include_router(paciente.router)
app.include_router(emergencia.router)
'''
app.include_router(usuarios.router)

app.include_router(nacimientos.router)
app.include_router(consultas.router)

'''

@app.get("/")
async def root():
    return "Hola FastAPi \n ingresa a  http://127.0.0.1:8000/docs para ver la documentación"