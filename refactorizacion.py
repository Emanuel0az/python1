class Inventario:
    def __init__(self):
        self.__items = []

    def agregar_item(self, item):
        self.__items.append(item)

    def mostrar(self, nombre_jugador):
        print(f"Inventario de {nombre_jugador}:")
        for item in self.__items:
            print(f"- {item}")

class Juego:
    def __init__(self, jugador):
        self.__jugador = jugador

    def iniciar(self):
        print(f"Bienvenido a la aventura, {self.__jugador.nombre}!")
        item = "espada"
        self.encuentro(item)
        print(f"¡La aventura ha terminado, {self.__jugador.nombre}!")
        self.__jugador.inventario.mostrar(self.__jugador.nombre)

    def encuentro(self, item):
        print(f"Encuentras una {item}. ¿Quieres agregarla a tu inventario? (s/n)")
        respuesta = input().strip().lower()
        if respuesta == "s":
            self.__jugador.inventario.agregar_item(item)

class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__inventario = Inventario()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def inventario(self):
        return self.__inventario


nombre_jugador = input("Ingresa tu nombre: ").strip()
jugador = Jugador(nombre_jugador)
juego = Juego(jugador)
juego.iniciar()
