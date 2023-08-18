#5
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        edad_str = f"Edad: {self.edad}" if self.edad is not None else ""
        notas_str = ', '.join(map(str, self.notas)) or "Ninguna"
        
        print(f"Información del estudiante:\nNombre: {self.nombre}\nNúmero de registro: {self.numero_registro}\n{edad_str}\nNotas: {notas_str}")

    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, *notas):
        self.notas.extend(notas)

nombre_alumno = input("Ingrese el nombre del alumno: ")
numero_registro_alumno = input("Ingrese el número de registro del alumno: ")
alumno = Alumno(nombre_alumno, numero_registro_alumno)

alumno.setAge(int(input("Ingrese la edad del alumno: ")))

num_notas = int(input("Ingrese la cantidad de notas del alumno: "))
alumno.setNota(*(float(input(f"Ingrese la nota {i+1} del alumno: ")) for i in range(num_notas)))

alumno.display()


