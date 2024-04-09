
# Función que calcula los intereses
# Capital invertido = cantidad de dinero que se inicia en una inversión
# Interés anual = porcentaje de ganancia o pérdida
# tiempo_meses = período de tiempo durante el cual se acumulan intereses
def calcular_intereses(capital_invertido, interes_anual, tiempo_meses):
    
    # Pasamos el capital anual a mensual
    interes_mensual = interes_anual / 12 
    
    # Aplicamos la fórmula para obtener el interés generado en un periodo de tiempo
    intereses_generados = capital_invertido * interes_mensual * tiempo_meses
    return intereses_generados

# Solicita al usuario la información 
capital_invertido = float(input("Ingrese el capital invertido: "))
interes_anual = float(input("Ingrese el interés anual: "))
tiempo_meses = int(input("Ingrese el tiempo en meses: "))

# Llama a la funcion
intereses_generados = calcular_intereses(capital_invertido, interes_anual, tiempo_meses)

# Salida en pantalla
print("Los intereses generados son:", intereses_generados)
