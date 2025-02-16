#Escribe una función que reciba un diccionario de valores numéricos y devuelva el valor mínimo de este diccionario. Muestra el resultado por pantalla.
def valorMinimo(diccionario):
    return min(diccionario.values())

def main():
    diccionario = {"a": 10, "b": 2, "c": 5, "d": 8}
    resultado = valorMinimo(diccionario)
    print(f"El valor mínimo es: {resultado}")

if __name__ == "__main__":
    main()