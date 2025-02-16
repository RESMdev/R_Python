#Escribe una función generadora de la secuencia de Fibonacci y comprueba su 
# correcto funcionamiento. Los valores de esta secuencia se calculan siguiendo 
# la siguiente fórmula:
#F0=0 
#F1=1 
#Fn=Fn−1+Fn−2 ∀n>1


def fibonacciGenerador():
    f0, f1 = 0, 1  # Inicializamos los primeros dos términos
    yield f0  # Retorna el primer número de Fibonacci
    yield f1  # Retorna el segundo número de Fibonacci
    
    while True:
        fn = f0 + f1  # Calcula el siguiente número
        yield fn  # Retorna el siguiente número de Fibonacci
        f0, f1 = f1, fn  # Actualiza f0 y f1 para la siguiente iteración

def main():
    # Creamos el generador
    fib_gen = fibonacciGenerador()

    # Pedimos los primeros 5 números de la secuencia de Fibonacci
    print("Primer número:", next(fib_gen))  # F0
    print("Segundo número:", next(fib_gen))  # F1
    print("Tercer número:", next(fib_gen))  # F2
    print("Cuarto número:", next(fib_gen))  # F3
    print("Quinto número:", next(fib_gen))  # F4

if __name__ == "__main__":
    main()
