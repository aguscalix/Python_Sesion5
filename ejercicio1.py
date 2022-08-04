'''Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
 y otra función que calcule el área de un círculo recibiendo el radio del mismo.'''

from cmath import pi


def areaTriangulo(base, altura):
    
    area_triangulo = base * altura / 2

    print(f"Área del triángulo: {area_triangulo}")


def areaCirculo(radio):

    area_circulo = round(pi * radio ** 2, 2)

    print(f"Área del círculo: {area_circulo}")



figura = input("Qué figura quieres? escribe triangulo o circulo: ")

if figura == "triangulo":
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    areaTriangulo(base, altura)
elif figura == "circulo":
    radio = float(input("Ingresa el radio: "))
    areaCirculo(radio)
else:
    print("Figura no disponible")