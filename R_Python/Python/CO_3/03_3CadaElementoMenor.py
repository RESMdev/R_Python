#Crea una función llamada every_element_greater_than que tome por parámetro un número y una lista numérica y devuelva True si todos los elementos son mayores 
#que el número pasado por parámetro y False en caso contrario.

def every_element_greater_than(numero, lista):
   res=False
   if(numero<min(lista)):
       res=True
   return res

def main():
    numero=5
    lista=[6, 2, 45, 100, 6, 1, 7, 83]
    res=every_element_greater_than(numero, lista)
    print(res)

if __name__ == "__main__": 
    main()