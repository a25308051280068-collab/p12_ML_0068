print("Christian Garcia Jimenez Nc=0068")
import pandas as pd
print(pd.__version__) # Output: 1.5.2

# ==============================================================================
# ACTIVIDAD P8: FUNCIONES EN PYTHON
# Archivo: p8-funciones-0777.py
# ==============================================================================

# ------------------------------------------------------------------------------
# PARTE 1: EJEMPLOS (Basados en elprimer link: elpythonista.com)
# ------------------------------------------------------------------------------

# 1. Definición y llamada básica a una función
def saludar_usuario():
    """Imprime un saludo básico en consola."""
    print("¡Hola! Bienvenido al curso de Python para Machine Learning.")

print("--- Ejercicio 1 ---")
saludar_usuario()


# 2. Función con parámetros de entrada y retorno de valor
def sumar_numeros(num1, num2):
    """Retorna la suma de dos números enteros o flotantes."""
    return num1 + num2

print("\n--- Ejercicio 2 ---")
resultado_suma = sumar_numeros(15, 25)
print(f"El resultado de la suma es: {resultado_suma}")


# 3. Parámetros por defecto en una función
def calcular_total_compra(subtotal, impuesto=0.16):
    """Calcula el costo total aplicando un impuesto opcional."""
    total = subtotal + (subtotal * impuesto)
    return total

print("\n--- Ejercicio 3 ---")
print(f"Total con impuesto estándar (16%): {calcular_total_compra(100)}")
print(f"Total con impuesto personalizado (8%): {calcular_total_compra(100, 0.08)}")


# 4. Uso de *args para número indeterminado de argumentos posicionales
def calcular_promedio(*notas):
    """Suma todas las notas recibidas y calcula su promedio."""
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

print("\n--- Ejercicio 4 ---")
promedio_alumnos = calcular_promedio(85, 90, 78, 92, 88)
print(f"El promedio de las calificaciones es: {promedio_alumnos:.2f}")


# 5. Uso de **kwargs para número indeterminado de argumentos nombrados
def registrar_estudiante(**datos):
    """Muestra la información recibida en formato de clave-valor."""
    print("Ficha de Registro:")
    for clave, valor in datos.items():
        print(f"  - {clave.capitalize()}: {valor}")

print("\n--- Ejercicio 5 ---")
registrar_estudiante(nombre="Juan", edad=20, carrera="IA", grupo="3H")


# 6. Funciones Lambda (Anónimas)
multiplicar = lambda a, b: a * b

print("\n--- Ejercicio 6 ---")
print(f"Resultado de multiplicación con Lambda: {multiplicar(6, 7)}")


# ------------------------------------------------------------------------------
# PARTE 2: EJEMPLOS (Basados en el segundo link: pythones.net)
# ------------------------------------------------------------------------------

# 7. Función integrada con estructuras de control
def es_par_o_impar(numero):
    """Determina si un número es par o impar."""
    if numero % 2 == 0:
        return f"El número {numero} es Par."
    else:
        return f"El número {numero} es Impar."

print("\n--- Ejercicio 7 ---")
print(es_par_o_impar(14))
print(es_par_o_impar(27))


# 8. Retorno múltiple de valores mediante Tuplas
def operaciones_basicas(x, y):
    """Retorna suma, resta y producto de dos valores en una sola llamada."""
    suma = x + y
    resta = x - y
    producto = x * y
    return suma, resta, producto

print("\n--- Ejercicio 8 ---")
s, r, p = operaciones_basicas(10, 4)
print(f"Suma: {s}, Resta: {r}, Producto: {p}")


# 9. Función Recursiva básica
def cuenta_regresiva(numero):
    """Imprime números de forma descendente hasta 0 usando recursividad."""
    if numero <= 0:
        print("¡Tiempo terminado!")
    else:
        print(numero)
        cuenta_regresiva(numero - 1)

print("\n--- Ejercicio 9 ---")
cuenta_regresiva(5)


# 10. Modificación de variables globales desde una función
contador_global = 0

def incrementar_contador():
    """Incrementa la variable global utilizando la palabra reservada 'global'."""
    global contador_global
    contador_global += 1

print("\n--- Ejercicio 10 ---")
incrementar_contador()
incrementar_contador()
print(f"Valor final del contador global: {contador_global}")


# 11. Implementación de Decoradores
def decorador_log(funcion):
    """Decorador que notifica la ejecución de una función."""
    def funcion_decorada():
        print("[LOG]: Iniciando procesamiento...")
        funcion()
        print("[LOG]: Procesamiento finalizado.")
    return funcion_decorada

@decorador_log
def ejecutar_modelo_ml():
    print("Entrenando modelo de Machine Learning...")

print("\n--- Ejercicio 11 ---")
ejecutar_modelo_ml()

print("Christian Garcia Jimenez Nc=0068")

