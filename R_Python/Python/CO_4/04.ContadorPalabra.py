#Escribe una función que reciba el nombre de un fichero y que muestre por pantalla cuántas veces aparece cada palabra.
def cuantasVecesAparece(nombreDelFichero, palabra):
    with open(nombreDelFichero, 'r') as archivo:
        contador = 0
        for linea in archivo:
            palabras = linea.split()
            for p in palabras:
                if p == palabra:  # Compara la palabra leída con la palabra buscada
                    contador += 1
        print(f"La palabra '{palabra}' aparece {contador} veces.")

def main():
    cuantasVecesAparece("/home/vboxuser/Documents/R_GitKraken/R_Python/R_Python/Python/CO_4/palabras_mixtas.txt", 'foca')

if __name__ == "__main__":
    main()