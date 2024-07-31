class _Motor:
    def __init__(self):
        self.__encendido = False

    def encender(self):
        self.__encendido = True

    def apagar(self):
        self.__encendido = False

    @property
    def encendido(self):
        return self.__encendido

class _Ruedas:
    def __init__(self, cantidad):
        self.__cantidad = cantidad

    @property
    def cantidad(self):
        return self.__cantidad

class Coche:
    def __init__(self, ruedas=4):
        self.__motor = _Motor()
        self.__ruedas = _Ruedas(ruedas)
        self.__velocidad = 0

    def conducir(self):
        if not self.__motor.encendido:
            self.__motor.encender()
        self.__velocidad = 60 
        print(f"Conduciendo a {self.__velocidad} km/h")

    def parar(self):
        self.__motor.apagar()
        self.__velocidad = 0
        print("El coche está detenido.")

# Uso de las clases
mi_coche = Coche()
mi_coche.conducir()
mi_coche.parar()
