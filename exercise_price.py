def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100
    monto_impuesto= precio_base * 0.21
    subtotal =precio_base + (precio_base * 0.21)
    monto_propina = (precio_base + (precio_base * 0.21)) * 0.10


    print(precio_base * 0.21)
    print(precio_base + monto_impuesto)
    print(subtotal * 0.10)
    print(subtotal + monto_propina)

price()