"""Crea una función llamada every_element_greater_than que tome por parámetro un número y una lista numérica y devuelva True si todos los elementos son mayores 
que el número pasado por parámetro y False en caso contrario.
Crea una función llamada greater_than_average que tome un parámetro x de tipo numérico, y una lista llamada data_array. La función deberá devolver cierto en 
caso de que el valor x sea mayor que la media de la lista, y falso en caso contrario.
Crea una función llamada clean_list que tome una lista de nombres de usuarios y una lista de nombres de usuarios baneados y devuelva una nueva lista con los 
usuarios no baneados."""
#Crea una función llamada get_minimum que dado una lista de números,devuelva el valor mínimo encontrado el dicho array.
def get_minum(lista):
   return min(lista)

def main():
    lista=[6, 2, 45, 100, 6, 1, 7, 83]
    rest=get_minum(lista)
    print(rest)

if __name__ == "__main__": 
    main()