class board(object):
    Tablero = None

    def __init__(self):
        """
        Iniciador de un objeto de clase board.
        """
        #Tablero de 8x8
        self.Tablero = [[0]*8 for i in range(8)]

    def pieceposition(self, x , y):
        """
        Esta función establece una ficha dentro de una pocision dada en el tablero
        """
        self.Tablero[x][y] = 8

    def pieceMovement(self,lista):
        """
        Esta funcion establece los posibles movimientos que una ficha puede tener en el tablero
        """
        if lista[0] < 0 or lista[1] < 0:
            pass
        else:
            self.Tablero[lista[0]][lista[1]] = 1

    def getBoard(self):
        return self.Tablero
    

