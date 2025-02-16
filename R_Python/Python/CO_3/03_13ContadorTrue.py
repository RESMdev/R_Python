def contadorTrue(diccionario):
    contador = 0
    for key in diccionario:  # Itera sobre las claves del diccionario principal
        if diccionario[key]['success'] == True:  # Verifica si 'success' es True
            contador += 1  # Incrementa el contador si es True
    return contador

def main():
    diccionario = {
        1 : {'id': 1, 'success': True, 'name': 'Lary'},
        2 : {'id': 2, 'success': False, 'name': 'Rabi'},
        3 : {'id': 3, 'success': True, 'name': 'Alex'}
    }

    res = contadorTrue(diccionario)
    print(res)

if __name__ == "__main__":
    main()
