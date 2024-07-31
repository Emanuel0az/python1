class _Habitacion:
    def __init__(self, descripcion):
        self.__descripcion = descripcion

    @property
    def descripcion(self):
        return self.__descripcion

class Casa:
    def __init__(self):
        self.__habitaciones = []

    def agregar_habitacion(self, descripcion):
        habitacion = _Habitacion(descripcion)
        self.__habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        for habitacion in self.__habitaciones:
            print(f"Habitación: {habitacion.descripcion}")


mi_casa = Casa()
mi_casa.agregar_habitacion("Habitación principal")
mi_casa.agregar_habitacion("Cocina")
mi_casa.mostrar_habitaciones()
