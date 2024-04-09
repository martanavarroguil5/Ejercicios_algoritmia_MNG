
# Funcion que calcula el salario por horas extra
def calcular_importe_horas_extra(salario_mensual_bruto, horas_extra):
    
    # Se define las horas normales al mes y el salario por hora
    horas_normales_mes = 35 * 4  # 4 semanas al mes, 35 horas semanales
    tarifa_hora_normal = salario_mensual_bruto / horas_normales_mes

    # Se calcula el dinero extra que se debe incluir en el sueldo en funcion de las horas extra
    # Si ha trabajado de entre 1 y 7 horas de más, esas horas las cobra por 1,25 más
    if horas_extra >= 1 and horas_extra <= 8:
        tarifa_hora_extra = tarifa_hora_normal * horas_extra * 1.25
    
    # Si las horas extra superan 7 horas, esas horas las cobra por 1,5 más
    elif horas_extra > 7:
        tarifa_hora_extra = tarifa_hora_normal * 1.5 * horas_extra
    else:
        # No hay horas extra que pagar
        return tarifa_hora_extra == 0
    

    return tarifa_hora_extra

# Solicita al usuario la información
salario_mensual_bruto = float(input("Ingrese el salario mensual bruto: "))
horas_extra = int(input("Ingrese la cantidad de horas extra trabajadas: "))

# Lama a la funcion y muestra ell resultado
importe_horas_extra = calcular_importe_horas_extra(salario_mensual_bruto, horas_extra)
print("El importe de las horas extra a pagar es:", importe_horas_extra)
