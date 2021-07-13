#SELECCIONAR METODO NIOSH PARA EVALUAR MUESTRAS
SeleccionMetodo=input("Ingrese, 1 para NIOSH1501, 2 para NIOSH600,  o 3 para NIOSH7300): ")

#DEFINICION DE FUNCIONES PARA EL CODIGO
def CalculoVolumenMuestra(n1,n2):
    Volumen=n1*n2
    return Volumen
def CalculoConcentracion(n1,n2):
    Concentracion=n1/n2
    return Concentracion
def CalculoConcPresp(n1,n2):
    Concentracion=(n1/n2)*1000
    return Concentracion
def CalculoCPonderada(n1,n2,n3,n4):
    Cponderada=((n1*n2)+(n3*n4))/(n2+n4)
    return Cponderada
def AjusteTLV(n1,n2):
    TLVc=(40*n1*(168-n2))/(n2*128)
    return TLVc
def IndiceRiesgo(n1,n2):
    IR=n1/n2
    return IR
def EvaluacionRiesgoIR(n1):
    if CalculoIR<0.5:
        print("El riesgo es BAJO para este contaminante, el IR está por debajo 0.5")
    elif CalculoIR>0.5 and CalculoIR<1:
        print("El riesgo es MEDIO para este contaminante, el IR está entre 0.5 y 1")
    else:
        print("El riesgo es ALTO para este contaminante, el IR está por encima de 1")

