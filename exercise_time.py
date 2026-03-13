def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    print((total_segundos // 60) // 60)
    print(total_segundos // 3660)
    print(total_segundos % 3660)

time()