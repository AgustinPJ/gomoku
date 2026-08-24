
class Tablero:
    def __init__(self,dimension: int)->None:
        self.dimension = dimension #guarda la dimension
        self.grilla = [[None]*self.dimension for _ in range(self.dimension)]# crea la grilla
    