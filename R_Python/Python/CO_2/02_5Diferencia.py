def diferencia(valorA, valorB, valorC):
    if abs(sum([valorA - valorB])) <= 1 and abs(sum([valorA - valorC])) > 2 and abs(sum([valorB - valorC])) > 2:
        return "Los dos primeros números tienen una diferencia máxima de 1, y el tercero tiene una diferencia mayor que 2 con los otros dos."
    else:
        return "Los números no cumplen la condición."

def main():
    valorA = int(input("Dime un valor: "))
    valorB = int(input("Dime otro valor: "))
    valorC = int(input("Dime un último valor: "))
    resultado = diferencia(valorA, valorB, valorC)
    print(resultado)

if __name__ == "__main__":
    main()
