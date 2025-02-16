def factorial(numero):
    i=1
    resultado = 1
    while i<=numero:
        resultado=resultado*i
        i=i+1
        
    return resultado

def main():
    numero=int(input("Introduce un número para calcular su factorial"))
    resultado = factorial(numero)
    print("El factorial es: ", resultado)

if __name__ == "__main__":
    main()