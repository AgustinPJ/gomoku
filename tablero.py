
class Tablero:

    def __init__(self, dimension: int):
        self.dimension = dimension  # guarda la dimension
        self.grilla = [[None] * self.dimension for _ in range(self.dimension)]  # crea la grilla

    def esta_en_rango(self, fila: int, columna: int):  # verifica si la coordenada existe 
        return (0 <= fila < self.dimension) and (0 <= columna < self.dimension)
    
    def esta_vacia(self, fila: int , columna: int):  # verifica si la coordenada esta vacia
           return self.esta_en_rango(fila, columna) and self.grilla[fila][columna] is None
    
    def colocar_ficha(self, fila:int,columna:int,turno:str):  # coloca la ficha en la coordenada si es posible
         if self.esta_vacia(fila, columna):
              self.grilla[fila][columna] = turno
              return True 
         else: 
              return False