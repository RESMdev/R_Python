def convertir_hora(hora, minutos):
    """Convierte la hora de formato 24h a 12h y devuelve el resultado en una cadena."""
    if not (0 <= hora <= 23) or not (0 <= minutos <= 59):
        return "Hora inválida. Deben ser entre 0 y 23 para la hora, y entre 0 y 59 para los minutos."
    
    periodo = "AM" if hora < 12 else "PM"
    hora_12 = hora % 12
    hora_12 = 12 if hora_12 == 0 else hora_12
    
    return f"Son las {hora_12:02}:{minutos:02} {periodo}"


def main():
    """Función principal que pide la entrada del usuario y muestra la hora convertida."""
    try:
        hora = int(input("Introduce la hora: "))
        minutos = int(input("Introduce los minutos: "))
        print(convertir_hora(hora, minutos))
    except ValueError:
        print("Entrada inválida. Introduce números enteros para la hora y los minutos.")


# Llamada a la función main
if __name__ == "__main__":
    main()
