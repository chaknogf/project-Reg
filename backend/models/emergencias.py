from database import database
import mysql.connector
from datetime import datetime


db = database.get_database_connection()

now = datetime.now()

Temergencias = ('''
   CREATE TABLE IF NOT EXISTS `emergencias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hoja` varchar(10) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `sexo` varchar(2) DEFAULT NULL,
  `telefono` int DEFAULT NULL,
  `dpi` int DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `acompañante` varchar(50) DEFAULT NULL,
  `parentesco` int DEFAULT NULL,
  `comentario` varchar(100) DEFAULT NULL,
  `user` varchar(50) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_hoja` (`hoja`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
''')



def crear_tabla():
    try:
        cursor = db.cursor()
        cursor.execute(Temergencias)
        db.commit()
        return {"message": "Tabla emergencias creada"}
    except mysql.connector.Error as error:
        return {"message": f"Erro al crear Tabla: {error}"}
    finally:
        if db.is_connected():
            cursor.close
            print(f"Tabla emergencias datetime:{now} CREADA")
    
    