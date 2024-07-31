from datetime import datetime

class Persona:
    def __init__(self, nombre, apellidos, fecha_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento

    def calcular_edad(self):
        hoy = datetime.now()
        fecha_nac = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d")
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        return edad

    def saludar(self):
        edad = self.calcular_edad()
        return f"Hola, me llamo {self.nombre} {self.apellidos}, y tengo {edad} años"

class Profesor(Persona):
    def saludar(self):
        edad = self.calcular_edad()
        return f"Hola, soy el profesor {self.nombre} {self.apellidos}, y tengo {edad} años"

class Estudiante(Persona):
    def saludar(self):
        edad = self.calcular_edad()
        return f"Hola, soy el estudiante {self.nombre} {self.apellidos}, y tengo {edad} años"

class Clase:
    def __init__(self, nombre_clase, profesor, estudiantes):
        self.nombre_clase = nombre_clase
        self.profesor = profesor
        self.estudiantes = estudiantes

    def imprimir_estudiantes(self):
        for estudiante in self.estudiantes:
            print(f"{estudiante.nombre} {estudiante.apellidos}")

    def imprimir_detalle_clase(self):
        print(f"Clase: {self.nombre_clase}, impartida por el profesor {self.profesor.nombre} {self.profesor.apellidos}")


profesor = Profesor("John", "Doe", "1980-05-15")
estudiantes = [
    Estudiante("Jane", "Smith", "2000-06-01"),
    Estudiante("Alice", "Johnson", "1999-09-21"),
    Estudiante("Bob", "Brown", "2001-12-11")
]
clase = Clase("Programación Backend", profesor, estudiantes)


clase.imprimir_detalle_clase()


clase.imprimir_estudiantes()


print(profesor.saludar())
for estudiante in estudiantes:
    print(estudiante.saludar())
