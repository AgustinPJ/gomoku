from tablero import Tablero
from validacion import validador
class Juego:
    def __init__(self,dimension:int): # inicia el juego
        self.tablero =  Tablero(dimension)
        self.validador = validador()
        self.turno = "A"
        self.turnos_jugados = 0
        self.estado = "jugando"
    def jugada(self,fila:int,columna:int): # evalua si la jugada es valida y el estado de la partida
        if self.estado!= "jugando":
            return (False,"la partida ya finalizo")
        if self.tablero.colocar_ficha(fila,columna,self.turno):
            self.turnos_jugados += 1
            if self.validador.validar_ganador(self.tablero,fila,columna,self.turno):
                self.estado =f"ganador {self.turno}"
                return (True,self.estado)
            if self.validador.empate(self.tablero,self.turnos_jugados):
                self.estado = "hay empate"
                return (True,self.estado)
            if self.turno == "A":
                self.turno = "B"
            else:
                self.turno = "A"
            return (True,"jugada valida")
        
        else:
            return (False,"jugada invalida")