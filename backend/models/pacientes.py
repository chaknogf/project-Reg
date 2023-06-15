from database import database
import mysql.connector
from datetime import datetime
from database import database
from database.database import Base
from sqlalchemy import Column, Integer, String, Date

db = database.get_database_connection()
 
now = datetime.now()

Tpacientes = ('''
   CREATE TABLE IF NOT EXISTS `pacientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `expediente` int DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `dpi` int DEFAULT NULL,
  `pasaporte` varchar(50) DEFAULT NULL,
  `sexo` varchar(2) DEFAULT NULL,
  `nacimiento` date DEFAULT NULL,
  `nacionalidad` int DEFAULT NULL,
  `lugar_nacimiento` int DEFAULT NULL,
  `estado_civil` int DEFAULT NULL,
  `educacion` int DEFAULT NULL,
  `pueblo` int DEFAULT NULL,
  `idioma` varchar(10) DEFAULT NULL,
  `ocupacion` varchar(50) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `telefono` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `padre` varchar(50) DEFAULT NULL,
  `madre` varchar(50) DEFAULT NULL,
  `responsable` varchar(50) DEFAULT NULL,
  `parentesco` int DEFAULT NULL,
  `dpi_responsable` int DEFAULT NULL,
  `telefono_responsable` int DEFAULT NULL,
  `estado` varchar(2) DEFAULT NULL,
  `exp_madre` int DEFAULT NULL,
  `user` varchar(50) DEFAULT NULL,
  `fechaDefuncion` date DEFAULT NULL, 
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `expediente_unico` (`expediente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
''')



def crear_tabla():
    try:
        cursor = db.cursor()
        cursor.execute(Tpacientes)
        db.commit()
        return {"message": "Tabla pacientes creada"}
    except mysql.connector.Error as error:
        return {"message": f"Erro al crear Tabla: {error}"}
    finally:
        if db.is_connected():
            cursor.close
            print(f"Tabla pacientes datetime:{now} CREADA")
    

# Definición del modelo de datos
class PacienteModel(Base):
    __tablename__ = "pacientes"
    
    id = Column(Integer, primary_key=True) 
    expediente = Column(Integer)
    nombre = Column(String(50))
    apellido = Column(String(50))
    dpi = Column(Integer)
    pasaporte = Column(String(50))
    sexo = Column(String(2))
    nacimiento = Column(Date)
    nacionalidad = Column(Integer)
    lugar_nacimiento = Column(Integer)
    estado_civil = Column(Integer)
    educacion = Column(Integer)
    pueblo= Column(Integer)
    idioma = Column(String(10))
    ocupacion = Column(String(50))
    direccion = Column(String(100))
    telefono = Column(Integer)
    email = Column(String(100))
    padre = Column(String(50))
    madre = Column(String(50))
    responsable = Column(String(50))
    parentesco = Column(Integer)
    dpi_responsable = Column(Integer)
    telefono_responsable = Column(Integer)
    estado = Column(String(2))
    exp_madre = Column(Integer)
    user = Column(String(50))
    fechaDefuncion = Column(String)