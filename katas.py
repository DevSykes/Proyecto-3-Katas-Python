# ==============================================================================
# 1. Escribe una función que reciba una cadena de texto como parámetro 
# y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.
# ==============================================================================

def contar_frecuencia_letras(cadena):
    frecuencias = {}
    
    for caracter in cadena:
        # Para que ignore espacios
        if caracter == " ":
            continue
            
        # para no distinga entre mayus y minus
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
# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado 
#(por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es
#mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso".
#La función debe devolver una tupla que contenga la media y el estado.
# ==============================================================================

def evaluar_media(numeros, nota_aprobado=5):
    if not numeros:
        return (0, "suspenso")
    
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    
    return (media, estado)

# ==============================================================================
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
# ==============================================================================

def factorial(n):
    if n == 0 or n == 1:
        return 1
    # recursivo
    else:
        return n * factorial(n - 1)
    
# ==============================================================================
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
# ==============================================================================


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

    # Línea de separación
    print("\n" + "═"*40 + "\n")

    # --- Pruebas Ejercicio 2 ---
    print("--- Ejercicio 2 ---")
    numeros = [1, 2, 3, 4, 5]
    resultado2 = list(map(doblar, numeros))
    print(f"Lista original: {numeros}")
    print(f"Resultado: {resultado2}")

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

    print("--- Ejercicio 4 ---")
        
    lista_a = [10, 20, 30]
    lista_b = [1, 2, 3]
        
    resultado4 = calcular_diferencia(lista_a, lista_b)
        
    print(f"Lista A: {lista_a}")
    print(f"Lista B: {lista_b}")
    print(f"Resta:   {resultado4}")


    # --- Pruebas Ejercicio 5 ---

    print("--- Ejercicio 5 ---")
    print(evaluar_media([4, 6, 8]))

    # --- Pruebas Ejercicio 6 ---
    print("--- Ejercicio 6 ---")
    print(factorial(5))

    # --- Pruebas Ejercicio 7 ---
    print("--- Ejercicio 7 ---")