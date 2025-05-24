from abc import ABC , abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo = 0):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nacimiento = fecha_nacimiento
        self._saldo = saldo
#Lo voy a terminar para mañana no tuve tiempo