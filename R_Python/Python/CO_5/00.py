class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.mostrar()
    
    def mostrar(self):
        print("hola "+self.nombre)

#main
p=Persona("Pepe", "30")
p.mostrar()