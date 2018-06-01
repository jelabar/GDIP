import datetime
import netaddr
# Agrega direcciones IP
# Puedo tomar este elemento para saber el padre de las IP que están ocupadas.


class Agregado():
    def __init__(self, *args, **kwargs):
        self.__fecha_creacion = datetime.datetime.now()
        self.__fecha_actualizacion
        self.__familia
        self.__prefijo
        self.__rir
        self.__fecha_agregada
        self.__descripcion

    def Extender():
        print('Se extiende el objeto red')

    def Reducir():
        print('Se reduce el objeto red')

    def ComprobarReduccion():
        print('Se puede reducir')

    # Trae el listado de redes guardadas en la BD.
    def listarRedes():
        return 1


class DireccionIP():
    # Es un objeto que tiene 2 componentes, su número IP y un valor de máscara.
    # IPv6(128 bits)
    def __init__(self, Direccion):
        self.__id
        self.__direccion = netaddr.IPAddress(Direccion)
        if netaddr.valid_ipv4(Direccion):
            self.__familia = 4
        if netaddr.valid_ipv6(Direccion):
            self.__familia = 6
        self.__vrf
        self.__id_interfaz
        self.__fecha_creacion = datetime.datetime.now()
        self.__fecha_actualizacion
        self.__nat_interno
        self.__descripcion

# Máscara (IPv4) o Prefijo (IPv6) identifican un rango de direcciones IP que
# están en la misma red.


class Prefijo():
    """docstring for Prefijo"""
    def __init__(self, cadena):
        self.arg = cadena
        print("Objeto creado")

# Regional Internet Registry


class rir():
    """docstring for rir"""
    def __init__(self, arg):
        super(rir, self).__init__()
        self.__name = arg
        self.__slug = self.__name.lower()
        self.__isprivate = True


class carro:
    def __init__(self, Modelo, Marca):
        self.modelo = Modelo
        self.marca = Marca
