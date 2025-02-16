#Crea una función llamada clean_list que tome una lista de nombres de usuarios y una lista de nombres de usuarios baneados y 
# devuelva una nueva lista con los usuarios no baneados.
def clean_list(usuarios, baneados):
    noBaneados = usuarios.copy()  # Copiamos la lista original para no modificarla

    for usuario in usuarios:  # Recorremos la lista de usuarios
        if usuario in baneados:  # Si el usuario está en la lista de baneados
            noBaneados.remove(usuario)  # Lo eliminamos

    return noBaneados  # Retornamos la lista sin baneados

def main():
    usuarios = ["Platón", "Aristóteles", "Diógenes", "Anaximandro", "Anaxímenes", "Nietzsche", "Descartes", "Marx", "TomásDeAquino"]
    baneados = ["Nietzsche", "Descartes", "Marx", "Diógenes"]

    res = clean_list(usuarios, baneados)
    print(res)

if __name__ == "__main__":
    main()
