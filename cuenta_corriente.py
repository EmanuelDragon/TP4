from cuenta_bancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0,limite_extraccion = 500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
    
    def extraer(self, monto):
        if monto <= self.obtener_saldo() and monto <= self._limite_extraccion:
            super().extraer(monto)
        else:
            if monto > self._limite_extraccion:
                print("Usted no puede extraer ese monto")
            else:
                print("Usted no posee saldo suficiente para realizar la operación")
