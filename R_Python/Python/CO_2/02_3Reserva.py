def reservar(reserva, acompanyante):
    # Validar entrada
    if reserva < 0 or acompanyante < 0 or reserva > 10 or acompanyante > 10:
        print("El número ha de ser entre 0 y 10")
        return  # Salir si los valores son inválidos

    # Condición para NO tener mesa
    if reserva <= 2 or acompanyante <= 2:
        print("No tenemos mesa, lo sentimos mucho")
    # Condición para tener mesa
    elif (reserva >= 8 or acompanyante >= 8) and reserva > 2 and acompanyante > 2:
        print("Tenemos una mesa disponible")
    # Caso incierto
    else:
        print("No sabemos si tendremos mesa")

def main():
    """Función principal que pide la entrada del usuario y llama a reservar()."""
    try:
        reserva = int(input("Del 1 al 10, ¿cómo es tu estilo de vestir? "))
        acompanyante = int(input("Del 1 al 10, ¿cómo es el estilo de vestir de tu acompañante? "))

        reservar(reserva, acompanyante)  # Llamar a la función sin print()
    except ValueError:
        print("Entrada inválida. Introduce dos valores numéricos.")

# Llamada a la función main
if __name__ == "__main__":
    main()
