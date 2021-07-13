#IMPORTACIONES
import math

while True: #SE GENERA CICLO INFINITO - UNA VEZ TEMINE UN PROCEDIMIENTO DA OPCION PARA SELECCIONAR
    #SELECCION DE METODO DE CALCULO
    Seleccionmetodo=input("Seleccione 1 para ley al cuadrado, 2 para superficie, 3 solo Coseno, 4 Flujo Luminoso, 5 Matriz Intensidad: ")

    #DEFINICION DE FORMULAS

    def CalculoECandelas(n1,n2):
        NivelIluminacion=n1/(n2**2)
        return NivelIluminacion

    def CalculoELumen(n1,n2):
        NivelIluminacion=n1/n2
        return NivelIluminacion

    def CalculoTrigon(n1,n2,n3):
        n2=Angulo*math.pi/180 #AQUI EL ANGULO ESTA EN GRADOS Y SE CONVIERTE A RADIANES
        NivelIluminacion=((n1*math.cos(n2))/n3**2)
        return NivelIluminacion

    def CalculoFlujoLumin(n1,n2):
        FlujoLumin=n1*n2
        return FlujoLumin

    def CalculoIntensidadReal(n1,n2):
        IntensidadReal=n1*(n2/1000)
        return IntensidadReal

    def CalculoNivelHorizontal(n1,n2,n3):
        n2=Angulo*math.pi/180 #AQUI EL ANGULO ESTA EN GRADOS Y SE CONVIERTE A RADIANES
        NivelHorizontal=(n1*((math.cos(n2))**3)/n3**2)
        return NivelHorizontal

    if Seleccionmetodo=="1":
        #INGRESO DE DATOS PARA USAR FORMULA - ILUMINACION 
        ILuminosa=float(input("Ingrese la intensidad luminosa en candelas: "))
        Distancia=float(input("Ingrese la distancia en metros: "))
        Nivel=CalculoECandelas(ILuminosa,Distancia)
        print("El nivel de Iluminacion es {:.2F} LUX".format(Nivel))

        #VALORACION DEL NIVEL DE ILUMINACION EN OFICINA
        if Nivel<300:
            print("El nivel de iluminacion es DEFICIENTE")
        elif Nivel>300 and Nivel<750:
            print("El nivel de iluminacion es ADECUADO")
        else:
            print("El nivel de iluminacion es EXCESIVO")

    elif Seleccionmetodo=="2":
        #INGRESO DE DATOS PARA USAR FORMULA
        FLuminoso=float(input("Ingrese el flujo luminoso en lumen: "))
        Superficie=float(input("Ingrese la superficie en m2: "))
        Nivel=CalculoELumen(FLuminoso,Superficie)
        print("El nivel de Iluminacion es {:.2F} LUX".format(Nivel))

        #VALORACION DEL NIVEL DE ILUMINACION EN OFICINA
        if Nivel<300:
            print("El nivel de iluminacion es DEFICIENTE")
        elif Nivel>300 and Nivel<750:
            print("El nivel de iluminacion es ADECUADO")
        else:
            print("El nivel de iluminacion es EXCESIVO")

    elif Seleccionmetodo=="3":
        #INGRESO DE DATOS PARA USAR FORMULA
        ILuminosa=float(input("Ingrese la intensidad luminosa en candelas: "))
        Angulo=float(input("ingrese el valor del angulo en grados: "))
        Distancia=float(input("Ingrese la distancia en metros: "))
        Nivel=CalculoTrigon(ILuminosa,Angulo,Distancia)
        print("El nivel de Iluminacion es {:.2F} LUX".format(Nivel))

        #VALORACION DEL NIVEL DE ILUMINACION EN OFICINA
        if Nivel<300:
            print("El nivel de iluminacion es DEFICIENTE")
        elif Nivel>300 and Nivel<750:
            print("El nivel de iluminacion es ADECUADO")
        else:
            print("El nivel de iluminacion es EXCESIVO")

    elif Seleccionmetodo=="4":
        #INGRESO DE DATOS PARA LA FORMULA
        ILuminosa2=float(input("Ingrese la intensidad luminosa en candelas: "))
        Angulo=float(input("ingrese el valor del angulo en grados: "))
        Distancia2=float(input("Ingrese la distancia en metros: "))
        SuperficieS=float(input("Ingrese el valor de la superficie en m2: "))
        Nivel=CalculoTrigon(ILuminosa2,Angulo,Distancia2)
        print("El nivel de Iluminacion es {:.2F} LUX".format(Nivel))
        FlujoLuminoso=CalculoFlujoLumin(Nivel,SuperficieS)
        print("El flujo luminoso es {:.2F} LUMEN".format(FlujoLuminoso))

        #VALORACION DEL NIVEL DE ILUMINACION EN OFICINA
        if Nivel<300:
            print("El nivel de iluminacion es DEFICIENTE")
        elif Nivel>300 and Nivel<750:
            print("El nivel de iluminacion es ADECUADO")
        else:
            print("El nivel de iluminacion es EXCESIVO")

    elif Seleccionmetodo=="5":
        
        #INGRESO DE DATOS PARA LA FORMULA:
        FlujoLampara=float(input("Ingrese el flujo luminoso en lumen de la lampara: "))
        IGrafico=float(input("Ingrese la intensidad de grafico en Candelas segun matriz: "))
        IReal=CalculoIntensidadReal(FlujoLampara,IGrafico)
        print("La Intensidad Real es de {:.2F} CANDELAS".format(IReal))
        Angulo=float(input("ingrese el valor del angulo en grados: "))
        Altura=float(input("Ingrese el valor de la altura en metros: "))
        NivelHorizontalEH=CalculoNivelHorizontal(IReal,Angulo,Altura)
        print("El nivel de Iluminacion Horizontal EH es {:.2F} LUX".format(NivelHorizontalEH))

        #VALORACION DEL NIVEL DE ILUMINACION EN OFICINA
        if NivelHorizontalEH<300:
            print("El nivel de iluminacion es DEFICIENTE")
        elif NivelHorizontalEH>300 and NivelHorizontalEH<750:
            print("El nivel de iluminacion es ADECUADO")
        else:
            print("El nivel de iluminacion es EXCESIVO")