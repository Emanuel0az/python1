class perro :
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    
    def ladrar (self):
        return "Guau!"
    
    
    def mover(self, direccion):
        return f"{self.nombre} se mueve hacia {direccion}"
    
    
bobby = perro(nombre="Bobby", edad=5)
maximus = perro(nombre="Maximus", edad=7)


print("el perro ladra: ", maximus.ladrar())
print(bobby.mover("adelante"))

#Ejercicio 2

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mover(self, direccion):
        return f"{self.nombre} se mueve hacia {direccion}"


class Perro(Animal):
    def ladrar(self):
        return "Guau!"


class Gato(Animal):
    def maullar(self):
        return "Miau!"


class Ave(Animal):
    def cantar(self):
        return "Pío pío!"


# Crear instancias de las clases
bobby = Perro(nombre="Bobby", edad=5)
maximus = Perro(nombre="Maximus", edad=7)
michu = Gato(nombre="Michu", edad=3)
piolin = Ave(nombre="Piolín", edad=2)

# Utilizar las instancias
print("El perro ladra:", maximus.ladrar())
print(bobby.mover("adelante"))
print("El gato maúlla:", michu.maullar())
print(piolin.mover("hacia el árbol"))

# Imprimir la dirección de memoria de las instancias
print(f"Dirección de memoria de bobby: {id(bobby)}")
print(f"Dirección de memoria de maximus: {id(maximus)}")
print(f"Dirección de memoria de michu: {id(michu)}")
print(f"Dirección de memoria de piolin: {id(piolin)}")
