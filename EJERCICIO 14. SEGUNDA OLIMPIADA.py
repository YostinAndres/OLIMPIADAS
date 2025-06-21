#CALCULADORA DE PORCENTAJE DE GANANCIA
costo=float(input("ingrese el costo del producto: "))
venta=float(input("ingrese el precio de venta: "))
ganancia=costo-venta
porcentaje=(ganancia/costo)*100

print("Porcentaje de ganancia: ")
print(porcentaje)
print("%")

if porcentaje > 30:
    print("alta ganancia")
elif porcentaje < 10:
    print("muy baja ganancia")
else:
    print("ganancia moderada")     