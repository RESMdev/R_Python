def verificar_posicion(lista, numero):
    # Verificar si el número está en la primera o última posición de la lista
    if lista[0] == numero:
        return "El número está en la primera posición."
    elif lista[-1] == numero:
        return "El número está en la última posición."
    else:
        return "El número no está ni en la primera ni en la última posición."

def main():
    # Crear una lista de enteros
    lista = [int(x) for x in input("Introduce los números de la lista separados por espacio: ").split()]
    
    # Verificar que la longitud de la lista sea al menos 1
    if len(lista) < 1:
        print("La lista debe tener al menos un elemento.")
        return
    
    # Pedir al usuario que ingrese un número para verificar su posición
    numero = int(input("Introduce un número para verificar si está en la primera o última posición: "))
    
    # Llamar a la función para verificar la posición
    resultado = verificar_posicion(lista, numero)
    print(resultado)

if __name__ == "__main__":
    main()
