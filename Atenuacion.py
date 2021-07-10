import numpy as np
import math
#SELECCIONAR METODO PARA EVALUAR LA ATENUACION DE LOR PROTECTORES AUDITIVOS
SeleccionMetodo=input("""
                        Ingrese, 
                        1 (BANDAS DE OCTAVA), 
                        2 (METODO HML), 
                        3 (METODO SNR), 
                        4 (METODO NRR)
                        
                        : """)

#ESTABLECIMIENTO DE FUNCIONES PARA CALCULOS DE ATENUACION

def CalculoAPVf(n1,n2):
    ProteccionAsumida=n1-n2
    return ProteccionAsumida
def CalculoLeqfPrima(n1,n2):
    IntensidadAsumidaF=n1-n2
    return IntensidadAsumidaF
def CalculoLAeqPrima(n1,n2,n3,n4,n5,n6,n7,n8):
    IntensidadAsumidaT=10*math.log10(10**(0.1*n1)+10**(0.1*n2)+10**(0.1*n3)+10**(0.1*n4)+10**(0.1*n5)+10**(0.1*n6)+10**(0.1*n7)+10**(0.1*n8))
    return IntensidadAsumidaT
    
if SeleccionMetodo=="1":
    #BANDA FRECUENCIAS (FEECUENCIAS - INTENSIDAD)
    ListaLAeqvsF=[]
    #ENTRADA DE DATOS LAeq,F SEGUN FRECUENCIA OBTENIDAS POR MEDICION
    Intensidad1=float(input("Ingrese LAeq,f en decibeles en frecuencia de 63 Hz: "))
    ListaLAeqvsF.append(Intensidad1)
    Intensidad2=float(input("Ingrese LAeq,f en decibeles en frecuencia de 125 Hz: "))
    ListaLAeqvsF.append(Intensidad2)
    Intensidad3=float(input("Ingrese LAeq,f en decibeles en frecuencia de 250 Hz: "))
    ListaLAeqvsF.append(Intensidad3)    
    Intensidad4=float(input("Ingrese LAeq,f en decibeles en frecuencia de 500 Hz: "))
    ListaLAeqvsF.append(Intensidad4)    
    Intensidad5=float(input("Ingrese LAeq,f en decibeles en frecuencia de 1000 Hz: "))
    ListaLAeqvsF.append(Intensidad5)
    Intensidad6=float(input("Ingrese LAeq,f en decibeles en frecuencia de 2000 Hz: "))
    ListaLAeqvsF.append(Intensidad6)
    Intensidad7=float(input("Ingrese LAeq,f en decibeles en frecuencia de 4000 Hz: "))
    ListaLAeqvsF.append(Intensidad7)
    Intensidad8=float(input("Ingrese LAeq,f en decibeles en frecuencia de 8000 Hz: "))
    ListaLAeqvsF.append(Intensidad8)
    print(f"La lista de intensidades por banda de frecuencia es: {ListaLAeqvsF}")
    print(f"Las intensidades en el rango de conversacion es: {ListaLAeqvsF[3:6]}")
    ValorMaximo=max(ListaLAeqvsF[3:6])
    if ValorMaximo>80:
        print(f"Existe riesgo de HIPOACUSIA. Valor maximo en el rango de 500Hz y 2KHz: {ValorMaximo} dB")
    else:
        print("No hay riesgo de hipoacusia")   
    print("""
    --------------------------------------------------------------------------------------------------------
    """)
    #INGRESAR LOS DATOS DE VALOR MEDIA DE ATENUACION mf POR FRECUENCIA
    ListaValormf=[]
    Atenuacion1=float(input("Ingrese mf en decibeles en frecuencia de 63 Hz: "))
    ListaValormf.append(Atenuacion1)
    Atenuacion2=float(input("Ingrese mf en decibeles en frecuencia de 125 Hz: "))
    ListaValormf.append(Atenuacion2)
    Atenuacion3=float(input("Ingrese mf en decibeles en frecuencia de 250 Hz: "))
    ListaValormf.append(Atenuacion3)    
    Atenuacion4=float(input("Ingrese mf en decibeles en frecuencia de 500 Hz: "))
    ListaValormf.append(Atenuacion4) 
    Atenuacion5=float(input("Ingrese mf en decibeles en frecuencia de 1000 Hz: "))
    ListaValormf.append(Atenuacion5) 
    Atenuacion6=float(input("Ingrese mf en decibeles en frecuencia de 2000 Hz: "))
    ListaValormf.append(Atenuacion6) 
    Atenuacion7=float(input("Ingrese mf en decibeles en frecuencia de 4000 Hz: "))
    ListaValormf.append(Atenuacion7)     
    Atenuacion8=float(input("Ingrese mf en decibeles en frecuencia de 8000 Hz: "))
    ListaValormf.append(Atenuacion8)
    print(f"La lista de intensidades por banda de frecuencia es: {ListaLAeqvsF}")    
    print(f"La lista de valores medios de atenuacion mf por banda es: {ListaValormf}")     
    print("""
    --------------------------------------------------------------------------------------------------------
    """)
    #INGRESAR LOS DATOS DE DESVIACION ESTANDAR POR FRECUENCIA
    ListaDesvEstandar=[]
    Desviacion1=float(input("Ingrese desviacion estandar en frecuencia de 63 Hz: "))
    ListaDesvEstandar.append(Desviacion1)
    Desviacion2=float(input("Ingrese desviacion estandar en frecuencia de 125 Hz: "))
    ListaDesvEstandar.append(Desviacion2)
    Desviacion3=float(input("Ingrese desviacion estandar en frecuencia de 250 Hz: "))
    ListaDesvEstandar.append(Desviacion3)
    Desviacion4=float(input("Ingrese desviacion estandar en frecuencia de 500 Hz: "))
    ListaDesvEstandar.append(Desviacion4)
    Desviacion5=float(input("Ingrese desviacion estandar en frecuencia de 1000 Hz: "))
    ListaDesvEstandar.append(Desviacion5)    
    Desviacion6=float(input("Ingrese desviacion estandar en frecuencia de 2000 Hz: "))
    ListaDesvEstandar.append(Desviacion6)
    Desviacion7=float(input("Ingrese desviacion estandar en frecuencia de 4000 Hz: "))
    ListaDesvEstandar.append(Desviacion7)
    Desviacion8=float(input("Ingrese desviacion estandar en frecuencia de 8000 Hz: "))
    ListaDesvEstandar.append(Desviacion8)
    print(f"La lista de intensidades por banda de frecuencia es: {ListaLAeqvsF}")    
    print(f"La lista de valores medios de atenuacion mf por banda es: {ListaValormf}")
    print(f"La lista de valores de desviacion estandar S por banda es: {ListaDesvEstandar}")     
    print("""
    --------------------------------------------------------------------------------------------------------
    """)
    #CALCULO DE LA PROTECCION ASUMIDA POR FRECUENCIA APVf
    ListaAPVf=[]
    APVf63=CalculoAPVf(Atenuacion1, Desviacion1)
    ListaAPVf.append(APVf63)
    APVf125=CalculoAPVf(Atenuacion2, Desviacion2)
    ListaAPVf.append(APVf125)
    APVf250=CalculoAPVf(Atenuacion3, Desviacion3)
    ListaAPVf.append(APVf250)
    APVf500=CalculoAPVf(Atenuacion4, Desviacion4)
    ListaAPVf.append(APVf500)
    APVf1000=CalculoAPVf(Atenuacion5, Desviacion5)
    ListaAPVf.append(APVf1000)
    APVf2000=CalculoAPVf(Atenuacion6, Desviacion6)
    ListaAPVf.append(APVf2000)
    APVf4000=CalculoAPVf(Atenuacion7, Desviacion7)
    ListaAPVf.append(APVf4000)
    APVf8000=CalculoAPVf(Atenuacion8, Desviacion8)
    ListaAPVf.append(APVf8000)     
    print(f"La lista de intensidades por banda de frecuencia es: {ListaLAeqvsF}")    
    print(f"La lista de valores medios de atenuacion mf por banda es: {ListaValormf}")
    print(f"La lista de valores de desviacion estandar S por banda es: {ListaDesvEstandar}")
    MyList = list(np.around(np.array(ListaAPVf),2))
    print(f"Los valores de proteccion asumida APVf por banda es: {MyList}")
    print("""
    --------------------------------------------------------------------------------------------------------
    """)
    #CALCULO DE LA L'Aeq,f POR BANDA DE FRECUENCIA
    ListaLPrimaeq=[]
    LPrimaf63=CalculoLeqfPrima(Intensidad1, APVf63)
    ListaLPrimaeq.append(LPrimaf63)
    LPrimaf125=CalculoLeqfPrima(Intensidad2, APVf125)
    ListaLPrimaeq.append(LPrimaf125)
    LPrimaf250=CalculoLeqfPrima(Intensidad3, APVf250)
    ListaLPrimaeq.append(LPrimaf250)
    LPrimaf500=CalculoLeqfPrima(Intensidad4, APVf500)
    ListaLPrimaeq.append(LPrimaf500)
    LPrimaf1000=CalculoLeqfPrima(Intensidad5, APVf1000)
    ListaLPrimaeq.append(LPrimaf1000)
    LPrimaf2000=CalculoLeqfPrima(Intensidad6, APVf2000)
    ListaLPrimaeq.append(LPrimaf2000)
    LPrimaf4000=CalculoLeqfPrima(Intensidad7, APVf4000)
    ListaLPrimaeq.append(LPrimaf4000)
    LPrimaf8000=CalculoLeqfPrima(Intensidad8, APVf8000)
    ListaLPrimaeq.append(LPrimaf8000)
    print(f"La lista de intensidades por banda de frecuencia es: {ListaLAeqvsF}")    
    print(f"La lista de valores medios de atenuacion mf por banda es: {ListaValormf}")
    print(f"La lista de valores de desviacion estandar S por banda es: {ListaDesvEstandar}")
    MyList = list(np.around(np.array(ListaAPVf),2))
    print(f"Los valores de proteccion asumida APVf por banda es: {MyList}")
    MyList1 = list(np.around(np.array(ListaLPrimaeq),2))    
    print(f"Los valores de Intensidad atenuada L'Aeq,f es: {MyList1}")        
    print("""
    --------------------------------------------------------------------------------------------------------
    """)
    #CALCULO DE LAEQ PRIMA TOTAL Y VALORACION DE EFECTIVIDAD DEL PROTECTOR AUDITIVO.     
    LaeqPrimaFitrada= CalculoLAeqPrima(LPrimaf63,LPrimaf125,LPrimaf250,LPrimaf500,LPrimaf1000,LPrimaf2000,LPrimaf4000,LPrimaf8000)
    print("La intensidad atenuada con protector auditivo es: {:.1f} decibeles".format(LaeqPrimaFitrada))
    AjusteIntensidadAtenuada=LaeqPrimaFitrada+4
    print("La intensidad atenuada mas el ajuste de 4 dB es: {:.1f} decibeles".format(AjusteIntensidadAtenuada))
    if AjusteIntensidadAtenuada<80:
        print("Por lo tanto, el protector auditivo evaluado aporta ATENUACION ADECUADA")
    else:
        print("Por lo tanto, el protector auditivo evaluado suministra ATENUACION INADECUADA")
    print("""
    --------------------------------------------------------------------------------------------------------
    """)
        
