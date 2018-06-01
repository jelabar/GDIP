from Modelos import *
from GestionBD import *

objeto1 = Prefijo("Nombre")


carr1 = carro('Miata', 'Mazda')
print(carr1.marca)
print(carr1.modelo)

# Crear conexión a BD
bbdd = BaseDatos("ipam.sqlite")

# Lista direcciones de la BD

# Cerrar conexión a la BD para finalizar
bbdd.cerrarBD()
