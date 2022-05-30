class Move():
    def __init__(self):
        self.start_row = None
        self.start_col = None
        self.end_row = None
        self.end_col = None

    # Setter Method
    # moveNotation is a string that will be converted into a the move variables 
    # Chess move notation is as follows: [pieceLocation]-[pieceDestination] ex.) b1-a3 *knight move
    def setMove(self, moveNotation):
        if not (len(moveNotation) == 5 and (moveNotation[0] and moveNotation[3]) in "abcdefgh"
                and (moveNotation[1] and moveNotation[4]) in "12345678"):
            return False
        self.start_col = "abcdefgh".index(moveNotation[0])
        self.start_row = self.invertRowNums((int)(moveNotation[1]) - 1)
        self.end_col = "abcdefgh".index(moveNotation[3])
        self.end_row = self.invertRowNums((int)(moveNotation[4]) - 1)

    # this is needed because the board is printed with 0 at the top not 7
    def invertRowNums(self, rowVal):
        return abs(rowVal - 7)



