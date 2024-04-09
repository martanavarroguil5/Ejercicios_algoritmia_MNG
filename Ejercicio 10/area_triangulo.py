
# Funcion que calcula el area para un triangulo de lado "lado" y altura "altura"
def calcular_area_triangulo(lado, altura):
    
    # Fórmula para calcular el area de un triangulo
    area = 0.5 * lado * altura
    return area

# Solicitud de los datos
lado = float(input("Ingrese la medida del lado del triángulo: "))
altura = float(input("Ingrese la medida de la altura relativa al lado: "))

# Llamada a la funcion y salida en pantalla
area = calcular_area_triangulo(lado, altura)
print("El área del triángulo es:", area)

# Para que este código funcieone para un triangulo rectangulo se debe introducir la informacion de un
# de los dos lados en la variable de "lado" y el otro en la de "altura".