def configuracionAlarma(dia, vacaciones):
    if vacaciones:  # Si estás de vacaciones
        if dia in ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes"]:
            alarma = "10:00"
        else:
            return "La alarma no sonará"
    else:  # Si NO estás de vacaciones
        if dia in ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes"]:
            alarma = "8:00"
        else:
            alarma = "10:00"
    
    return f"La alarma sonará a las {alarma}"

def main():
    dia = input("Dime un día de la semana: ").strip().lower()
    vacaciones = input("¿Estarás de vacaciones ese día? (sí/no): ").strip().lower() == "sí"

    resultado = configuracionAlarma(dia, vacaciones)
    print(resultado)

# Llamada a la función main
if __name__ == "__main__":
    main()
