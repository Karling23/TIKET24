def encontrarMenor(*num):
    return min(num)

def calcularCuota(monto, tasa_interes, meses):
    tasa_mensual = tasa_interes / 100 / 12  
    cuota = monto * (tasa_mensual * (1 + tasa_mensual) ** meses) / ((1 + tasa_mensual) ** meses - 1) 
    return cuota

def determinarResultadosIMC(imc):
    if imc < 0:
        return "IMC fuer de rango"
    elif 0 <= imc < 16:
        return "Delgadez severa"
    elif 16 <= imc < 17:
        return "Delgadez moderada"
    elif 17 <= imc < 18.5:
        return "Delgadez leve"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado 1"
    elif 35 <= imc < 40:
        return "Obesidad Grado 2"
    elif imc >= 40:
        return "Obesidad Grado 3"

