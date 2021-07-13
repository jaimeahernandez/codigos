#SELECCION DEL TIPO DE VIBRACION (HAV O WBV)
TipoVibracion=input("Ingrese, 1 (para HAV) o 2 (para WBV): ")
if TipoVibracion=="1":
    FuentesVibracion=input("Ingrese, A (Una fuente) o B (Varias fuentes): ")
    
    #DEFINICION DE FUNCIONES
    import math
    def CalculoAPonderadaHAVFuentes(n1,n2,n3):
        AceleracionPonderada=math.sqrt(n1**2+n2**2+n3**2)
        return AceleracionPonderada
    
    def CalculoA8HAVFuentes(n1,n2):
        CalculoA8=n1*math.sqrt(n2/8)
        return CalculoA8
    
    #CALCULO DE LA ACELERACION PONDERADA EN M/S2
    if FuentesVibracion=="A":
        ax=float(input("Ingrese el valor de la aceleracion en el eje X en m/s2: "))
        ay=float(input("Ingrese el valor de la aceleracion en el eje y en m/s2: "))
        az=float(input("Ingrese el valor de la aceleracion en el eje z en m/s2: "))
        ahv=CalculoAPonderadaHAVFuentes(ax,ay,az)
        print("El valor de la Aceleracion Ponderada ahv es de: {:.1f} m/s2".format(ahv))
        
        #CALCULO DEL A(8) PARA VIBRACION MANO BRAZO Y UNA SOLA FUENTE DE VIBRACION
        Texp=float(input("Ingrese el tiempo de exposición en horas: "))
        A8=CalculoA8HAVFuentes(ahv,Texp)
        print("El valor de la Aceleracion de 8 horas A8 es de: {:.1f} m/s2".format(A8))

        #VALORACION DE RIESGO POR VIBRACION MANO BRAZO Y UNA SOLA FUENTE DE VIBRACION
        LimiteAccion=2.5
        LimitePermisible=5
        if A8<LimiteAccion:
            print("El riesgo evaluado es BAJO. El A(8) está por debajo del Limite de Acción")
            print("RECOMENDACION:MANTENER LAS MEDIDAS DE INTERVENCION ACTUALES")           
        elif A8>LimiteAccion and A8<LimitePermisible:
            print("El riesgo evaluado es MEDIO. El A(8) está entre el Limite de Acción y el Limite Permisible")
            print("RECOMENDACION:APLICAR MEDIDAS DE INTERVENCION A MEDIANO PLAZO")
        else:
            print("El riesgo evaluado es ALTO. El A(8) está por encima del Limite Permisible")
            print("RECOMENDACION:APLICAR MEDIDAS DE INTERVENCION A CORTO PLAZO")
    
    elif FuentesVibracion=="B":
        Numerodefuentes=(input("Ingrese, 2 (Dos fuentes), 3 (Tres Fuentes): "))
        if Numerodefuentes=="3":
            
            #CALCULO DEL A(8) DE CADA FUENTE DE VIBRACION
            ahv1=float(input("Ingrese el valor de la acelaracion ponderada ahv de la primera fuente: "))
            Texp1=float(input("Ingrese el valor del tiempo de exposición en horas de la primera fuente: "))
            ahv2=float(input("Ingrese el valor de la acelaracion ponderada ahv de la segunda fuente: "))
            Texp2=float(input("Ingrese el valor del tiempo de exposición en horas de la segunda fuente: "))
            ahv3=float(input("Ingrese el valor de la acelaracion ponderada ahv de la tercera fuente: "))
            Texp3=float(input("Ingrese el valor del tiempo de exposición en horas de la tercera fuente: "))
            A8_1=CalculoA8HAVFuentes(ahv1,Texp1)
            print("El valor de la Aceleracion de 8 horas A8_1 es de: {:.1f} m/s2".format(A8_1))
            A8_2=CalculoA8HAVFuentes(ahv2,Texp2)
            print("El valor de la Aceleracion de 8 horas A8_2 es de: {:.1f} m/s2".format(A8_2))
            A8_3=CalculoA8HAVFuentes(ahv3,Texp3)
            print("El valor de la Aceleracion de 8 horas A8_3 es de: {:.1f} m/s2".format(A8_3))

            #CALCULO DEL A(8) GLOBAL
            A8_Global=CalculoAPonderadaHAVFuentes(A8_1,A8_2,A8_3)
            print("El valor de la Aceleracion Global de 8 horas A8_Global es de: {:.1f} m/s2".format(A8_Global))

            #VALORACION DE RIESGO POR VIBRACION MANO BRAZO Y VARIAS FUENTES DE VIBRACION
            LimiteAccion=2.5
            LimitePermisible=5
            if A8_Global<LimiteAccion:
                print("El riesgo evaluado es BAJO. El A(8) Global está por debajo del Limite de Acción")
                print("RECOMENDACION:MANTENER LAS MEDIDAS DE INTERVENCION ACTUALES")           
            elif A8_Global>LimiteAccion and A8_Global<LimitePermisible:
                print("El riesgo evaluado es MEDIO. El A(8) Global está entre el Limite de Acción y el Limite Permisible")
                print("RECOMENDACION:APLICAR MEDIDAS DE INTERVENCION A MEDIANO PLAZO")
            else:
                print("El riesgo evaluado es ALTO. El A(8) Global está por encima del Limite Permisible")
                print("RECOMENDACION:APLICAR MEDIDAS DE INTERVENCION A CORTO PLAZO")
