import tablero

class validador:

    def verificar_fila(self, tablero,fila:int,turno:str) :
        contador= 0
        for col in range(tablero.dimension):
            if tablero.grilla[fila][col] == turno:
                contador +=1
                if contador == 5:
                    return True
            else:
                contador = 0
        return False
    def verificar_columna(self,tablero,columna:int,turno:str):
        contador= 0
        for fil in range(tablero.dimension):
            if tablero.grilla[fil][columna] == turno:                        
                contador +=1
                if contador == 5:
                    return True
            else:
                contador = 0
        return False

