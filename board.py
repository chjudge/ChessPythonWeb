from colorama import Fore, Style

from empty import Empty
from pawn import Pawn
from knight import Knight
from rook import Rook
from bishop import Bishop
from queen import Queen
from king import King
from move import Move


class Board:
    def __init__(self):
        self.white_pieces = []
        self.black_pieces = []
        self.board = []
        self.create_board()
        self.empty = Empty(-1, -1, "n/a")
        self.en_passant = []
        self.past_piece = None
        self.old_move = Move()

    def create_board(self):
        self.board = [[Empty(-1, -1, "n/a") for col in range(8)] for row in range(8)]

        self.white_pieces.append(Rook(7, 0, "white"))
        self.white_pieces.append(Knight(7, 1, "white"))
        self.white_pieces.append(Bishop(7, 2, "white"))
        self.white_pieces.append(Queen(7, 3, "white"))
        self.white_pieces.append(King(7, 4, "white"))
        self.white_pieces.append(Bishop(7, 5, "white"))
        self.white_pieces.append(Knight(7, 6, "white"))
        self.white_pieces.append(Rook(7, 7, "white"))
        for i in range(8):
            self.white_pieces.append(Pawn(6, i, "white"))

        for p in self.white_pieces:
            self.board[p.row][p.col] = p

        self.black_pieces.append(Rook(0, 0, "black"))
        self.black_pieces.append(Knight(0, 1, "black"))
        self.black_pieces.append(Bishop(0, 2, "black"))
        self.black_pieces.append(Queen(0, 3, "black"))
        self.black_pieces.append(King(0, 4, "black"))
        self.black_pieces.append(Bishop(0, 5, "black"))
        self.black_pieces.append(Knight(0, 6, "black"))
        self.black_pieces.append(Rook(0, 7, "black"))
        for i in range(8):
            self.black_pieces.append(Pawn(1, i, "black"))

        for p in self.black_pieces:
            self.board[p.row][p.col] = p

    # returns the piece at a specific location 
    def get_piece(self, row, col):
        return self.board[row][col]

    # determine if the player's king is in check
    def in_check(self, white_turn):
        king = self.white_pieces[4] if white_turn else self.black_pieces[4]

        return king.king_check(king.row, king.col, self)

    # moves a piece to the end location and sets the old square empty
    def move_piece(self, move, white_turn):
        if len(self.en_passant) != 0:
            if self.board[move.start_row][move.start_col].color == "white":
                self.board[move.end_row + 1][move.end_col] = self.empty
            else:
                self.board[move.end_row - 1][move.end_col] = self.empty
        self.board[move.start_row][move.start_col].piece_move(move.end_row, move.end_col)
        self.board[move.end_row][move.end_col] = self.board[move.start_row][move.start_col]
        self.board[move.start_row][move.start_col] = self.empty

        if self.in_check(white_turn):
            self.undo()
            return False

        if len(self.en_passant) != 0:
            if (white_turn and self.en_passant[0].color == "white")\
                    or (not white_turn and self.en_passant[0].color == "black"):
                self.en_passant.clear()
        return True

    # when castling is happening
    def castle(self, castle_loc):
        if castle_loc == "white king's side":
            self.board[7][5] = self.board[7][7]
            self.board[7][7] = self.empty
        elif castle_loc == "white queen's side":
            self.board[7][3] = self.board[7][0]
            self.board[7][0] = self.empty
        elif castle_loc == "black king's side":
            self.board[0][5] = self.board[0][7]
            self.board[0][7] = self.empty
        elif castle_loc == "black queen's side":
            self.board[0][3] = self.board[0][0]
            self.board[0][0] = self.empty

    # sets pieces and squares in case undo is needed
    def set_undo(self, move):
        self.old_move.define_move(move.start_row, move.start_col, move.end_row, move.end_col)
        self.past_piece = self.board[move.end_row][move.end_col]

    # if a move wasn't legal (leaving the king in check) then
    def undo(self):
        if len(self.en_passant) != 0:
            if self.past_piece.color == "white":
                self.board[self.old_move.end_row + 1][self.old_move.end_col] = self.past_piece
            else:
                self.board[self.old_move.end_row - 1][self.old_move.end_col] = self.past_piece
            print("undo")
        else:
            self.board[self.old_move.start_row][self.old_move.start_col] = self.board[self.old_move.end_row][
                self.old_move.end_col]
            self.board[self.old_move.end_row][self.old_move.end_col] = self.past_piece
            # if(castle == "white king's side"):
            #     self.board[7][7] = self.board[7][5]
            #     self.board[7][5] = self.empty
            # elif(castle == "white queen's side"):
            #     self.board[7][0] = self.board[7][3]
            #     self.board[7][3] = self.empty
            # elif(castle == "black king's side"):
            #     self.board[0][7] = self.board[0][5]
            #     self.board[0][5] = self.empty
            # elif(castle == "black queen's side"):
            #     self.board[0][0] = self.board[0][3]
            #     self.board[0][3] = self.empty

    def __str__(self):
        print_string = "Chess Board: \n"
        # gets the row in board
        for rowArr in self.board:
            for pieceIndex in range(8):
                # sets the color for the pieces
                if rowArr[pieceIndex].color == "black":
                    print_string += Fore.RED
                elif rowArr[pieceIndex].color == "white":
                    print_string += Fore.BLUE
                print_string += f"{str(rowArr[pieceIndex])}"
                print_string += Style.RESET_ALL
                if pieceIndex != 7:
                    print_string += "|"
            if self.board[7] != rowArr:
                print_string += "\n___ ___ ___ ___ ___ ___ ___ ___\n"
        return print_string
