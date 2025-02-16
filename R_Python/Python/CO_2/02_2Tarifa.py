def calcularTarifa(minutos):
    pagar=10
    if (minutos>180 and minutos<=240):
        pagar=minutos*0.1
    if (minutos>240):
        pagar=minutos*0.2
    return pagar
    
def main():
    #Función principal que pide la entrada del usuario y muestra la hora convertida."""
    try:
        minutos = int(input("Introduce los minutos hablados: "))
        print(calcularTarifa(minutos))
        if minutos < 0:
            print("Error: los minutos no pueden ser negativos.")
        else:
            print(f"El costo de la llamada es: ${calcularTarifa(minutos):.2f}")
    except ValueError:
        print("Entrada inválida. Introduce el número de minutos hablados numéricamente")


# Llamada a la función main
if __name__ == "__main__":
    main()