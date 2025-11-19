from Figurasgeometricas import Figurasgeometricas

class Circulo(Figurasgeometricas):
    def __init__(self,radio):
        self.radio=radio
    def area(self):
      return self.radio * self.radio * 3.1416


