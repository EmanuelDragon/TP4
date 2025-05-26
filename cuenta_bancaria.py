from datetime import date, datetime
from abc import ABC , abstractmethod

class CuentaBancaria(ABC):
    def __init__(self,nombre_titular,dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular     
        self._dni_titular = dni_titular             
        self._fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y/%m/%d').date()
        self._saldo = saldo

    def obtener_saldo(self):
        return self._saldo
    
    @abstractmethod
    def depositar(self,monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo es de: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debeser mayor a 0")

    @abstractmethod
    def extraer(self,monto):
        if monto <= self.obtener_saldo():
            self._saldo -= monto
            print(f"Se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo acutal es de: {self.obtener_saldo()}")
        else:
            print("No posee saldo suficiente para esta operación")

    def _calcular_edad(self):
        fecha_actual = date.today()
        edad = fecha_actual - self._fecha_nacimiento
        return edad.days // 365
    
    def obtener_edad(self):
        return self._calcular_edad()

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = 0.001
    
    def calcular_interes(self):
        return self._saldo * self._tasa_interes

    def obtener_saldo(self):
        return super().obtener_saldo()
    
    def depositar(self, monto):
        return super().depositar(monto)
    
    def extraer(self, monto):
        return super().extraer(monto)
    
    def _calcular_edad(self):
        return super()._calcular_edad(self)
    
    def obtener_edad(self):
        return self._calcular_edad