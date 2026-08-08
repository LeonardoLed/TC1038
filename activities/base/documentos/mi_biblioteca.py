# mi_biblioteca.py

def saludar(nombre):
    """Devuelve un saludo personalizado."""
    return f"¡Hola, {nombre}! Bienvenido/a."

def calcular_promedio(numeros):
    """Calcula y devuelve el promedio de una lista de números."""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)
