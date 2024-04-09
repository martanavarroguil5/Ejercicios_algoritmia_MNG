
# Los coeficientes son los coeficientes de ponderación para cada número
def calcular_media_ponderada(numero1, numero2, numero3, coeficiente1, coeficiente2, coeficiente3):

    # Suma los números multiplicados por sus ponderaciones
    suma_ponderada = (numero1 * coeficiente1) + (numero2 * coeficiente2) + (numero3 * coeficiente3)
    
    # Divide entre la suma de los coeficientes para hallar la media
    suma_coeficientes = coeficiente1 + coeficiente2 + coeficiente3
    media_ponderada = suma_ponderada / suma_coeficientes
    return media_ponderada

# Solicita la información de cada número y sus coeficientes
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

coeficiente1 = float(input("Ingrese el coeficiente para el primer número: "))
coeficiente2 = float(input("Ingrese el coeficiente para el segundo número: "))
coeficiente3 = float(input("Ingrese el coeficiente para el tercer número: "))

# Llama a la función y salida en pantalla
media_ponderada = calcular_media_ponderada(numero1, numero2, numero3, coeficiente1, coeficiente2, coeficiente3)
print("La media ponderada es:", media_ponderada)

