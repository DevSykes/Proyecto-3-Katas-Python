# ==============================================================================
# Escribe una función que reciba una cadena de texto como parámetro 
# y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.
# ==============================================================================

def contar_frecuencia_letras(cadena):
    frecuencias = {}
    
    for caracter in cadena:
        # Ignorar espacios
        if caracter == " ":
            continue
            
        # Poner todo en minusculas
        letra = caracter.lower() 
        
        # Si hay letra, suma 1. Si no, se crea, valor 1.
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
            
    return frecuencias

# Pruebas
if __name__ == "__main__":
    texto_prueba = "Hola Mundo"
    resultado = contar_frecuencia_letras(texto_prueba)
    print(f"Texto: '{texto_prueba}'")
    print(f"Resultado: {resultado}")