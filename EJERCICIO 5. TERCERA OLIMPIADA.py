#REGISTRO DE EMPLEADOS CON CONDICIONALES

# 0: Listas iniciales
nombres = ["Juan", "María", "Pedro"]
cargos = ["Auxiliar", "Técnico", "Analista"]

# 1: Si "Pedro" está en nombres, añade "Lucía"
if nombres[0] == "Pedro" or nombres[1] == "Pedro" or nombres[2] == "Pedro":
    nombres.append("Lucía")

# 2: Si "Analista" está en cargos, añade "Coordinador"
if cargos[0] == "Analista" or cargos[1] == "Analista" or cargos[2] == "Analista":
    cargos.append("Coordinador")

# 3: Si "María" está en nombres, elimínala
if nombres[0] == "María":
    nombres.pop(0)
elif nombres[1] == "María":
    nombres.pop(1)
elif len(nombres) > 2 and nombres[2] == "María":
    nombres.pop(2)

# 4: Si longitud de nombres > 3, eliminar primer elemento
if len(nombres) > 3:
    nombres.pop(0)

# 5: Si "Juan" está en nombres, reemplazar por "Julián"
if len(nombres) > 0 and nombres[0] == "Juan":
    nombres.remove("Juan")
    nombres.append("Julián")
elif len(nombres) > 1 and nombres[1] == "Juan":
    nombres.remove("Juan")
    nombres.append("Julián")
elif len(nombres) > 2 and nombres[2] == "Juan":
    nombres.remove("Juan")
    nombres.append("Julián")

# 6: Crear equipo 1 con los dos primeros de nombres
equipol = [nombres[0], nombres[1]]

# 7: Crear puestos_clave con los dos últimos de cargos
puestos_clave = [cargos[-2], cargos[-1]]

# 8: Si están "Lucía" y "Coordinador", crear tupla
lucia_en_nombres = False
if nombres[0] == "Lucía":
    lucia_en_nombres = True
elif len(nombres) > 1 and nombres[1] == "Lucía":
    lucia_en_nombres = True
elif len(nombres) > 2 and nombres[2] == "Lucía":
    lucia_en_nombres = True
elif len(nombres) > 3 and nombres[3] == "Lucía":
    lucia_en_nombres = True

coordinador_en_cargos = False
if cargos[0] == "Coordinador":
    coordinador_en_cargos = True
elif cargos[1] == "Coordinador":
    coordinador_en_cargos = True
elif cargos[2] == "Coordinador":
    coordinador_en_cargos = True
elif len(cargos) > 3 and cargos[3] == "Coordinador":
    coordinador_en_cargos = True

if lucia_en_nombres and coordinador_en_cargos:
    tupla = ("Lucía", "Coordinador")

# 9: Si "Auxiliar" está en puestos_clave, eliminarlo
if puestos_clave[0] == "Auxiliar":
    puestos_clave.pop(0)
elif len(puestos_clave) > 1 and puestos_clave[1] == "Auxiliar":
    puestos_clave.pop(1)

# 10: Si "Julián" está en nombres, crear diccionario empleado
empleado_creado = False
if nombres[0] == "Julián" or (len(nombres) > 1 and nombres[1] == "Julián") or (len(nombres) > 2 and nombres[2] == "Julián") or (len(nombres) > 3 and nombres[3] == "Julián"):
    empleado = {
        "nombre": "Julián",
        "cargo": "Técnico",
        "activo": True
    }
    empleado_creado = True

# 11: Si se creó empleado, añadir contrato
if empleado_creado == True:
    empleado["contrato"] = "Indefinido"

# 12: Si "Analista" está en cargos, añadir "Practicante"
if cargos[0] == "Analista" or cargos[1] == "Analista" or cargos[2] == "Analista" or (len(cargos) > 3 and cargos[3] == "Analista"):
    cargos.append("Practicante")

# 13: Si "Lucía" no está en nombres, agregala
lucia_ya_estaba = False
if nombres[0] == "Lucía":
    lucia_ya_estaba = True
elif len(nombres) > 1 and nombres[1] == "Lucía":
    lucia_ya_estaba = True
elif len(nombres) > 2 and nombres[2] == "Lucía":
    lucia_ya_estaba = True
elif len(nombres) > 3 and nombres[3] == "Lucía":
    lucia_ya_estaba = True

if lucia_ya_estaba == False:
    nombres.append("Lucía")

# 14: Mostrar resultados
print("nombres:", nombres)
print("cargos:", cargos)
print("equipol:", equipol)
print("puestos_clave:", puestos_clave)
if empleado_creado == True:
    print("empleado:", empleado)
if lucia_en_nombres and coordinador_en_cargos:
    print("tupla:", tupla)
