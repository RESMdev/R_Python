#Crea una función llamada squares_greater que dada una lista de números, devuelva una nueva lista con los cuadrados de aquellos números mayores que 10.
def squares_greater(lista):
    return [i**2 for i in lista if i > 10]
def main():
    lista=[2,3,4,20,10,30,40]
    res=squares_greater(lista)
    print (res)

if __name__ == "__main__":
    main()