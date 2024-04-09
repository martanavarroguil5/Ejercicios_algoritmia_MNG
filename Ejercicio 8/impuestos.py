
# Fncion que calcula el precio con impuestos
def calcular_precio_con_impuestos(precio_sin_impuestos, iva):
    
    # Cálculo del impuesto en funcion del precio y del iva
    impuesto = precio_sin_impuestos * (iva / 100) 
    
    # Precio total (mas el impuesto calculado)
    precio_con_impuestos = precio_sin_impuestos + impuesto
    return precio_con_impuestos

# Solicita al usuario el precio sin impuuestos y el iva.
precio_sin_impuestos = float(input("Ingrese el precio sin impuestos: "))
iva = float(input("Ingrese el porcentaje de IVA: "))

# Salida en pantalla del precio calculado
precio_con_impuestos = calcular_precio_con_impuestos(precio_sin_impuestos, iva)
print("El precio con impuestos incluidos es:", precio_con_impuestos)