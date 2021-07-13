#IMPORTACIONES
import math

#SELECCION DEL METODO DE CALCULO
TipoOperacion=input("Indique la operacion a realizar: 1 para Suma, 2 para Resta, 3 para Promedio, 4 para LAeq,d-Unica Tarea, 5 para LAeq,d-Varias Tareas: ")

def CalculoLAeqdVT(n1,n2,n3,n4,n5,n6):
    LAeqdVariasTareas=(10*math.log10(1/8*(n1*10**(n2/10)+n3*10**(n4/10)+n5*10**(n6/10))))
    return LAeqdVariasTareas

def CalculoLAeqd(n1,n2):
    NivelEquivalente=(n1+(10*math.log10(n2/8)))    
    return NivelEquivalente

def CalculoSumaDecibeles(n1,n2,n3):
    IntensidadTotal=(10*math.log10(10**(n1/10)+10**(n2/10)+10**(n3/10)))
    return IntensidadTotal

if TipoOperacion=="5":
    
    #INGRESO DE DATOS PARA CALCULO:
    LAeqt1=float(input("Ingrese la intensidad equivalente LAeq,t en decibeles de la tarea1: "))
    Texp1=float(input("Ingrese el tiempo de exposición a ruido de la tarea1 en Horas: "))
    LAeqt2=float(input("Ingrese la intensidad equivalente LAeq,t en decibeles de la tarea2: "))
    Texp2=float(input("Ingrese el tiempo de exposición a ruido de la tarea2 en Horas: "))
    LAeqt3=float(input("Ingrese la intensidad equivalente LAeq,t en decibeles de la tarea3: "))
    Texp3=float(input("Ingrese el tiempo de exposición a ruido de la tarea3 en Horas: "))
    
    #CALCULO DEL NIVEL EQUIVALENTE DIARIO
    LAeqdVT=CalculoLAeqdVT(Texp1,LAeqt1,Texp2,LAeqt2,Texp3,LAeqt3)
    print("El valor total de LAeq,d para estas tareas es: {:.1f} decibeles".format(LAeqdVT))
    
    #EVALUACION DEL RIESGO
    LimiteAccion=80
    LimitePermisible=85
    if LAeqdVT<80:
        print("EL riesgo es BAJO, la intensidad equivalente diaria es menor que 80 db")
    elif LAeqdVT>=80 and LAeqdVT<85:
        print("El riesgo es MEDIO, la intensidad equivalente diaria se encuentra entre 80 dB y 85 dB")
    elif LAeqdVT>=85:
        print("El riesgo es ALTO, la intensidad equivalente diaria es mayor que 85 dB")

elif TipoOperacion=="4":
    
    #ENTRADA DE DATOS PARA EL CALCULO
    LAeqt=float(input("Ingrese la intensidad equivalente LAeq,t en decibeles: "))
    Texp=float(input("Ingrese el tiempo de exposición a ruido a la fuente en Horas: "))
    
    #CALCULO DEL NIVEL EQUIVALENTE DIARIO
    NivelEqDiario=CalculoLAeqd(LAeqt,Texp)
    print("El valor total de LAeq,d es: {:.1f} decibeles".format(NivelEqDiario))
    
    #EVALUACION DEL RIESGO
    LimiteAccion=80
    LimitePermisible=85
    if NivelEqDiario<80:
        print("EL riesgo es BAJO, la intensidad equivalente diaria es menor que 80 db")
    elif NivelEqDiario>=80 and NivelEqDiario<85:
        print("El riesgo es MEDIO, la intensidad equivalente diaria se encuentra entre 80 dB y 85 dB")
    elif NivelEqDiario>=85:
        print("El riesgo es ALTO, la intensidad equivalente diaria es mayor que 85 dB")

elif TipoOperacion=="1":
    
    #INGRESO DE DATOS PARA EL CALCULO
    Valor1=float(input("Ingrese el primer valor de intensidad en decibeles a sumar: "))
    Valor2=float(input("Ingrese el segundo valor de intensidad en decibeles a sumar: "))
    Valor3=float(input("Ingrese el tercer valor de intensidad en decibeles a sumar: "))

    #CALCULO DE LA INTENSIDAD TOTAL
    LTotal=CalculoSumaDecibeles(Valor1,Valor2,Valor3)
    print("El valor total de la intensidad es: {:.1f} decibeles".format(LTotal))
    
    #EVALUACION DEL RIESGO
    LimiteAccion=80
    LimitePermisible=85
    if LTotal<80:
        print("EL riesgo es BAJO, la Intensidad Total es menor que 80 db")
    elif LTotal>=80 and LTotal<85 and LTotal!=85:
        print("El riesgo es MEDIO, la Intensidad Total se encuentra entre 80 dB y 85 dB")
    elif LTotal>=85 and LTotal==85:
        print("El riesgo es ALTO, la Intensidad Total es mayor que 85 dB")
        
elif TipoOperacion=="2":
    
    #INGRESO DE DATOS PARA EL CALCULO
    Valor1=float(input("Ingrese el mayor valor de intensidad en decibeles a restar: "))
    Valor2=float(input("Ingrese el menor valor de intensidad en decibeles a restar: "))
    
    #CALCULO DE LA INTENSIDAD RESTANTE
    IntensidadRestante=float(10*math.log10(10**(Valor1/10)-10**(Valor2/10)))
    print("El valor restante de la intensidad es: {:.1f} decibeles".format(IntensidadRestante))
    
    #EVALUACION Y VALORACION DEL RIESGO
    LimiteAccion=80
    LimitePermisible=85
    if IntensidadRestante<80:
        print("EL riesgo es BAJO, la Intensidad Total es menor que 80 db")
    elif IntensidadRestante>=80 and IntensidadRestante<85 and IntensidadRestante!=85:
        print("El riesgo es MEDIO, la Intensidad Total se encuentra entre 80 dB y 85 dB")
    elif IntensidadRestante>85 and IntensidadRestante==85:
        print("El riesgo es ALTO, la Intensidad Total es mayor que 85 dB")

elif TipoOperacion=="3":
    
    #INGRESO DE LOS DATOS A PROCESAR
    Valor1=float(input("Ingrese el primer valor de intensidad en decibeles a promediar: "))
    Valor2=float(input("Ingrese el segundo valor de intensidad en decibeles a promediar: "))
    Valor3=float(input("Ingrese el tercer valor de intensidad en decibeles a promediar: "))

    #CALCULO DEL PROMEDIO DE INTENSIDAD
    IntensidadMedia=float(10*math.log10(1/3*(10**(Valor1/10)+10**(Valor2/10)+10**(Valor3/10))))
    print("El valor promedio de la intensidad es: {:.1f} decibeles".format(IntensidadMedia))
    
    #EVALUACION Y VALORACION DEL RIESGO
    LimiteAccion=80
    LimitePermisible=85
    if IntensidadMedia<80:
        print("EL riesgo es BAJO, la Intensidad Total es menor que 80 db")
    elif IntensidadMedia>=80 and IntensidadMedia<85:
        print("El riesgo es MEDIO, la Intensidad Total se encuentra entre 80 dB y 85 dB")
    elif IntensidadMedia>85:
        print("El riesgo es ALTO, la Intensidad Total es mayor que 85 dB")