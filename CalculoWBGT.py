#SELECCION DEL METODO (INTERIORES/EXTERIORES)

TipoWBGT=input("Indique si el trabajo es, con exposición solar (SI/NO): ")
if TipoWBGT=="SI":
    
    #INGRESO DE DATOS PARA EL CALCULO
    TH=float(input("Indique el valor de la Temperatura Húmeda: "))
    TG=float(input("Indique el valor de la Temperatura de Globo: "))
    TS=float(input("Indique el valor de la Temperatura Seca: "))
    M=float(input("Indique el valor de la Carga Termica: "))

    #CRITERIOS DE VALORACION (CARGA TERMICA)
    if M<200:
        print(f"La carga térmica es Liviano")
    elif M>=200 and M<300:
        print(f"La carga térmica es Moderado")
    else:
        print(f"La carga térmica es Pesado")
    
    #CALCULO DEL INDICE WBGT EXTERIOR
    WBGTExterior=float(0.7*TH+0.2*TG+0.1*TS)
    print(f"El WBGT con exposición solar es:{WBGTExterior}")

    #INGRESO DE DATOS Y DECLARACION DE LIMITES DE ACCION Y PERMISIBLES
    CicloTrabajo=input("Indique ciclo de trabajo(Continuo, 75%Trabajo, 50%Trabajo, 25%Trabajo): ")
    CargaTrabajo=input("Indique carga de trabajo(Liviano, Moderado, Pesado): ")
    LimiteAccion1=28
    LimitePermisible1=31
    LimiteAccion2=28
    LimitePermisible2=31
    LimiteAccion3=29.5
    LimitePermisible3=32
    LimiteAccion4=30
    LimitePermisible4=32.5
    LimiteAccion5=25
    LimitePermisible5=28
    LimiteAccion6=26
    LimitePermisible6=29
    LimiteAccion7=27
    LimitePermisible7=30
    LimiteAccion8=29
    LimitePermisible8=31.5
    LimiteAccion9=24
    LimitePermisible9=27.5
    LimiteAccion10=25.5
    LimitePermisible10=29
    LimiteAccion11=28
    LimitePermisible11=30.5
    LimiteAccion12=24.5
    LimitePermisible12=28
    LimiteAccion13=27
    LimitePermisible13=30
    
    #CRITERIOS DE VALORACION DEL RIESGO
    if CicloTrabajo=="Continuo" and CargaTrabajo=="Liviano":
        print(f"El Limite de acción es: {LimiteAccion1} y el Limite Permisible es: {LimitePermisible1}")
        if WBGTExterior<LimiteAccion1:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion1}")
        elif WBGTExterior>LimitePermisible1:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible1}")
        elif LimiteAccion1<WBGTExterior<LimitePermisible1:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion1} y el {LimitePermisible1}")
    elif CicloTrabajo=="75%Trabajo" and CargaTrabajo=="Liviano":
        print(f"El Limite de acción es: {LimiteAccion2} y el Limite Permisible es: {LimitePermisible2}")
        if WBGTExterior<LimiteAccion2:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion2}")
        elif WBGTExterior>LimitePermisible2:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible2}")
        elif LimiteAccion2<WBGTExterior<LimitePermisible2:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion2} y el {LimitePermisible2}")
    elif CicloTrabajo=="50%Trabajo" and CargaTrabajo=="Liviano":
        print(f"El Limite de acción es: {LimiteAccion3} y el Limite Permisible es: {LimitePermisible3}")
        if WBGTExterior<LimiteAccion3:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion3}")
        elif WBGTExterior>LimitePermisible3:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible3}")
        elif LimiteAccion3<WBGTExterior<LimitePermisible3:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion3} y el {LimitePermisible3}")
    elif CicloTrabajo=="25%Trabajo" and CargaTrabajo=="Liviano":
        print(f"El Limite de acción es: {LimiteAccion4} y el Limite Permisible es: {LimitePermisible4}")
        if WBGTExterior<LimiteAccion4:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion4}")
        elif WBGTExterior>LimitePermisible4:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible4}")
        elif LimiteAccion4<WBGTExterior<LimitePermisible4:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion4} y el {LimitePermisible4}")
    elif CicloTrabajo=="Continuo" and CargaTrabajo=="Moderado":
        print(f"El Limite de acción es: {LimiteAccion5} y el Limite Permisible es: {LimitePermisible5}")
        if WBGTExterior<LimiteAccion5:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion5}")
        elif WBGTExterior>LimitePermisible5:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible5}")
        elif LimiteAccion5<WBGTExterior<LimitePermisible5:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion5} y el {LimitePermisible5}")
    elif CicloTrabajo=="75%Trabajo" and CargaTrabajo=="Moderado":
        print(f"El Limite de acción es: {LimiteAccion6} y el Limite Permisible es: {LimitePermisible6}")
        if WBGTExterior<LimiteAccion6:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion6}")
        elif WBGTExterior>LimitePermisible6:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible6}")
        elif LimiteAccion6<WBGTExterior<LimitePermisible6:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion6} y el {LimitePermisible6}")
    elif CicloTrabajo=="50%Trabajo" and CargaTrabajo=="Moderado":
        print(f"El Limite de acción es: {LimiteAccion7} y el Limite Permisible es: {LimitePermisible7}")
        if WBGTExterior<LimiteAccion7:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion7}")
        elif WBGTExterior>LimitePermisible7:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible7}")
        elif LimiteAccion7<WBGTExterior<LimitePermisible7:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion7} y el {LimitePermisible7}")
    elif CicloTrabajo=="25%Trabajo" and CargaTrabajo=="Moderado":
        print(f"El Limite de acción es: {LimiteAccion8} y el Limite Permisible es: {LimitePermisible8}")
        if WBGTExterior<LimiteAccion8:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion8}")
        elif WBGTExterior>LimitePermisible8:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible8}")
        elif LimiteAccion8<WBGTExterior<LimitePermisible8:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion8} y el {LimitePermisible8}")
    elif CicloTrabajo=="75%Trabajo" and CargaTrabajo=="Pesado":
        print(f"El Limite de acción es: {LimiteAccion9} y el Limite Permisible es: {LimitePermisible9}")
        if WBGTExterior<LimiteAccion9:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion9}")
        elif WBGTExterior>LimitePermisible9:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible9}")
        elif LimiteAccion9<WBGTExterior<LimitePermisible9:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion9} y el {LimitePermisible9}")
    elif CicloTrabajo=="50%Trabajo" and CargaTrabajo=="Pesado":
        print(f"El Limite de acción es: {LimiteAccion10} y el Limite Permisible es: {LimitePermisible10}")
        if WBGTExterior<LimiteAccion10:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion10}")
        elif WBGTExterior>LimitePermisible10:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible10}")
        elif LimiteAccion10<WBGTExterior<LimitePermisible10:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion10} y el {LimitePermisible10}")
    elif CicloTrabajo=="25%Trabajo" and CargaTrabajo=="Pesado":
        print(f"El Limite de acción es: {LimiteAccion11} y el Limite Permisible es: {LimitePermisible11}")
        if WBGTExterior<LimiteAccion11:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion11}")
        elif WBGTExterior>LimitePermisible11:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible11}")
        elif LimiteAccion11<WBGTExterior<LimitePermisible11:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion11} y el {LimitePermisible11}")
    elif CicloTrabajo=="50%Trabajo" and CargaTrabajo=="Muy Pesado":
        print(f"El Limite de acción es: {LimiteAccion12} y el Limite Permisible es: {LimitePermisible12}")
        if WBGTExterior<LimiteAccion12:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion12}")
        elif WBGTExterior>LimitePermisible12:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible12}")
        elif LimiteAccion12<WBGTExterior<LimitePermisible12:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion12} y el {LimitePermisible12}")
    else:
        print(f"El Limite de acción es: {LimiteAccion13} y el Limite Permisible es: {LimitePermisible13}")
        if WBGTExterior<LimiteAccion13:
            print(f"El riesgo es BAJO. EL WBGTExterior se encuentra por debajo de {LimiteAccion13}")
        elif WBGTExterior>LimitePermisible13:
            print(f"El riesgo es ALTO. EL WBGTExterior se encuentra por encima de {LimitePermisible13}")
        elif LimiteAccion13<WBGTExterior<LimitePermisible13:
            print(f"El riesgo es MEDIO. EL WBGTExterior se encuentra entre el {LimiteAccion13} y el {LimitePermisible13}")
