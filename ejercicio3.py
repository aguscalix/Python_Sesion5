#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} es un año bisiesto.")
            else:
                print(f"{year} no es año bisiesto.")
        else:
            print(f"{year} es un año bisiesto.")
    else:
        print(f"{year} no es año bisiesto.")


year = int(input("¿Qué año quieres comprobar?: "))

bisiesto(year)