import tablero

class validador:

    def verificar_fila(self, tablero,fila:int,turno:str) :
        contador= 0
        for col in tablero.grilla[fila]:
            if col == turno:
                contador +=1
            if contador == 5:
                return True
            else:
                contador = 0
        return False