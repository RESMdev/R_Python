#Escribe una función que recibe el nombre de un fichero 
#(cada línea puede tener varias palabras) y una letra, y que muestre por pantalla 
#las palabras del fichero que contienen la letra.

def busqueda_por_letra(nombre_fichero, letra):
    try:
        with open(nombre_fichero, 'r') as archivo:  # Usamos 'nombre_fichero' en lugar de 'fichero'
            for linea in archivo:
                palabras = linea.split()
                for palabra in palabras:
                    if letra in palabra:
                        print(palabra)
    except FileNotFoundError:
        print(f"El archivo {nombre_fichero} no se encuentra.")

# Función principal
def main():
    # Aquí debes indicar tanto el nombre del archivo como la letra
    busqueda_por_letra("/home/vboxuser/Documents/R_GitKraken/R_Python/R_Python/Python/CO_4/palabras_mixtas.txt", 'a')

# Llamamos a la función main
if __name__ == "__main__":
    main()
