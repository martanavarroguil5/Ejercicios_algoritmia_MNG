
# Cuenta esttandar
class Cuenta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    # Getter
    def get_cliente(self):
        if isinstance(self.cliente, str):
            return self.cliente
        else:
            raise TypeError("Introduce un nombre correcto.")
        
    def get_saldo(self):
        if isinstance(self.saldo, float):
            return self.cliente
        else:
            raise TypeError("Debe ser un número decimal.")
    
    # Esta función suma a el saldo del cliente una cantidad "cantidad".
    def depositar(self, cantidad):
        self.saldo += cantidad
    
    # Esta función le quita al cliente una cantidad "cantidad" de su saldo.
    def retirar(self, cantidad):
        if self.saldo >= cantidad :
            self.saldo -= cantidad
            return True
        else:
            print("No se puede retirar fondos. Saldo es insuficiente.")
            return False


# Cuenta especial (con descuento). Hereda de Cuenta.
class CuentaConDescubierto(Cuenta): 
    def __init__(self, cliente, saldo, descubrimiento):
        super().__init__(cliente, saldo) # Herencia del constructor y getters.
        self.descubrimiento = descubrimiento # Propio de la clase hija.
     
    # getter
    def get_descubriento(self):
        if isinstance(self.descubrimiento, float):
            return self.descubrimiento
        else:
            raise TypeError("Inroduce un numero con decimales para el descubrimiento.")
    
    # Funcion que permite bajar a numeros negativos
    def retirar(self, cantidad):

        # El descubrimiento es el tope negativo al que el banco te deja bajar. No puedes tener menos.
        if self.saldo - cantidad >= -self.descubrimiento:
            self.saldo -= cantidad
            return True
        else:
            print("No se puede retirar fondos. Saldo es insuficiente.")
            return False
