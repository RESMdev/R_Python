#Crea una función llamada greater_than_average que tome un parámetro x de tipo numérico, y una lista llamada data_array. 
# La función deberá devolver cierto en caso de que el valor x sea mayor que la media de la lista, y falso en caso contrario.

def greater_than_average(x, data_array):
    media = sum(data_array) / len(data_array)  # Calculamos la media directamente
    return x > media  # Retornamos True si x es mayor que la media

def main():
    numero = 200
    lista = [6, 2, 45, 100, 6, 1, 7, 83]
    res = greater_than_average(numero, lista)
    print(res)

if __name__ == "__main__": 
    main()
