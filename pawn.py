from piece import Piece as p
from empty import Empty

class Pawn(p):
    # Constuctor defined in parents
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.en_passant = 0 # 1 - take left, 2 - take right (objective view)

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        endR = move.end_row
        endC = move.end_col
        color = self.color

        # up-2, up1, take diagnol, en passant, false
        if(
            isinstance(board.getPiece(endR, endC), Empty) and
            self.hasMoved == False and 
            self.col == endC and
            ((color == "white" and endR == 4) or (color == "black" and endR == 3))
        ):
            self.enPassant(endR,endC,board)
            return True
        elif(
                isinstance(board.getPiece(endR, endC), Empty) and
                self.col == endC and
                (color == "white" and endR == self.row - 1) or
                (color == "black" and endR == self.row + 1)):
            return True
        elif(
                board.getPiece(endR, endC).color != "n/a" and
                board.getPiece(endR, endC).color != color and
                (self.col + 1 == endC or self.col - 1 == endC) and
                ((color == "white" and endR == self.row - 1) or
                 (color == "black" and endR == self.row + 1))
        ):
            return True
        elif (
            (self.en_passant == 1 and endC == self.col - 1) or
            (self.en_passant == 2 and endC == self.col + 1) and
            ((color == "white" and endR == self.row - 1) or (color == "black" and endR == self.row + 1))
        ): 
            return True
        return False

    # checks and activates opponents pawn en passant if possible
    def enPassant(self, end_r, end_c, board):
        edge_right = 1
        edge_left = 1
        if(end_c == 7):
            edge_right = 0
        if(end_c == 0):
            edge_left = 0
        if(isinstance(board.getPiece(end_r,end_c + 1 * edge_right),Pawn) and 
            isinstance(board.getPiece(end_r,end_c - 1 * edge_left),Pawn) and 
            board.getPiece(end_r,end_c + 1 * edge_right).color != self.color and
            board.getPiece(end_r,end_c - 1 * edge_right).color != self.color):
            board.getPiece(end_r,end_c + 1 * edge_right).en_passant = 1
            board.getPiece(end_r,end_c - 1 * edge_right).en_passant = 2
            board.en_passant.append(board.getPiece(end_r,end_c + 1 * edge_right))
            board.en_passant.append(board.getPiece(end_r,end_c - 1 * edge_right))
        elif(isinstance(board.getPiece(end_r,end_c + 1 * edge_right),Pawn) and
            board.getPiece(end_r,end_c + 1 * edge_right).color != self.color):
            board.getPiece(end_r,end_c + 1 * edge_right).en_passant = 1
            board.en_passant.append(board.getPiece(end_r,end_c + 1 * edge_right))
        elif(isinstance(board.getPiece(end_r,end_c - 1 * edge_right),Pawn) and 
            board.getPiece(end_r,end_c - 1 * edge_right).color != self.color):
            board.getPiece(end_r,end_c - 1 * edge_right).en_passant = 2
            board.en_passant.append(board.getPiece(end_r,end_c - 1 * edge_right))

    def __str__(self):
        return " P "