#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def chequearPrimo(numero):
    restos_ceros = 0
    for serie in range(1, numero + 1):
        if numero % serie == 0:
            restos_ceros += 1
    if restos_ceros == 2:
        print("Es un número primo")
    else:
        print("No es un número primmo")
    


    

numero = int(input("Chequea si un número es primo: "))
chequearPrimo(numero)