elif SeleccionMetodo=="2":

    def DiferenciaDecibelesAYC(n1,n2):
        DiferenciaDB=n1-n2
        return DiferenciaDB
    
    def CalculoPNRmenor(n1,n2,n3,n4):
        ValorPNR=(n1-(n2-n1)*(n3-n4-2)/4)
        return ValorPNR
    
    def CalculoPNRmayor(n1,n2,n3,n4):
        ValordePNR=(n1-(n1-n2)*(n3-n4-2)/8)
        return ValordePNR
    
    def DiferenciaLAeqPNR(n1,n2):
        Diferencia=n1-n2
        return Diferencia
    
    #CALCULO DE LA DIFERENCIA ENTRE INTENSIDADADES CON PONDERACIONES "A" Y "C"
    ValorenDC=float(input("Ingrese la intensidad medida LCeq en decibeles C: "))
    ValorenDA=float(input("Ingrese la intensidad medida LAeq en decibeles A: "))
    DiferenciaDecibeles=DiferenciaDecibelesAYC(ValorenDC,ValorenDA)
    print(f"La diferencia entre LCeq y LAeq es de: {DiferenciaDecibeles} dB")

    #ESTIMACION DE LA ATENUACION DE NIVEL DE RUIDO, PNR MENOR O IGUAL QUE 2
    ValorH=float(input("Ingrese el valor de atenuacion H en Decibeles: "))
    ValorM=float(input("Ingrese el valor de atenuacion M en Decibeles: "))
    ValorL=float(input("Ingrese el valor de atenuacion L en Decibeles: "))
    if DiferenciaDecibeles<=2:
        ValorAtenuacionPNR=CalculoPNRmenor(ValorM,ValorH,ValorenDC,ValorenDA)
        print(f"EL valor de PNR o reduccion prevista de ruido es igual a: {ValorAtenuacionPNR} dB")
    else:
        ValorAtenuacionPNR=CalculoPNRmayor(ValorM,ValorL,ValorenDC,ValorenDA)
        print(f"EL valor de PNR o reduccion prevista de ruido es igual a: {ValorAtenuacionPNR} dB")
    
    #CALCULO DE LA INTENSIDAD EFECTIVA L'Aeq PONDERADO "A"
    LAeqPrima=DiferenciaLAeqPNR(ValorenDA,ValorAtenuacionPNR)
    print(f"La intensidad efectiva ponderada A es igual a: {LAeqPrima} dB")

    #CALCULO DE LAEQ PRIMA TOTAL Y VALORACION DE EFECTIVIDAD DEL PROTECTOR AUDITIVO.     
    AjusteIntensidadAtenuada=LAeqPrima+4
    print("La intensidad atenuada mas el ajuste de 4 dB es: {:.1f} decibeles".format(AjusteIntensidadAtenuada))
    if AjusteIntensidadAtenuada<80:
        print("Por lo tanto, el protector auditivo evaluado aporta ATENUACION ADECUADA")
    else:
        print("Por lo tanto, el protector auditivo evaluado suministra ATENUACION INADECUADA")

