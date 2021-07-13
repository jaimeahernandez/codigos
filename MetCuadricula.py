#IMPORTACIONES
import math

#DEFINICION DE FUNCIONES
def IndicedeLocal(n1,n2,n3):
    Indice=(n1*n2)/(n3*(n1+n2))
    return Indice

def CalculoMinPuntos(n1):
    NumeroMin=(n1+2)**2
    return NumeroMin

#CALCULO DEL INDICE DE LOCAL K
Largo=float(input("Ingrese el Largo del punto de muestreo: "))
Ancho=float(input("Ingrese el Ancho del punto de muestreo: "))
Altura=float(input("Ingrese la Altura de Montaje del Punto de muestreo: "))
ILocal=IndicedeLocal(Largo,Ancho,Altura)
ILocalRoundUp=math.ceil(ILocal)
print(f"El indice de local es: {ILocalRoundUp} ")

#CALCULO DEL NUMERO MINIMO DE PUNTOS
NumeroMinimoPuntos=CalculoMinPuntos(ILocalRoundUp)
print(f"El minimo numero de puntos es: {NumeroMinimoPuntos}")

#CALCULO DEL NIVEL DE ILUMINACION PROMEDIO
NumerodeMediciones=int(input("Ingrese el número de mediciones realizadas: "))
ListaMediciones=[]
for i in range(0,NumerodeMediciones):
    ListaMediciones.append(float(input("Ingrese el valor de la medición en LUX: ")))
Promedio=sum(ListaMediciones)/len(ListaMediciones)
print(f"El nivel de iluminación promedio es de: {Promedio} LUX")

#VALORACION DEL NIVEL DE ILUMINACION PROMEDIO
Valorminimo=300
Valormaximo=750
if Promedio<Valorminimo:
    print("Su valoración es DEFICIENTE")
elif Promedio>Valorminimo and Promedio<Valormaximo:
    print("Su valoración es ADECUADO")
else:
    print("Su valoración es EXCESIVO")

#CALCULAR LA UNIFORMIDAD
Emin=min(ListaMediciones)
print(f"El nivel de iluminación mas bajo es: {Emin} LUX")
if Emin>=Promedio/2:
    print("El nivel de iluminacion en el area es UNIFORME. La desigualdad se cumple")
else:
    print("El nivel de iluminacion en el area es NO ES UNIFORME. La desigualdad no se cumple")