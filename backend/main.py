from fastapi import FastAPI
from routers import paciente, emergencia, consulta
#from fastapi.staticfiles import StaticFiles
from models import pacientes, emergencias, consultas
from fastapi.middleware.cors import CORSMiddleware
from middlewares.error_hendler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer

app = FastAPI()
app.add_middleware(ErrorHandler)

origenes_permitidos = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origenes_permitidos,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/crearTablas', tags=["SQL"])
def crear_tablas():
    p = pacientes.crear_tabla()
    e = emergencias.crear_tabla()
    c = consultas.crear_tabla()
    return {f"{p} {e} {c}"}

#importacion de routers

app.include_router(paciente.router)
app.include_router(emergencia.router)
app.include_router(consulta.router)
'''
app.include_router(usuarios.router)

app.include_router(nacimientos.router)
app.include_router(consultas.router)

'''

@app.get("/")
async def root():
    return "Hola FastAPi \n ingresa a  http://127.0.0.1:8000/docs para ver la documentación"