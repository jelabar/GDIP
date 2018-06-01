import sqlite3
import datetime


class BaseDatos():

    def __init__(self, Ubicacion):
        ahora = datetime.datetime.now()
        try:
            self.__conexion = sqlite3.connect(Ubicacion)
        except Exception as e:
            print("No se pudo abrir el archivo ", Ubicacion, " por error: ", e)
        else:
            self.__c = self.__conexion.cursor()
            sql_stmt = "INSERT INTO Auditoria (FechaHora, Tipo_Operacion,\
            Operador , Descripcion) VALUES ('"+ahora.strftime('%Y-%m-%d\
            %H:%M:%S')+"',1,'Sistema','Conexión Exitosa')"
            self.__c.execute(sql_stmt)
            self.__conexion.commit()

    def cerrarBD(self):
        self.__conexion.close()

    def insertarRegistro(self, stmt):
        self.__c.execute(stmt)
        self.__conexion.commit()
