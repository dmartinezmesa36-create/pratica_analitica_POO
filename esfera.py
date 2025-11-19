from Figurasgeometricas import Figurasgeometricas 
class Esfera(Figurasgeometricas):
    
    
    def __init__(self, nombre):
        super().__init__(nombre)
    @property
    def radio(self)-> float:
        return self._radio
    @radio.setter
    def radio(self,radio:float):
        self._radio=radio
    def area(self):
        return 4 * 3.1416 * (self.radio **2)