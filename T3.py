import math
import random


def punto_aleatorio(a, b):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)
    return x, y


def en_elipse(x, y, a, b):
    return x * x / (a * a) + y * y / (b * b) <=1


def en_hiperbola(x, y, c, d):
    return x * x / (c * c) - y * y / (d * d) >=1


def leer_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser positivo.")
        except ValueError:
            print("Entrada invalida.")


def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser un entero positivo.")
        except ValueError:
            print("Entrada inválida.")


def main():
    print("=== Monte Carlo: Interseccion Elipse - Hiperbola ===")
    a = leer_positivo("Ingrese a de la elipse: ")
    b = leer_positivo("Ingrese b de la elipse: ")
    c = leer_positivo("Ingrese c de la hiperbola: ")
    d = leer_positivo("Ingrese d de la hiperbola: ")
    n = leer_entero_positivo("Cantidad de puntos aleatorios: ")

    puntos_elipse = 0
    puntos_interseccion = 0

    for _ in range(n):
        x, y = punto_aleatorio(a, b)
        if en_elipse(x, y, a, b):
            puntos_elipse += 1
            if en_hiperbola(x, y, c, d):
                puntos_interseccion += 1

    area_elipse = math.pi * a * b

    if puntos_elipse > 0:
        area_interseccion = area_elipse * puntos_interseccion / puntos_elipse
    else:
        area_interseccion = 0

    print("\n----- RESULTADOS -----")
    print(f"Puntos generados: {n}")
    print(f"Puntos dentro de la elipse: {puntos_elipse}")
    print(f"Puntos en la intersección: {puntos_interseccion}")
    print(f"\nArea de la elipse: {area_elipse:.4f}")
    print(f"Area aproximada de interseccion: {area_interseccion:.4f}")


if __name__ == "__main__":
    main()