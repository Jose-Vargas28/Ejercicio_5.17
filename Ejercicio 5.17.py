# Función para obtener datos de los choferes
def obtener_datos_choferes():
    choferes = []
    for i in range(5):
        nombre = input(f"Ingrese el nombre del chofer {i + 1}: ")
        horas = []
        for j in range(6):
            horas_trabajadas = int(input(f"Ingrese las horas trabajadas el día {j + 1} para {nombre}: "))
            horas.append(horas_trabajadas)
        sueldo_hora = float(input(f"Ingrese el sueldo por hora de {nombre}: "))
        choferes.append({"nombre": nombre, "horas": horas, "sueldo_hora": sueldo_hora})
    return choferes

def calcular_horas_semanales(chofer):
    return sum(chofer["horas"])

def calcular_sueldo_semanal(chofer):
    return calcular_horas_semanales(chofer) * chofer["sueldo_hora"]

def total_a_pagar(choferes):
    return sum(calcular_sueldo_semanal(chofer) for chofer in choferes)

def trabajador_mas_horas_lunes(choferes):
    return max(choferes, key=lambda chofer: chofer["horas"][0])

def imprimir_reporte(choferes):
    print("Reporte Semanal de Choferes")
    print("="*30)
    total_empresa = 0
    for chofer in choferes:
        horas_semanales = calcular_horas_semanales(chofer)
        sueldo_semanal = calcular_sueldo_semanal(chofer)
        total_empresa += sueldo_semanal
        print(f"Nombre: {chofer['nombre']}")
        print(f"  Horas trabajadas a la semana: {horas_semanales}")
        print(f"  Sueldo semanal: ${sueldo_semanal:.2f}")
    print("="*30)
    print(f"Total que pagará la empresa: ${total_empresa:.2f}")
    chofer_lunes = trabajador_mas_horas_lunes(choferes)
    print(f"El trabajador que más horas labora el lunes es: {chofer_lunes['nombre']}")

# Obtener datos de los choferes
choferes = obtener_datos_choferes()

# Ejecutar el reporte
imprimir_reporte(choferes)
