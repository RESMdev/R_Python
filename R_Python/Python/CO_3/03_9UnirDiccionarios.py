#Escribe una función que reciba dos diccionarios con claves de tipo string y valores de tipo numérico, y que devuelva un nuevo diccionario
#que contenga los dos anteriores. Muestra el resultado por pantalla.
def juntarDicionarios(diccionarioA, diccionarioB):
     return {**diccionarioA, **diccionarioB}  # Combina ambos diccionarios

def main():
    diccionarioA={"Pedro":80, "Carla":90, "Alba":100}
    diccionarioB={"Lucas":40, "Samuel":50, "Cesar":80}
    res=juntarDicionarios(diccionarioA, diccionarioB)
    print(res)

if __name__=="__main__":
    main()