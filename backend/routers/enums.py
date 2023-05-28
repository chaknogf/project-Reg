from pydantic import BaseModel
from enum import Enum
from typing import Optional
import sys
sys.path.append("/ruta/al/directorio")


class GeneroEnum(str, Enum):
    Masculino = 'M'
    Femenino = 'F'
    
class EstadoEnum(str, Enum):
    Vivo = 'v'
    Muerto = 'm'
    
    
class PuebloEnum(int, Enum):
    Ladino = 1
    Maya = 2
    Garífuna = 3
    Xinca = 4
    Otros = 5
    No_indica = 6
    
class IdiomaEnum(int, Enum):
    Achi = 1
    Akateka = 2
    Awakateka = 3
    Chorti = 4
    Chalchiteka = 5
    Chuj = 6
    Itza = 7 
    Ixil = 8
    Jakalteka = 9
    Kaqchikel = 10
    Kiche = 11
    Mam = 12
    Mopan = 13
    Poqomam = 14 
    Pocomchi = 15
    Qanjobal = 16
    Qeqchi = 17
    Sakapulteka = 18
    Sipakapensa = 19
    Tektiteka = 20
    Tzutujil = 21
    Uspanteka = 22 
    No_indica = 23
    Español = 24 

class DiscapacidadEnum(int, Enum):
    No_aplica = 0
    Fisica = 1
    Mental = 2
    Visual = 3
    Auditiva = 4
    Otra = 5

class OrientacionSexualEnum(int, Enum):
    No_aplica = 0
    Heterosexual = 1
    Bisexual = 2
    Homosexual = 3
    Trans = 4
    Otro = 5
    
class EstudiosEnum(int, Enum):
    No_aplica = 1
    Pre_Primaria = 2
    Primaria = 3
    Básicos = 4
    Diversificado = 5
    Universidad = 6
    Ninguno = 7
    Otro = 8
    No_indica = 9
    
class ParentescoEnum(int, Enum):
    Madre = 0
    Padre = 1
    hijo_a = 2
    abuelo_a = 3
    tio_a = 4
    primo_a = 5
    sobrino_a = 6
    yerno = 7
    nuera = 8
    suegro_a = 9
    tutor = 10
    amistad = 11
    otro = 12
    
class EstadoCivilEnum(int, Enum):
    casado = 1
    unido = 2
    soltero = 3
    
class LugarNacimiento(int, Enum):
    Guatemala = 101
    

class nacionalidadEnum(int, Enum):
     
    Guatemalteca = 1
    Beliceña = 2
    Salvadoreña = 3
    Hondureña = 4
    Nicaragüense = 5
    Costarricense = 6
    Panameña = 7
    Mexicana = 8
    Otro_pais = 9
   
    
    