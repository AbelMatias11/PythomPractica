#4
largo = float(input("Coloque el largo del rectángulo: "))
ancho = float(input("Coloque el ancho del rectángulo: "))

class R:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho
 
rectangulo = R(largo, ancho)
area = rectangulo.calcular_area()
print(f"El largo {largo} y ancho {ancho} Y el area del rectangulo es: {area:.2f}")
