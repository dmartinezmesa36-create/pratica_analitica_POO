from Figurasgeometricas import Figurasgeometricas 
class Cubo(Figurasgeometricas):
    
    
    def __init__(self, nombre):
        super().__init__(nombre)
    @property
    def lado(self)-> float:
        return self._lado
    @lado.setter
    def lado(self,lado:float):
        self._lado=lado

    def area(self):
        return (self.lado**2)*6