#SELECCION DEL METODO
if SeleccionMetodo=="1":
    
    #SELECCION DEL CONTAMINANTE A CALCULAR
    SeleccionContaminante=input("Ingrese, B para Benceno, T para Tolueno o X para Xileno): ")
    if SeleccionContaminante=="B":      

        #CALCULO DEL VOLUMEN DE LA MUESTRA 1 - NIOSH1501 - BENCENO
        TiempoMuestra1=int(input("Ingrese el tiempo de muestreo de la muestra1 en minutos min: "))
        FlujoCalibracion=float(input("Ingrese el flujo de calibración de la bomba en L/min: "))   
        Volumen1=CalculoVolumenMuestra(TiempoMuestra1,FlujoCalibracion)   
        print("El Volumen de la muestra1 es de: {:.1f} Litros".format(Volumen1))   
        
        #CALCULO DE LA CONCENTRACION MUESTRA 1 - NIOSH1501 (mcg/L=mg/m3) - BENCENO
        PesoMuestra1=float(input("Ingrese el peso de la muestra1 en microgramos mcg: "))
        Concentracion1=CalculoConcentracion(PesoMuestra1,Volumen1)
        print("La Concentración de la muestra1 es de: {:.2f} mg/m3".format(Concentracion1))

        #CALCULO DEL VOLUMEN DE LA MUESTRA 2 - NIOSH1501 - BENCENO       
        TiempoMuestra2=int(input("Ingrese el tiempo de muestreo de la muestra2 en minutos min: "))        
        Volumen2=CalculoVolumenMuestra(TiempoMuestra2,FlujoCalibracion)
        print("El Volumen de la muestra2 es de: {:.1f} Litros".format(Volumen2))        
             
        #CALCULO DE LA CONCENTRACION MUESTRA 2 - NIOSH1501 (mcg/L=mg/m3) - BENCENO
        PesoMuestra2=float(input("Ingrese el peso de la muestra2 en microgramos mcg: "))
        Concentracion2=CalculoConcentracion(PesoMuestra2,Volumen2)
        print("La Concentración de la muestra2 es de: {:.2f} mg/m3".format(Concentracion2))
                
        #CALCULO DE LA CONCENTRACION PONDERADA - NIOSH1501 - BENCENO
        ConcentracionPonderada=CalculoCPonderada(Concentracion1,TiempoMuestra1,Concentracion2,TiempoMuestra2)
        print("La Concentración ponderada de las muestras es de: {:.2f} mg/m3".format(ConcentracionPonderada))      
            
        #CONVERSION DE LA UNIDAD DE LA CONCENTRACION PONDERADA - NIOSH1501 - BENCENO
        PesoMolecularS=float(input("Ingrese peso molecular del BENCENO en g/mol: "))
        ConvCPonderada=(24.45*ConcentracionPonderada)/PesoMolecularS
        print("La Conversion de la Concentracion Ponderada es de: {:.2f} ppm".format(ConvCPonderada))

        #CALCULO DEL TLV AJUSTADO - NIOSH1501 - BENCENO
        TLVBenceno=float(input("Ingrese el TLV para Benceno en ppm: "))
        HorasSemanales=int(input("Ingrese las Horas Semanales de Trabajo: "))
        TLVAjustado=AjusteTLV(TLVBenceno,HorasSemanales)
        print("El TLV ajustado del Benceno es de: {:.2f} ppm".format(TLVAjustado))
        
        #CALCULO DEL INDICE DE RIESGO IR - NIOSH1501 - BENCENO
        CalculoIR=IndiceRiesgo(ConvCPonderada,TLVAjustado)
        print("El Indice de Riesgo IR para BENCENO es de: {:.2f}".format(CalculoIR))
        
        #VALORACION DEL INDICE DE RIESGO IR - NIOSH600
        ValoracionIR=EvaluacionRiesgoIR(CalculoIR)

    elif SeleccionContaminante=="T":
        
        #CALCULO DEL VOLUMEN DE LA MUESTRA 1 - NIOSH1501 - TOLUENO
        TiempoMuestra1=int(input("Ingrese el tiempo de muestreo de la muestra1 en minutos min: "))
        FlujoCalibracion=float(input("Ingrese el flujo de calibración de la bomba en L/min: "))   
        Volumen1=CalculoVolumenMuestra(TiempoMuestra1,FlujoCalibracion)   
        print("El Volumen de la muestra1 es de: {:.1f} Litros".format(Volumen1))   
        
        #CALCULO DE LA CONCENTRACION MUESTRA 1 - NIOSH1501 (mcg/L=mg/m3) - TOLUENO
        PesoMuestra1=float(input("Ingrese el peso de la muestra1 en microgramos mcg: "))
        Concentracion1=CalculoConcentracion(PesoMuestra1,Volumen1)
        print("La Concentración de la muestra1 es de: {:.2f} mg/m3".format(Concentracion1))

        #CALCULO DEL VOLUMEN DE LA MUESTRA 2 - NIOSH1501 - TOLUENO       
        TiempoMuestra2=int(input("Ingrese el tiempo de muestreo de la muestra2 en minutos min: "))        
        Volumen2=CalculoVolumenMuestra(TiempoMuestra2,FlujoCalibracion)
        print("El Volumen de la muestra2 es de: {:.1f} Litros".format(Volumen2))        
             
        #CALCULO DE LA CONCENTRACION MUESTRA 2 - NIOSH1501 (mcg/L=mg/m3) - TOLUENO
        PesoMuestra2=float(input("Ingrese el peso de la muestra2 en microgramos mcg: "))
        Concentracion2=CalculoConcentracion(PesoMuestra2,Volumen2)
        print("La Concentración de la muestra2 es de: {:.2f} mg/m3".format(Concentracion2))
                
        #CALCULO DE LA CONCENTRACION PONDERADA - NIOSH1501 - TOLUENO
        ConcentracionPonderada=CalculoCPonderada(Concentracion1,TiempoMuestra1,Concentracion2,TiempoMuestra2)
        print("La Concentración ponderada de las muestras es de: {:.2f} mg/m3".format(ConcentracionPonderada))      
            
        #CONVERSION DE LA UNIDAD DE LA CONCENTRACION PONDERADA - NIOSH1501 - TOLUENO
        PesoMolecularS=float(input("Ingrese peso molecular del TOLUENO en g/mol: "))
        ConvCPonderada=(24.45*ConcentracionPonderada)/PesoMolecularS
        print("La Conversion de la Concentracion Ponderada es de: {:.2f} ppm".format(ConvCPonderada))

        #CALCULO DEL TLV AJUSTADO - NIOSH1501 - TOLUENO
        TLVTolueno=float(input("Ingrese el TLV para Tolueno en ppm: "))
        HorasSemanales=int(input("Ingrese las Horas Semanales de Trabajo: "))
        TLVAjustado=AjusteTLV(TLVTolueno,HorasSemanales)
        print("El TLV ajustado del Tolueno es de: {:.2f} ppm".format(TLVAjustado))
        
        #CALCULO DEL INDICE DE RIESGO IR - NIOSH1501 - TOLUENO
        CalculoIR=IndiceRiesgo(ConvCPonderada,TLVAjustado)
        print("El Indice de Riesgo IR para TOLUENO es de: {:.2f}".format(CalculoIR))
        
        #VALORACION DEL INDICE DE RIESGO IR - NIOSH1501 - TOLUENO
        ValoracionIR=EvaluacionRiesgoIR(CalculoIR)

    elif SeleccionContaminante=="X":
         
        #CALCULO DEL VOLUMEN DE LA MUESTRA 1 - NIOSH1501 - XILENO
        TiempoMuestra1=int(input("Ingrese el tiempo de muestreo de la muestra1 en minutos min: "))
        FlujoCalibracion=float(input("Ingrese el flujo de calibración de la bomba en L/min: "))   
        Volumen1=CalculoVolumenMuestra(TiempoMuestra1,FlujoCalibracion)   
        print("El Volumen de la muestra1 es de: {:.1f} Litros".format(Volumen1))   
        
        #CALCULO DE LA CONCENTRACION MUESTRA 1 - NIOSH1501 (mcg/L=mg/m3) - XILENO
        PesoMuestra1=float(input("Ingrese el peso de la muestra1 en microgramos mcg: "))
        Concentracion1=CalculoConcentracion(PesoMuestra1,Volumen1)
        print("La Concentración de la muestra1 es de: {:.2f} mg/m3".format(Concentracion1))

        #CALCULO DEL VOLUMEN DE LA MUESTRA 2 - NIOSH1501 - XILENO       
        TiempoMuestra2=int(input("Ingrese el tiempo de muestreo de la muestra2 en minutos min: "))        
        Volumen2=CalculoVolumenMuestra(TiempoMuestra2,FlujoCalibracion)
        print("El Volumen de la muestra2 es de: {:.1f} Litros".format(Volumen2))        
             
        #CALCULO DE LA CONCENTRACION MUESTRA 2 - NIOSH1501 (mcg/L=mg/m3) - XILENO
        PesoMuestra2=float(input("Ingrese el peso de la muestra2 en microgramos mcg: "))
        Concentracion2=CalculoConcentracion(PesoMuestra2,Volumen2)
        print("La Concentración de la muestra2 es de: {:.2f} mg/m3".format(Concentracion2))
                
        #CALCULO DE LA CONCENTRACION PONDERADA - NIOSH1501 - XILENO
        ConcentracionPonderada=CalculoCPonderada(Concentracion1,TiempoMuestra1,Concentracion2,TiempoMuestra2)
        print("La Concentración ponderada de las muestras es de: {:.2f} mg/m3".format(ConcentracionPonderada))      
            
        #CONVERSION DE LA UNIDAD DE LA CONCENTRACION PONDERADA - NIOSH1501 - XILENO
        PesoMolecularS=float(input("Ingrese peso molecular del XILENO en g/mol: "))
        ConvCPonderada=(24.45*ConcentracionPonderada)/PesoMolecularS
        print("La Conversion de la Concentracion Ponderada es de: {:.2f} ppm".format(ConvCPonderada))

        #CALCULO DEL TLV AJUSTADO - NIOSH1501 - XILENO
        TLVXileno=float(input("Ingrese el TLV para XILENO en ppm: "))
        HorasSemanales=int(input("Ingrese las Horas Semanales de Trabajo: "))
        TLVAjustado=AjusteTLV(TLVXileno,HorasSemanales)
        print("El TLV ajustado del XILENO es de: {:.2f} ppm".format(TLVAjustado))
        
        #CALCULO DEL INDICE DE RIESGO IR - NIOSH1501 - XILENO
        CalculoIR=IndiceRiesgo(ConvCPonderada,TLVAjustado)
        print("El Indice de Riesgo IR para XILENO es de: {:.2f}".format(CalculoIR))
        
        #VALORACION DEL INDICE DE RIESGO IR - NIOSH1501 - XILENO
        ValoracionIR=EvaluacionRiesgoIR(CalculoIR)

