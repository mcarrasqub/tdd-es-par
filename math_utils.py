# Intencionalmente vacío o sin la función 'es par' para provocar RED

def es_par(n: int) -> bool:

    """
    Devuelve True si 'n' es un número par; en caso contrario, False.
    Un entero es par cuando el residuo de dividirlo entre 2 es 0.
    """
    return n % 2 == 0

def es_multiplo_de(n: int, m: int) -> bool:

    """
    Devuelve True si 'n' es múltiplo de 'm'; en caso contrario, False.
    Un entero 'n' es múltiplo de otro entero 'm' si el residuo de dividir 'n' entre 'm' es 0.
    """
    if m == 0:
        return False
    else: 
        return n % m == 0