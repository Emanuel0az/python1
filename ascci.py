def codificar_texto(texto):

    return texto.replace('ñ', '##')

def decodificar_texto(texto_codificado):

    return texto_codificado.replace('##', 'ñ')

# Ejemplo de uso
texto = "El niño juega en el baño."

texto_codificado = codificar_texto(texto)
print(f"Texto codificado: {texto_codificado}")

texto_decodificado = decodificar_texto(texto_codificado)
print(f"Texto decodificado: {texto_decodificado}")
