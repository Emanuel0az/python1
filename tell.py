import re

def buscar_telefonos(texto):

    patron = r'\b\d{4}-\d{4}\b'
    return re.findall(patron, texto)

# Ejemplo de uso
texto = "Aquí hay algunos números de teléfono: 1234-5678, 9876-5432, y 0000-0000."
print(buscar_telefonos(texto))
