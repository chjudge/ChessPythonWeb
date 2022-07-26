# this is needed because the board is printed with 0 at the top not 7
def invert_row_nums(row_val):
    return abs(row_val - 7)


class Move:
    def __init__(self):
        self.start_row = None
        self.start_col = None
        self.end_row = None
        self.end_col = None

    # Setter Method
    # moveNotation is a string that will be converted into the move variables
    # Chess move notation is as follows: [pieceLocation]-[pieceDestination] ex.) b1-a3 *knight move
    def set_move(self, move_notation):
        if not (len(move_notation) == 5 and (move_notation[0] and move_notation[3]) in "abcdefgh"
                and (move_notation[1] and move_notation[4]) in "12345678"):
            return False
        self.start_col = "abcdefgh".index(move_notation[0])
        self.start_row = invert_row_nums(int(move_notation[1]) - 1)
        self.end_col = "abcdefgh".index(move_notation[3])
        self.end_row = invert_row_nums(int(move_notation[4]) - 1)

    # this is used when the program needs to define a move object
    def define_move(self, rs, cs, re, ce):
        self.start_row = rs
        self.start_col = cs
        self.end_row = re
        self.end_col = ce    
