#Escribe una función que reciba un diccionario y una lista de palabras. La función debe devolver un nuevo diccionario con los items del diccionario 
#cuyas claves correspondan a alguna de las palabras de la lista. Muestra el resultado por pantalla.
def filtrarDiccionario(diccionario, lista):
    # Devuelve un nuevo diccionario con solo las claves que estén en la lista
    nuevoDiccionario = {clave: diccionario[clave] for clave in lista if clave in diccionario}
    return nuevoDiccionario

def main():
    diccionario = {
        "Pedro": 80,
        "Carla": 90,
        "Alba": 100,
        "Lucas": 40,
        "Samuel": 50,
        "Cesar": 80
    }
    
    lista = ["Pedro", "Lucas", "Cesar"]  # Claves que queremos filtrar
    
    resultado = filtrarDiccionario(diccionario, lista)
    print(resultado)

if __name__ == "__main__":
    main()