elif SeleccionMetodo=="2":
    
        #CALCULO DEL VOLUMEN DE LA MUESTRA 1 - NIOSH600 - MATERIAL PARTICULADO (POLVO RESPIRABLE)
        TiempoMuestra1=int(input("Ingrese el tiempo de muestreo de la muestra1 en minutos min: "))
        FlujoCalibracion=float(input("Ingrese el flujo de calibración de la bomba en L/min: "))   
        Volumen1=CalculoVolumenMuestra(TiempoMuestra1,FlujoCalibracion)   
        print("El Volumen de la muestra1 es de: {:.1f} Litros".format(Volumen1))   
        
        #CALCULO DE LA CONCENTRACION MUESTRA 1 - NIOSH600 - MATERIAL PARTICULADO (POLVO RESPIRABLE)
        PesoMuestra1=float(input("Ingrese el peso de la muestra1 en miligramos mg: "))
        Concentracion1=CalculoConcPresp(PesoMuestra1,Volumen1)
        print("La Concentración de la muestra1 es de: {:.2f} mg/m3".format(Concentracion1))

        #CALCULO DEL VOLUMEN DE LA MUESTRA 2 - NIOSH600 - MATERIAL PARTICULADO (POLVO RESPIRABLE)       
        TiempoMuestra2=int(input("Ingrese el tiempo de muestreo de la muestra2 en minutos min: "))        
        Volumen2=CalculoVolumenMuestra(TiempoMuestra2,FlujoCalibracion)
        print("El Volumen de la muestra2 es de: {:.1f} Litros".format(Volumen2))        
             
        #CALCULO DE LA CONCENTRACION MUESTRA 2 - NIOSH600 - MATERIAL PARTICULADO (POLVO RESPIRABLE)
        PesoMuestra2=float(input("Ingrese el peso de la muestra2 en miligramos mg: "))
        Concentracion2=CalculoConcPresp(PesoMuestra2,Volumen2)
        print("La Concentración de la muestra2 es de: {:.2f} mg/m3".format(Concentracion2))
                
        #CALCULO DE LA CONCENTRACION PONDERADA - NIOSH600 - MATERIAL PARTICULADO (POLVO RESPIRABLE)
        ConcentracionPonderada=CalculoCPonderada(Concentracion1,TiempoMuestra1,Concentracion2,TiempoMuestra2)
        print("La Concentración ponderada de las muestras es de: {:.2f} mg/m3".format(ConcentracionPonderada))      
            
        #CALCULO DEL TLV AJUSTADO - NIOSH600 - MATERIAL PARTICULADO (POLVO RESPIRABLE)
        TLVPolvoResp=float(input("Ingrese el TLV para Polvo Respirable en mg/m3: "))
        HorasSemanales=int(input("Ingrese las Horas Semanales de Trabajo: "))
        TLVAjustado=AjusteTLV(TLVPolvoResp,HorasSemanales)
        print("El TLV ajustado para Polvo Respirable es de: {:.2f} mg/m3".format(TLVAjustado))
        
        #CALCULO DEL INDICE DE RIESGO IR - NIOSH600 - MATERIAL PARTICULADO (POLVO RESPIRABLE)
        CalculoIR=IndiceRiesgo(ConcentracionPonderada,TLVAjustado)
        print("El Indice de Riesgo IR para POLVO RESPIRABLE es de: {:.2f}".format(CalculoIR))
        
        #VALORACION DEL INDICE DE RIESGO IR - NIOSH600
        ValoracionIR=EvaluacionRiesgoIR(CalculoIR)

