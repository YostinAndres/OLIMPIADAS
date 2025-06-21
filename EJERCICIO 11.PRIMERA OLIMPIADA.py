dia=int(input("señor usuario ingrese el dia: "))
mes=int(input("señor usuario ingrese el mes: "))
año=int(input("señor usuario ingrese el año: "))

dias_por_mes=[31,28,31,30,31,30,31,31.30,31,30,31]
if mes < 1 or mes > 12:
    print("fecha invalida: mes incorrecto")
else:
    max_dias=dias_por_mes[mes-1]
if dia < 1 or dia > max_dias:
    print("fecha invalida: dia incorrecto")
else: 
    print("fecha valida")          