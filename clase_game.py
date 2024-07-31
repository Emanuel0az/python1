class _Habilidad:
    def __init__(self, nombre, poder):
        self.__nombre = nombre
        self.__poder = poder

    @property
    def nombre(self):
        return self.__nombre

    @property
    def poder(self):
        return self.__poder

class Personaje:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__habilidades = []

    def aprender_habilidad(self, nombre_habilidad, poder):
        habilidad = _Habilidad(nombre_habilidad, poder)
        self.__habilidades.append(habilidad)

    def mostrar_habilidades(self):
        print(f"Personaje: {self.__nombre}")
        for habilidad in self.__habilidades:
            print(f"Habilidad: {habilidad.nombre}, Poder: {habilidad.poder}")

# Uso de las clases
guerrero = Personaje("Guerrero")
guerrero.aprender_habilidad("Espada", 50)
guerrero.aprender_habilidad("Escudo", 30)
guerrero.mostrar_habilidades()