else:     
    #INGRESO DE DATOS PARA EL CALCULO
    TH=float(input("Indique el valor de la Temperatura Húmeda: "))
    TG=float(input("Indique el valor de la Temperatura de Globo: "))
    M=float(input("Indique el valor de la Carga Térmica: "))
    
    #CRITERIOS DE VALORACION PARA LA CARGA TERMICA
    if M<200:
        print(f"La carga térmica es Liviano")
    elif M>=200 and M<300:
        print(f"La carga térmica es Moderado")
    else:
        print(f"La carga térmica es Pesado")   
    
    #CALCULO DEL WBGT INTERIOR
    WBGTInterior=0.7*TH+0.3*TG
    print(f"El WBGT sin exposición solar es:{WBGTInterior}")
    
    #DECLARACION DE VARIABLES Y LIMITES (ACCION Y PERMISIBLES)
    CicloTrabajo=input("Indique ciclo de trabajo(Continuo, 75%Trabajo, 50%Trabajo, 25%Trabajo): ")
    CargaTrabajo=input("Indique carga de trabajo(Liviano, Moderado, Pesado): ")
    LimiteAccion1=28
    LimitePermisible1=31
    LimiteAccion2=28
    LimitePermisible2=31
    LimiteAccion3=29.5
    LimitePermisible3=32
    LimiteAccion4=30
    LimitePermisible4=32.5
    LimiteAccion5=25
    LimitePermisible5=28
    LimiteAccion6=26
    LimitePermisible6=29
    LimiteAccion7=27
    LimitePermisible7=30
    LimiteAccion8=29
    LimitePermisible8=31.5
    LimiteAccion9=24
    LimitePermisible9=27.5
    LimiteAccion10=25.5
    LimitePermisible10=29
    LimiteAccion11=28
    LimitePermisible11=30.5
    LimiteAccion12=24.5
    LimitePermisible12=28
    LimiteAccion13=27
    LimitePermisible13=30
    
    #CRITERIOS DE VALORACION
    if CicloTrabajo=="Continuo" and CargaTrabajo=="Liviano":
        print(f"El Limite de acción es: {LimiteAccion1} y el Limite Permisible es: {LimitePermisible1}")
        if WBGTInterior<LimiteAccion1:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion1}")
        elif WBGTInterior>LimitePermisible1:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible1}")
        elif LimiteAccion1<WBGTInterior<LimitePermisible1:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion1} y el {LimitePermisible1}")
    elif CicloTrabajo=="75%Trabajo" and CargaTrabajo=="Liviano":
        print(f"El Limite de acción es: {LimiteAccion2} y el Limite Permisible es: {LimitePermisible2}")
        if WBGTInterior<LimiteAccion2:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion2}")
        elif WBGTInterior>LimitePermisible2:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible2}")
        elif LimiteAccion2<WBGTInterior<LimitePermisible2:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion2} y el {LimitePermisible2}")
    elif CicloTrabajo=="50%Trabajo" and CargaTrabajo=="Liviano":
        print(f"El Limite de acción es: {LimiteAccion3} y el Limite Permisible es: {LimitePermisible3}")
        if WBGTInterior<LimiteAccion3:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion3}")
        elif WBGTInterior>LimitePermisible3:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible3}")
        elif LimiteAccion3<WBGTInterior<LimitePermisible3:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion3} y el {LimitePermisible3}")
    elif CicloTrabajo=="25%Trabajo" and CargaTrabajo=="Liviano":
        print(f"El Limite de acción es: {LimiteAccion4} y el Limite Permisible es: {LimitePermisible4}")
        if WBGTInterior<LimiteAccion4:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion4}")
        elif WBGTInterior>LimitePermisible4:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible4}")
        elif LimiteAccion4<WBGTInterior<LimitePermisible4:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion4} y el {LimitePermisible4}")
    elif CicloTrabajo=="Continuo" and CargaTrabajo=="Moderado":
        print(f"El Limite de acción es: {LimiteAccion5} y el Limite Permisible es: {LimitePermisible5}")
        if WBGTInterior<LimiteAccion5:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion5}")
        elif WBGTInterior>LimitePermisible5:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible5}")
        elif LimiteAccion5<WBGTInterior<LimitePermisible5:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion5} y el {LimitePermisible5}")
    elif CicloTrabajo=="75%Trabajo" and CargaTrabajo=="Moderado":
        print(f"El Limite de acción es: {LimiteAccion6} y el Limite Permisible es: {LimitePermisible6}")
        if WBGTInterior<LimiteAccion6:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion6}")
        elif WBGTInterior>LimitePermisible6:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible6}")
        elif LimiteAccion6<WBGTInterior<LimitePermisible6:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion6} y el {LimitePermisible6}")
    elif CicloTrabajo=="50%Trabajo" and CargaTrabajo=="Moderado":
        print(f"El Limite de acción es: {LimiteAccion7} y el Limite Permisible es: {LimitePermisible7}")
        if WBGTInterior<LimiteAccion7:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion7}")
        elif WBGTInterior>LimitePermisible7:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible7}")
        elif LimiteAccion7<WBGTInterior<LimitePermisible7:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion7} y el {LimitePermisible7}")
    elif CicloTrabajo=="25%Trabajo" and CargaTrabajo=="Moderado":
        print(f"El Limite de acción es: {LimiteAccion8} y el Limite Permisible es: {LimitePermisible8}")
        if WBGTInterior<LimiteAccion8:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion8}")
        elif WBGTInterior>LimitePermisible8:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible8}")
        elif LimiteAccion8<WBGTInterior<LimitePermisible8:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion8} y el {LimitePermisible8}")
    elif CicloTrabajo=="75%Trabajo" and CargaTrabajo=="Pesado":
        print(f"El Limite de acción es: {LimiteAccion9} y el Limite Permisible es: {LimitePermisible9}")
        if WBGTInterior<LimiteAccion9:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion9}")
        elif WBGTInterior>LimitePermisible9:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible9}")
        elif LimiteAccion9<WBGTInterior<LimitePermisible9:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion9} y el {LimitePermisible9}")
    elif CicloTrabajo=="50%Trabajo" and CargaTrabajo=="Pesado":
        print(f"El Limite de acción es: {LimiteAccion10} y el Limite Permisible es: {LimitePermisible10}")
        if WBGTInterior<LimiteAccion10:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion10}")
        elif WBGTInterior>LimitePermisible10:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible10}")
        elif LimiteAccion10<WBGTInterior<LimitePermisible10:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion10} y el {LimitePermisible10}")
    elif CicloTrabajo=="25%Trabajo" and CargaTrabajo=="Pesado":
        print(f"El Limite de acción es: {LimiteAccion11} y el Limite Permisible es: {LimitePermisible11}")
        if WBGTInterior<LimiteAccion11:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion11}")
        elif WBGTInterior>LimitePermisible11:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible11}")
        elif LimiteAccion11<WBGTInterior<LimitePermisible11:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion11} y el {LimitePermisible11}")
    elif CicloTrabajo=="50%Trabajo" and CargaTrabajo=="Muy Pesado":
        print(f"El Limite de acción es: {LimiteAccion12} y el Limite Permisible es: {LimitePermisible12}")
        if WBGTInterior<LimiteAccion12:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion12}")
        elif WBGTInterior>LimitePermisible12:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible12}")
        elif LimiteAccion12<WBGTInterior<LimitePermisible12:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion12} y el {LimitePermisible12}")
    else:
        print(f"El Limite de acción es: {LimiteAccion13} y el Limite Permisible es: {LimitePermisible13}")
        if WBGTInterior<LimiteAccion13:
            print(f"El riesgo es BAJO. EL WBGTInterior se encuentra por debajo de {LimiteAccion13}")
        elif WBGTInterior>LimitePermisible13:
            print(f"El riesgo es ALTO. EL WBGTInterior se encuentra por encima de {LimitePermisible13}")
        elif LimiteAccion13<WBGTInterior<LimitePermisible13:
            print(f"El riesgo es MEDIO. EL WBGTInterior se encuentra entre el {LimiteAccion13} y el {LimitePermisible13}")