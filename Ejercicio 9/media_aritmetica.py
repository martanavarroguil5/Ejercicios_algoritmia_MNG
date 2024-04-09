
# Funcion que calcula la media  de tres números
def calcular_media_aritmetica(numero1, numero2, numero3):
    suma = numero1 + numero2 + numero3
    media = suma / 3
    return media

# Solicita al usuario los tres numeros
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

#Llamada a la función y salida en pantalla
media_aritmetica = calcular_media_aritmetica(numero1, numero2, numero3)
print("La media aritmética es:", media_aritmetica)

