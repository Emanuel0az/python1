from datetime import datetime

def calcular_edad(fecha_nacimiento):

    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

fecha_nacimiento = '2002-09-09'
print(f"La edad actual es: {calcular_edad(fecha_nacimiento)} años")
