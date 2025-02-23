# Diccionario para almacenar clientes
clientes = {}

def añadir_cliente():
    nif = input("Ingrese NIF: ")
    nombre = input("Ingrese nombre: ")
    direccion = input("Ingrese dirección: ")
    telefono = input("Ingrese teléfono: ")
    email = input("Ingrese email: ")
    vip = input("¿Es VIP? (s/n): ").strip().lower() == 's'  # Convierte 's' en True

    clientes[nif] = {
        "name": nombre,
        "address": direccion,
        "phone": telefono,
        "email": email,
        "Vip": vip
    }
    print("Cliente añadido con éxito.")

def borrar_cliente():
    nif = input("Ingrese el NIF del cliente a borrar: ")
    if nif in clientes:
        del clientes[nif]
        print("Cliente eliminado correctamente.")
    else:
        print("Cliente no encontrado.")

def mostrar_cliente():
    nif = input("Ingrese el NIF del cliente a mostrar: ")
    if nif in clientes:
        cliente = clientes[nif]
        print("\n--- Datos del Cliente ---")
        print(f"NIF: {nif}")
        print(f"Nombre: {cliente['name']}")
        print(f"Dirección: {cliente['address']}")
        print(f"Teléfono: {cliente['phone']}")
        print(f"Email: {cliente['email']}")
        print(f"VIP: {'Sí' if cliente['Vip'] else 'No'}\n")
    else:
        print("Cliente no encontrado.")

def listar_clientes():
    if clientes:
        print("\n--- Listado de Clientes ---")
        for nif, datos in clientes.items():
            print(f"NIF: {nif}")
            print(f"Nombre: {datos['name']}")
            print(f"Dirección: {datos['address']}")
            print(f"Teléfono: {datos['phone']}")
            print(f"Email: {datos['email']}")
            print(f"VIP: {'Sí' if datos['Vip'] else 'No'}\n")
    else:
        print("No hay clientes registrados.")

def listar_clientes_vip():
    vip_clientes = {nif: datos for nif, datos in clientes.items() if datos["Vip"]}
    if vip_clientes:
        print("\n--- Listado de Clientes VIP ---")
        for nif, datos in vip_clientes.items():
            print(f"NIF: {nif}")
            print(f"Nombre: {datos['name']}")
            print(f"Dirección: {datos['address']}")
            print(f"Teléfono: {datos['phone']}")
            print(f"Email: {datos['email']}")
            print(f"VIP: {'Sí' if datos['Vip'] else 'No'}\n")
    else:
        print("No hay clientes VIP.")

def accion(opcion):
    if opcion == 1:
        añadir_cliente()
    elif opcion == 2:
        borrar_cliente()
    elif opcion == 3:
        mostrar_cliente()
    elif opcion == 4:
        listar_clientes()
    elif opcion == 5:
        listar_clientes_vip()
    elif opcion == 6:
        print("Saliendo del programa...")
        return False
    else:
        print("Opción no válida, intenta de nuevo.")
    return True

def main():
    while True:
        try:
            opcion = int(input("\nElige una opción: 1|Añadir cliente, 2|Borrar cliente, 3|Mostrar clientes, 4|Listar clientes, 5|Listar clientes VIP, 6|Terminar\n"))
            if not accion(opcion):
                break
        except ValueError:
            print("Error: Ingresa un número válido.")

main()
