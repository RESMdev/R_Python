import random

def juego():
    # Generar el número aleatorio
    numero = random.randint(1, 100)
    intentos = 0
    puntuacion = 100

    while True:
        # Incrementar el número de intentos
        intentos += 1
        
        # Solicitar al usuario un número
        adivina = int(input("Adivina el número entre 1 y 100: "))
        
        # Comprobar si el número adivinado es el correcto
        if adivina == numero:
            print("¡Felicidades, has adivinado el número!")
            break
        elif adivina % numero == 0:
            print(f"El número {adivina} es un múltiplo del número generado.")
        elif numero % adivina == 0:
            print(f"El número {adivina} es un divisor del número generado.")
        else:
            print(f"El número {adivina} no es ni múltiplo ni divisor del número generado.")
    
    # Calcular la puntuación
    puntuacion -= intentos
    print(f"Tu puntuación final es: {puntuacion}")

def main():
    juego()

if __name__ == "__main__":
    main()