elif TipoVibracion=="2":
    FuentesVibracion=input("Ingrese, A (Una fuente) o B (Varias fuentes): ")

    import math

    def CalculoA8parcialxy(n1,n2):
        A8Parcial=1.4*n1*math.sqrt(n2/8)
        return A8Parcial
    
    def CalculoA8WBVFuentes(n1,n2):
        CalculoA8=n1*math.sqrt(n2/8)
        return CalculoA8
    
    def CalculoAPonderadaWBVFuentes(n1,n2):
        AceleracionPonderadaEje=math.sqrt(n1**2+n2**2)
        return AceleracionPonderadaEje
    
    if FuentesVibracion=="A":
        ax=float(input("Ingrese el valor de la aceleracion en el eje X de la fuente en m/s2: "))
        ay=float(input("Ingrese el valor de la aceleracion en el eje y de la fuente en m/s2: "))
        az=float(input("Ingrese el valor de la aceleracion en el eje z de la fuente en m/s2: "))
        Texp=float(input("Ingrese el valor del tiempo de exposición en horas de la fuente: "))

        #CALCULAR EL A8 EN CADA EJE

        A8x=CalculoA8parcialxy(ax,Texp)
        print("El resultado de la aceleración de 8 horas en el eje x es: {:.2f} m/s2".format(A8x))
        A8y=CalculoA8parcialxy(ay,Texp)
        print("El resultado de la aceleración de 8 horas en el eje y es: {:.2f} m/s2".format(A8y))
        A8z=CalculoA8WBVFuentes(az,Texp)
        print("El resultado de la aceleración de 8 horas en el eje z es: {:.2f} m/s2".format(A8z))
        A8=max(A8x,A8y,A8z)
        print("El resultado de la aceleración de 8 horas es: {:.2f} m/s2".format(A8))
        
        Limitedeaccion=0.5
        LimitePermisible=1.15 
        if A8<Limitedeaccion:
            print("El riesgo es BAJO. El A8 está por debajo del Limite de acción")
            print("RECOMENDACION:MANTENER LAS MEDIDAS DE INTERVENCION ACTUALES")
        elif A8>Limitedeaccion and A8<LimitePermisible:
            print("El riesgo es MEDIO. El A8 está entre el Limite de acción y el Limite Permisible")
            print("RECOMENDACION:APLICAR MEDIDAS DE INTERVENCION A MEDIANO PLAZO")
        else:
            print("El riesgo es ALTO. El A8 está por encima del Limite Permisible")
            print("RECOMENDACION:APLICAR MEDIDAS DE INTERVENCION A CORTO PLAZO")
    
    elif FuentesVibracion=="B":
        
        #INGRESO Y CALCULO DE DATOS EN LA PRIMERA FUENTE
        ax1=float(input("Ingrese el valor de la aceleracion en el eje X de la primera fuente en m/s2: "))
        ay1=float(input("Ingrese el valor de la aceleracion en el eje y de la primera fuente en m/s2: "))
        az1=float(input("Ingrese el valor de la aceleracion en el eje z de la primera fuente en m/s2: "))
        Texp1=float(input("Ingrese el valor del tiempo de exposición en horas de la primera fuente: "))
        A8x1=CalculoA8parcialxy(ax1,Texp1)
        print("El resultado de A8 en el eje x para la primera fuente es: {:.2f} m/s2".format(A8x1))
        A8y1=CalculoA8parcialxy(ay1,Texp1)
        print("El resultado de A8 en el eje y para la primera fuente es: {:.2f} m/s2".format(A8y1))
        A8z1=CalculoA8WBVFuentes(az1,Texp1)
        print("El resultado de A8 en el eje z para la primera fuente es: {:.2f} m/s2".format(A8z1))
    
        #INGRESO Y CALCULO DE DATOS EN LA SEGUNDA FUENTE
        ax2=float(input("Ingrese el valor de la aceleracion en el eje X de la Segunda fuente en m/s2: "))
        ay2=float(input("Ingrese el valor de la aceleracion en el eje y de la Segunda fuente en m/s2: "))
        az2=float(input("Ingrese el valor de la aceleracion en el eje z de la Segunda fuente en m/s2: "))
        Texp2=float(input("Ingrese el valor del tiempo de exposición en horas de la Segunda fuente: "))
        A8x2=CalculoA8parcialxy(ax2,Texp2)
        print("El resultado de A8 en el eje x para la segunda fuente es: {:.2f} m/s2".format(A8x2))
        A8y2=CalculoA8parcialxy(ay2,Texp2)
        print("El resultado de A8 en el eje y para la segunda fuente es: {:.2f} m/s2".format(A8y2))
        A8z2=CalculoA8WBVFuentes(az2,Texp2)
        print("El resultado de A8 en el eje z para la segunda fuente es: {:.2f} m/s2".format(A8z2))

        #CALCULO DE VALORES GLOBALES EN CADA EJE
        A8xGlobal=CalculoAPonderadaWBVFuentes(A8x1,A8x2)
        print("El resultado de A8xGlobal es: {:.2F} m/s2".format(A8xGlobal))
        A8yGLobal=CalculoAPonderadaWBVFuentes(A8y1,A8y2)
        print("El resultado de A8yGlobal es: {:.2F} m/s2".format(A8yGLobal))
        A8zGlobal=CalculoAPonderadaWBVFuentes(A8z1,A8z2)
        print("El resultado de A8yGlobal es: {:.2F} m/s2".format(A8zGlobal))

        #CALCULO DEL A(8) Y VALORACION DEL RIESGO

        A8T=max(A8xGlobal,A8yGLobal,A8zGlobal)
        print("El resultado de A8 es: {:.2F} m/s2".format(A8T))

        Limitedeaccion=0.5
        LimitePermisible=1.15 
        if A8T<Limitedeaccion:
            print("El riesgo es BAJO. El A8 está por debajo del Limite de acción")
            print("RECOMENDACION:MANTENER LAS MEDIDAS DE INTERVENCION ACTUALES")
        elif A8T>Limitedeaccion and A8T<LimitePermisible:
            print("El riesgo es MEDIO. El A8 está entre el Limite de acción y el Limite Permisible")
            print("RECOMENDACION:APLICAR MEDIDAS DE INTERVENCION A MEDIANO PLAZO")
        else:
            print("El riesgo es ALTO. El A8 está por encima del Limite Permisible")
            print("RECOMENDACION:APLICAR MEDIDAS DE INTERVENCION A CORTO PLAZO")