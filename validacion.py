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
    
    def verificar_diagonal_negativa(self,tablero,fila:int,columna:int,turno: str):
        contador = 1
        for i in range(1,5):
            if tablero.esta_en_rango(fila + i,columna + i) and tablero.grilla[fila + i][(columna + i)] == turno:
                contador += 1
                if contador == 5:
                    return True
            else:
                break
        for j in range(1,5):
            if tablero.esta_en_rango(fila - j,columna - j) and tablero.grilla[fila - j][(columna - j)] == turno:
                contador +=1
                if contador == 5:
                    return True
            else:
                break
        return False
    
    def verificar_diagonal_positiva(self,tablero,fila:int,columna:int,turno: str):
        contador = 1
        for i in range(1,5):
            if tablero.esta_en_rango(fila - i,columna + i) and tablero.grilla[fila - i][(columna + i)] == turno:
                contador += 1
                if contador == 5:
                    return True
            else:
                break  
        for j in range(1,5):
            if tablero.esta_en_rango(fila + j,columna - j) and tablero.grilla[fila + j][(columna - j)] == turno:
                contador +=1
                if contador == 5:
                    return True
            else:
                break
        return False