elif SeleccionMetodo=="3":
    
    #SELECCION DEL CONTAMINANTE A CALCULAR
    SeleccionContaminante=input("Ingrese, Pb para Plomo, Cr para Cromo o Ni para Niquel): ")
    if SeleccionContaminante=="Pb":      

        #CALCULO DEL VOLUMEN DE LA MUESTRA 1 - NIOSH7300 - PLOMO
        TiempoMuestra1=int(input("Ingrese el tiempo de muestreo de la muestra1 en minutos min: "))
        FlujoCalibracion=float(input("Ingrese el flujo de calibración de la bomba en L/min: "))   
        Volumen1=CalculoVolumenMuestra(TiempoMuestra1,FlujoCalibracion)   
        print("El Volumen de la muestra1 es de: {:.1f} Litros".format(Volumen1))   
        
        #CALCULO DE LA CONCENTRACION MUESTRA 1 - NIOSH7300 - PLOMO
        PesoMuestra1=float(input("Ingrese el peso de la muestra1 en microgramos mcg: "))
        Concentracion1=CalculoConcentracion(PesoMuestra1,Volumen1)
        print("La Concentración de la muestra1 es de: {:.2f} mg/m3".format(Concentracion1))

        #CALCULO DEL VOLUMEN DE LA MUESTRA 2 - NIOSH7300 - PLOMO       
        TiempoMuestra2=int(input("Ingrese el tiempo de muestreo de la muestra2 en minutos min: "))        
        Volumen2=CalculoVolumenMuestra(TiempoMuestra2,FlujoCalibracion)
        print("El Volumen de la muestra2 es de: {:.1f} Litros".format(Volumen2))        
             
        #CALCULO DE LA CONCENTRACION MUESTRA 2 - NIOSH7300 - PLOMO
        PesoMuestra2=float(input("Ingrese el peso de la muestra2 en microgramos mcg: "))
        Concentracion2=CalculoConcentracion(PesoMuestra2,Volumen2)
        print("La Concentración de la muestra2 es de: {:.2f} mg/m3".format(Concentracion2))
                
        #CALCULO DE LA CONCENTRACION PONDERADA - NIOSH7300 - PLOMO
        ConcentracionPonderada=CalculoCPonderada(Concentracion1,TiempoMuestra1,Concentracion2,TiempoMuestra2)
        print("La Concentración ponderada de las muestras es de: {:.2f} mg/m3".format(ConcentracionPonderada))      
 
        #CALCULO DEL TLV AJUSTADO - NIOSH7300 - PLOMO
        TLVPlomo=float(input("Ingrese el TLV para PLOMO en mg/m3: "))
        HorasSemanales=int(input("Ingrese las Horas Semanales de Trabajo: "))
        TLVAjustado=AjusteTLV(TLVPlomo,HorasSemanales)
        print("El TLV ajustado para el PLOMO es de: {:.2f} ppm".format(TLVAjustado))
        
        #CALCULO DEL INDICE DE RIESGO IR - NIOSH7300 - PLOMO
        CalculoIR=IndiceRiesgo(ConcentracionPonderada,TLVAjustado)
        print("El Indice de Riesgo IR para PLOMO es de: {:.2f}".format(CalculoIR))
        
        #VALORACION DEL INDICE DE RIESGO IR - NIOSH7300 - PLOMO
        ValoracionIR=EvaluacionRiesgoIR(CalculoIR)

    if SeleccionContaminante=="Cr":      

        #CALCULO DEL VOLUMEN DE LA MUESTRA 1 - NIOSH7300 - CROMO
        TiempoMuestra1=int(input("Ingrese el tiempo de muestreo de la muestra1 en minutos min: "))
        FlujoCalibracion=float(input("Ingrese el flujo de calibración de la bomba en L/min: "))   
        Volumen1=CalculoVolumenMuestra(TiempoMuestra1,FlujoCalibracion)   
        print("El Volumen de la muestra1 es de: {:.1f} Litros".format(Volumen1))   
        
        #CALCULO DE LA CONCENTRACION MUESTRA 1 - NIOSH7300 - CROMO
        PesoMuestra1=float(input("Ingrese el peso de la muestra1 en microgramos mcg: "))
        Concentracion1=CalculoConcentracion(PesoMuestra1,Volumen1)
        print("La Concentración de la muestra1 es de: {:.2f} mg/m3".format(Concentracion1))

        #CALCULO DEL VOLUMEN DE LA MUESTRA 2 - NIOSH7300 - CROMO       
        TiempoMuestra2=int(input("Ingrese el tiempo de muestreo de la muestra2 en minutos min: "))        
        Volumen2=CalculoVolumenMuestra(TiempoMuestra2,FlujoCalibracion)
        print("El Volumen de la muestra2 es de: {:.1f} Litros".format(Volumen2))        
             
        #CALCULO DE LA CONCENTRACION MUESTRA 2 - NIOSH7300 - CROMO
        PesoMuestra2=float(input("Ingrese el peso de la muestra2 en microgramos mcg: "))
        Concentracion2=CalculoConcentracion(PesoMuestra2,Volumen2)
        print("La Concentración de la muestra2 es de: {:.2f} mg/m3".format(Concentracion2))
                
        #CALCULO DE LA CONCENTRACION PONDERADA - NIOSH7300 - CROMO
        ConcentracionPonderada=CalculoCPonderada(Concentracion1,TiempoMuestra1,Concentracion2,TiempoMuestra2)
        print("La Concentración ponderada de las muestras es de: {:.2f} mg/m3".format(ConcentracionPonderada))      
 
        #CALCULO DEL TLV AJUSTADO - NIOSH7300 - CROMO
        TLVCromo=float(input("Ingrese el TLV para CROMO en mg/m3: "))
        HorasSemanales=int(input("Ingrese las Horas Semanales de Trabajo: "))
        TLVAjustado=AjusteTLV(TLVCromo,HorasSemanales)
        print("El TLV ajustado para el CROMO es de: {:.2f} ppm".format(TLVAjustado))
        
        #CALCULO DEL INDICE DE RIESGO IR - NIOSH7300 - CROMO
        CalculoIR=IndiceRiesgo(ConcentracionPonderada,TLVAjustado)
        print("El Indice de Riesgo IR para CROMO es de: {:.2f}".format(CalculoIR))
        
        #VALORACION DEL INDICE DE RIESGO IR - NIOSH7300 - CROMO
        ValoracionIR=EvaluacionRiesgoIR(CalculoIR)

    if SeleccionContaminante=="Ni":      

        #CALCULO DEL VOLUMEN DE LA MUESTRA 1 - NIOSH7300 - NIQUEL
        TiempoMuestra1=int(input("Ingrese el tiempo de muestreo de la muestra1 en minutos min: "))
        FlujoCalibracion=float(input("Ingrese el flujo de calibración de la bomba en L/min: "))   
        Volumen1=CalculoVolumenMuestra(TiempoMuestra1,FlujoCalibracion)   
        print("El Volumen de la muestra1 es de: {:.1f} Litros".format(Volumen1))   
        
        #CALCULO DE LA CONCENTRACION MUESTRA 1 - NIOSH7300 - NIQUEL
        PesoMuestra1=float(input("Ingrese el peso de la muestra1 en microgramos mcg: "))
        Concentracion1=CalculoConcentracion(PesoMuestra1,Volumen1)
        print("La Concentración de la muestra1 es de: {:.2f} mg/m3".format(Concentracion1))

        #CALCULO DEL VOLUMEN DE LA MUESTRA 2 - NIOSH7300 - NIQUEL       
        TiempoMuestra2=int(input("Ingrese el tiempo de muestreo de la muestra2 en minutos min: "))        
        Volumen2=CalculoVolumenMuestra(TiempoMuestra2,FlujoCalibracion)
        print("El Volumen de la muestra2 es de: {:.1f} Litros".format(Volumen2))        
             
        #CALCULO DE LA CONCENTRACION MUESTRA 2 - NIOSH7300 - NIQUEL
        PesoMuestra2=float(input("Ingrese el peso de la muestra2 en microgramos mcg: "))
        Concentracion2=CalculoConcentracion(PesoMuestra2,Volumen2)
        print("La Concentración de la muestra2 es de: {:.2f} mg/m3".format(Concentracion2))
                
        #CALCULO DE LA CONCENTRACION PONDERADA - NIOSH7300 - NIQUEL
        ConcentracionPonderada=CalculoCPonderada(Concentracion1,TiempoMuestra1,Concentracion2,TiempoMuestra2)
        print("La Concentración ponderada de las muestras es de: {:.2f} mg/m3".format(ConcentracionPonderada))      
 
        #CALCULO DEL TLV AJUSTADO - NIOSH7300 - NIQUEL
        TLVNiquel=float(input("Ingrese el TLV para NIQUEL en mg/m3: "))
        HorasSemanales=int(input("Ingrese las Horas Semanales de Trabajo: "))
        TLVAjustado=AjusteTLV(TLVNiquel,HorasSemanales)
        print("El TLV ajustado para el NIQUEL es de: {:.2f} ppm".format(TLVAjustado))
        
        #CALCULO DEL INDICE DE RIESGO IR - NIOSH7300 - NIQUEL
        CalculoIR=IndiceRiesgo(ConcentracionPonderada,TLVAjustado)
        print("El Indice de Riesgo IR para NIQUEL es de: {:.2f}".format(CalculoIR))
        
        #VALORACION DEL INDICE DE RIESGO IR - NIOSH7300 - NIQUEL
        ValoracionIR=EvaluacionRiesgoIR(CalculoIR)