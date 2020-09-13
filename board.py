class board(object):
    Tablero = None

    def __init__(self):
        """
        Iniciador de un objeto de clase board.
        """
        #Tablero de 8x8
        self.Tablero = [[0]*8 for i in range(8)]

    def pieceposition(self, x , y):
        self.Tablero[x][y] = 8

    def pieceMovement(self,lista):
        pass

    def __repr__(self):
        return self.Tablero.__str__()
    

