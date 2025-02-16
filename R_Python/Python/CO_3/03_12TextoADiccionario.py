#Escribe un programa que lea un texto por teclado. Posteriormente debe crear un diccionario donde las claves sean las palabras del texto 
# y sus valores el número de apariciones de cada una de éstas en el texto. Muestra el resultado por pantalla.
def diccionarioPorTexto(texto):
    diccionario={}
    palabras = texto.split()

    for palabras in palabras:
        if palabras in diccionario:
            diccionario[palabras] +=1
        else: diccionario[palabras] =1
    return diccionario

def main():
    texto = input("Escribe un texto")
    resultado=diccionarioPorTexto(texto)
    print("Frecuencia de palabras: ")
    for palabra, cantidad in resultado.items():
        print(f"'{palabra}' : {cantidad}")
if __name__ == "__main__":
    main()