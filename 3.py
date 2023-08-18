#3
radiodelcirculo = float(input("Coloque el radio del circulo: "))

import math
class C:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2

circulo = C (radiodelcirculo)

area = circulo.calcular_area()
print(f"Radio del circulo {radiodelcirculo} y el area es: {area:.2f}")
