import sys
sys.path.append(".")

from board import board
from piece import *
import numpy as np

#Main
if __name__ == "__main__":
    boardDictionary = {}
    pieces = [peon(), alfil(), reina(), rey(), torre(), caballo()]
    
    """Para cada pieza generamos un tablero diferente, inicializamos en una pocisión 
        aleatoria del tablero y generamos las posibles pocisiones"""

    for piece in pieces:
            boardDictionary[piece.getTipo()] = board()
            #generamos una pocision incial aleatoria para la ficha
            posicionInicial = piece.setPosition()
            #Generamos la lista con los posibles movimientos para la pieza en cuestion
            posiblesMovimientos = piece.Move()
            #Añadimos la pocision inicial de la ficha al tablero
            boardDictionary[piece.getTipo()].pieceposition(posicionInicial[0],posicionInicial[1])
            #Agregamos al tablero las posibles posiciones para la ficha en cuestion
            for movimiento in posiblesMovimientos:
                try:
                    boardDictionary[piece.getTipo()].pieceMovement(movimiento)
                except:
                    pass
                
            print(piece.getTipo()+"\n")
            print(np.array(boardDictionary[piece.getTipo()].getBoard()))
            print("\n")

        

        