elif SeleccionMetodo=="3":
    #CALCULO DE LA INTENSIDAD ATENUADA L'AEQ
    ValorLCeq=float(input("Ingrese la intensidad en Decibeles C: "))
    ValorSNR=float(input("Ingrese el valor global de atenuacion SNR: "))
    LAeqPrima=ValorLCeq-ValorSNR
    print(f"El valor de la Intensidad Atenuada L'Aeq es de: {LAeqPrima} dB")

    #VALORACION DE EFECTIVIDAD DEL PROTECTOR AUDITIVO
    AjusteIntensidadAtenuada=LAeqPrima+4
    print("La intensidad atenuada mas el ajuste de 4 dB es: {:.1f} decibeles".format(AjusteIntensidadAtenuada))    
    if AjusteIntensidadAtenuada<80:
        print("Por lo tanto, el protector auditivo evaluado aporta ATENUACION ADECUADA")
    else:
        print("Por lo tanto, el protector auditivo evaluado suministra ATENUACION INADECUADA")
    
elif SeleccionMetodo=="4":
    
    def CalculodeLAeqPrimaInsercion(n1,n2):
        IntensidadAtenuada=n1-((n2-7)*0.5)
        return IntensidadAtenuada

    def CalculoLAeqPrimaCopas(n1,n2):
        IntensidadAtenuada=n1-((n2-7)*0.75)
        return IntensidadAtenuada

    def CalculoLAeqPrimaCombinados(n1,n2):
        IntensidadAtenuada=n1-(((n2-7)*0.5)+5)
        return IntensidadAtenuada    
    
    OpcionFormulaNRR=(input("Ingrese Tipo de Protector, I (Insercion), C (Copas), CM (Combinados): "))
    if OpcionFormulaNRR=="I":
        
        #CALCULO DE L'AEQ PARA LOS PROTECTORES DE INSERCION
        ValordeLAV=float(input("Ingrese el valor de Intensidad equivalente LAeq en decibeles: "))
        ValordeNRR=float(input("Ingrese el valor de atenuación NRR para protector de Inserción en decibeles: "))
        LAeqPrima=CalculodeLAeqPrimaInsercion(ValordeLAV,ValordeNRR)
        print(f"El valor de la intensidad atenuada L'Aeq es de: {LAeqPrima} decibeles")

        #VALORACION DE EFECTIVIDAD DEL PROTECTOR AUDITIVO  
        if LAeqPrima<80:
            print("Por lo tanto, el protector de inserción evaluado aporta ATENUACION ADECUADA")
        else:
            print("Por lo tanto, el protector de inserción evaluado suministra ATENUACION INADECUADA")

    elif OpcionFormulaNRR=="C":
        
        #CALCULO DE L'AEQ PARA LOS PROTECTORES DE COPAS
        ValordeLAV=float(input("Ingrese el valor de Intensidad equivalente LAeq en decibeles: "))
        ValordeNRR=float(input("Ingrese el valor de atenuación NRR para protector de Copas en decibeles: "))
        LAeqPrima=CalculoLAeqPrimaCopas(ValordeLAV,ValordeNRR)
        print(f"El valor de la intensidad atenuada L'Aeq es de: {LAeqPrima} decibeles")

        #VALORACION DE EFECTIVIDAD DEL PROTECTOR AUDITIVO  
        if LAeqPrima<80:
            print("Por lo tanto, el protector de copas evaluado aporta ATENUACION ADECUADA")
        else:
            print("Por lo tanto, el protector de copas evaluado suministra ATENUACION INADECUADA")
        
    elif OpcionFormulaNRR=="CM":
        
        #CALCULO DE L'AEQ PARA LOS PROTECTORES COMBINADOS
        ValordeLAV=float(input("Ingrese el valor de Intensidad equivalente LAeq en decibeles: "))
        ValordeNRR1=float(input("Ingrese el valor de atenuación NRR para protector de Inserción en decibeles: "))    
        ValordeNRR2=float(input("Ingrese el valor de atenuación NRR para protector de Copas en decibeles: "))
        ValorNRRh=max(ValordeNRR1,ValordeNRR2)
        LAeqPrima=CalculoLAeqPrimaCombinados(ValordeLAV,ValorNRRh)
        print(f"El valor de la intensidad atenuada L'Aeq es de: {LAeqPrima} decibeles")

        #VALORACION DE EFECTIVIDAD DEL PROTECTOR COMBINADO  
        if LAeqPrima<80:
            print("Por lo tanto, el protector combinado evaluado aporta ATENUACION ADECUADA")
        else:
            print("Por lo tanto, el protector combinado evaluado suministra ATENUACION INADECUADA")