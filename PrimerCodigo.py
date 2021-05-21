ValorIngresos=float(input("Por favor, coloque a continuacion sus ingresos: "))
ValorCostos=float(input("Por favor, coloque a continuacion sus costos: "))
UtilidadBruta=ValorIngresos-ValorCostos
print(f"la utilidad bruta de la empresa es: {UtilidadBruta} ")
ValorGastos=float(input("Por favor, coloque a continuacion sus gastos: "))
UtilidadOperativa=UtilidadBruta-ValorGastos
print(f"la utilidad operativa de la empresa es: {UtilidadOperativa} ")
ImpuestoRenta=UtilidadOperativa*30/100
UtilidadNeta=UtilidadBruta-ImpuestoRenta
print(f"El valor del Impuesto de renta es: {ImpuestoRenta} pesos")
print(f"El valor de la Utilidad neta es: {UtilidadNeta} pesos")
if UtilidadNeta>100000:
    print("Mayor de 100000 pesos, es ganancia")
else:
    print("Menor de 100000 pesos, es una perdida")