#Crea una función llamada word_length que dada una lista de palabras, devuelva una nueva lista con la longitud de cada una siempre y cuando 
# la palabra no sea "el".

def word_length(lista):
    return [len(i) for i in lista if i != "el"]

def main():
    lista=["saber", "verdad", "creencia", "opinion", "yo", "dualismo", "el"]
    res=word_length(lista)
    print (res)

if __name__ == "__main__":
    main()