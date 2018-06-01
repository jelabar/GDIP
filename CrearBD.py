import sqlite3

def CreateDB(Nombre,Ruta)
    conexion = sqlite3.connect(Ruta+Nombre)
    c=conexion.cursor()
    c.execute('''CREATE TABLE redes (date text, trans text, symbol text, qty real, price real)''')
    conexion.commit()
    conexion.close()
