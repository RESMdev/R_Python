#Escribe una función que reciba el nombre de un fichero que contiene palabras (cada línea tiene una palabra) y 
# que devuelva la palabra que tiene una longitud máxima y su longitud.
# Escribe una función que reciba el nombre de un fichero que contiene palabras (cada línea tiene una palabra) y 
# que devuelva la palabra que tiene una longitud máxima y su longitud.

def palabra_mas_larga(nombre_fichero):
    max_palabra = ""
    max_longitud = 0
    
    with open(nombre_fichero, "r") as file:
        for linea in file:
            palabra = linea.strip()  # Elimina espacios en blanco y saltos de línea
            if len(palabra) > max_longitud:
                max_palabra = palabra
                max_longitud = len(palabra)
    
    return max_palabra, max_longitud

# Función principal
def main():
    resultado = palabra_mas_larga("/home/vboxuser/Documents/R_GitKraken/R_Python/R_Python/Python/CO_4/palabras.txt")  # Aquí debe ir el nombre del archivo como string
    print("Palabra más larga:", resultado[0])
    print("Longitud:", resultado[1])

# Llamamos a la función main
if __name__ == "__main__":
    main()
