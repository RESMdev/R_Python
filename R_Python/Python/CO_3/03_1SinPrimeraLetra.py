# Crea una función llamada without_first_letter que dada una lista de palabras, devuelva una nueva lista con la primera letra de cada palabra eliminada.
def llamada_first_letter(lista):   
    i=0
    nuevaLista=[]
    while (i<len(lista)):
        palabra=lista[i]
        primeraLetra=palabra[0]
        nuevaLista.append(primeraLetra)
        i=i+1
    return nuevaLista


def main():
    lista = ["avion", "zapato", "casa", "rascacielos", "puente"]
    rest = llamada_first_letter(lista)
    print(rest)

if __name__ == "__main__": 
    main()
    