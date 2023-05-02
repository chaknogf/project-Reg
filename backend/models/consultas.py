from database import database
import mysql.connector
from datetime import datetime


db = database.get_database_connection()

now = datetime.now()

Tconsultas = ('''
  CREATE TABLE IF NOT EXISTS `consultas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `expediente` int DEFAULT NULL,
  `fecha_hora_ingreso` date DEFAULT NULL,
  `nombre_paciente` varchar(50) DEFAULT NULL,
  `especialidad` int(2) DEFAULT NULL,
  `servicio` int(2) DEFAULT NULL,
  `fecha_hora_egrero` date DEFAULT NULL,
  `user` varchar(50) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=myISAM CHARSET=utf8mb4 
''')



def crear_tabla():
    try:
        cursor = db.cursor()
        cursor.execute(Tconsultas)
        db.commit()
        return {"message": "Tabla consultas creada"}
    except mysql.connector.Error as error:
        return {"message": f"Erro al crear Tabla: {error}"}
    finally:
        if db.is_connected():
            cursor.close
            print(f"Tabla consultas datetime:{now} CREADA")
    
    