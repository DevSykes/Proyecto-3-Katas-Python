# ==============================================================================
# 1. Escribe una función que reciba una cadena de texto como parámetro 
# y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.
# ==============================================================================

def contar_frecuencia_letras(cadena):
    frecuencias = {}
    
    for caracter in cadena:
        # Ignorar espacios
        if caracter == " ":
            continue
            
        # Que no distinga entre mayus y minus
        letra = caracter.lower() 
        
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
            
    return frecuencias

# ==============================================================================
# 2. Dada una lista de números, obtén una nueva lista con el doble de 
# cada valor. Usa la función map().
# ==============================================================================

def doblar(numero):
    return numero * 2

numeros = [1, 2, 3, 4, 5]

# Utilizo map para doblar los numeros
# Entiendo que hay que envolverlo en list para pedirselos 1 a 1
numeros_dobles = list(map(doblar, numeros))

# ==============================================================================
# 3. Escribe una función que tome una lista de palabras y una palabra 
# objetivo como parámetros. La función debe devolver una lista con todas las 
# palabras de la lista original que contengan la palabra objetivo.
# ==============================================================================

def filtrar_por_palabra(lista_palabras, objetivo):
    resultado = []
    
    for palabra in lista_palabras:
        if objetivo in palabra:
            resultado.append(palabra)
            
    return resultado

# ==============================================================================
# 4. Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map().
# ==============================================================================

def restar(a, b):
    return a - b

def calcular_diferencia(lista1, lista2):
    resultado = list(map(restar, lista1, lista2))
    return resultado

# ==============================================================================
#  PRINT - PRUEBAS
# ==============================================================================

if __name__ == "__main__":
    
    # --- Pruebas Ejercicio 1 ---
    print("--- Ejercicio 1 ---")
    texto_prueba = "Hola Mundo"
    resultado1 = contar_frecuencia_letras(texto_prueba)
    print(f"Texto: '{texto_prueba}'")
    print(f"Resultado: {resultado1}")

    # --- Línea de separación ---
    print("\n" + "═"*40 + "\n")

    # --- Pruebas Ejercicio 2 ---
    print("--- Ejercicio 2 ---")
    numeros = [1, 2, 3, 4, 5]
    resultado2 = list(map(doblar, numeros))
    print(f"Lista original: {numeros}")
    print(f"Resultado al doble: {resultado2}")

    print("\n" + "═"*40 + "\n")

    # --- Pruebas Ejercicio 3 ---

print("--- Ejercicio 3 ---")

personajes = ["Zack Fair", "Cloud Strife", "Sephiroth", "Aerith Gainsborough", "Angeal Hewley", "Genesis Rhapsodos"]
busqueda = "a" # buscar nombres que contienen la letra 'a'

resultado_final = filtrar_por_palabra(personajes, busqueda)

print(f"Lista de personajes: {personajes}")
print(f"Buscando personajes con la letra: '{busqueda}'")
print(f"Resultado: {resultado_final}")

print("\n" + "═"*40 + "\n")

    # --- Pruebas Ejercicio 4 ---
    