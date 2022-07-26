from piece import Piece as p
import math
from move import Move
from rook import Rook
from empty import Empty


class King(p):
    # Constructor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def can_move(self, move, board):
        endR = move.end_row
        endC = move.end_col
        startR = self.row
        startC = self.col

        # general parameter check
        # uses distance formula to check if the move is legal
        if endR == startR and endC == startC:
            return False

        distance = math.sqrt(math.pow(startR - endR, 2) + math.pow(startC - endC, 2))

        if ((distance == 1 and distance == math.sqrt(2)) and
                board.get_piece(endR, endC).color != self.color):
            return True
        elif (endR == 7 and endC == 6 and not self.hasMoved and
              (self.color == "white" and isinstance(board.get_piece(7, 7), Rook) and
               not board.get_piece(7, 7).hasMoved) and
              isinstance(board.get_piece(7, 6), Empty) and isinstance(board.get_piece(7, 5), Empty) and
              not self.king_check(7, 4, board) and not self.king_check(7, 5, board) and not self.king_check(7, 6, board)):
            board.castle("white king's side")
            return True
        elif (endR == 7 and endC == 2 and not self.hasMoved and
              (self.color == "white" and isinstance(board.get_piece(7, 0), Rook) and
               not board.get_piece(7, 0).hasMoved) and
              isinstance(board.get_piece(7, 1), Empty) and isinstance(board.get_piece(7, 2), Empty) and
              isinstance(board.get_piece(7, 3), Empty) and
              not self.king_check(7, 2, board) and not self.king_check(7, 3, board) and not self.king_check(7, 6, board)):
            board.castle("white queen's side")
            return True
        elif (endR == 0 and endC == 6 and not self.hasMoved and
              (self.color == "white" and isinstance(board.get_piece(0, 7), Rook) and
               not board.get_piece(0, 7).hasMoved) and
              isinstance(board.get_piece(0, 6), Empty) and isinstance(board.get_piece(0, 5), Empty) and
              not self.king_check(0, 4, board) and not self.king_check(0, 5, board) and not self.king_check(0, 6, board)):
            board.castle("black king's side")
            return True
        elif (endR == 0 and endC == 2 and not self.hasMoved and
              (self.color == "white" and isinstance(board.get_piece(0, 0), Rook) and
               not board.get_piece(0, 0).hasMoved) and
              isinstance(board.get_piece(0, 1), Empty) and isinstance(board.get_piece(0, 2), Empty) and
              isinstance(board.get_piece(0, 3), Empty) and
              not self.king_check(0, 2, board) and not self.king_check(0, 3, board) and not self.king_check(0, 6, board)):
            board.castle("black queen's side")
            return True
        return False

    # takes row, col so that it's king_check can be used for castling as well
    def king_check(self, row, col, board):
        move = Move()
        is_in_check = False
        if self.color == "white":
            for piece in board.black_pieces:
                move.define_move(piece.row, piece.col, row, col)
                is_in_check = piece.can_move(move, board)
                if is_in_check:
                    print("-------------------------------")
                    break
        else:
            for piece in board.white_pieces:
                move.define_move(piece.row, piece.col, row, col)
                is_in_check = piece.can_move(move, board)
                if is_in_check:
                    print("-----------------------------------")
                    break
        print(f"is {self.color} king in check: {is_in_check}")
        return is_in_check

    def __str__(self):
        return " K "
