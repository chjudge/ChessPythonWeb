from board import Board
from move import Move
from pieces.empty import Empty
from pieces.rook import Rook
from pieces.king import King
from pieces.pawn import Pawn


def test_pawn_move():
    board = Board()
    move = Move()
    move.define_move(1, 2, 2, 2)
    board.move_piece(move, True)
    move.define_move(6, 2, 5, 2)
    board.move_piece(move, False)
    print(board)
    assert isinstance(board.get_piece(1, 2), Empty)
    assert isinstance(board.get_piece(2, 2), Pawn)
    assert board.get_piece(2, 2).color == "black"
    assert isinstance(board.get_piece(6, 2), Empty)
    assert isinstance(board.get_piece(5, 2), Pawn)
    assert board.get_piece(5, 2).color == "white"


def test_white_move_en_passant():
    pass
    board = Board()
    move = Move()
    move.define_move(6, 2, 4, 2)
    board.move_piece(move, True)
    move.define_move(4, 2, 3, 2)
    board.move_piece(move, True)
    move.define_move(1, 1, 3, 1)
    board.move_piece(move, False)
    move.define_move(3, 2, 2, 1)
    board.move_piece(move, True)
    print(board)
    assert isinstance(board.get_piece(3, 1), Empty)
    assert isinstance(board.get_piece(2, 1), Pawn)
    assert board.get_piece(2, 1).color == "white"


def test_king_side_castle():
    board = Board()
    move = Move()
    # king pawn
    move.define_move(6, 4, 4, 4)
    board.move_piece(move, True)
    # bishop
    move.define_move(7, 5, 6, 4)
    board.move_piece(move, True)
    # knight
    move.define_move(7, 6, 5, 7)
    board.move_piece(move, True)
    # king
    move.define_move(7, 4, 7, 6)
    board.move_piece(move, True)
    print(board)
    assert isinstance(board.get_piece(7, 5), Rook)
    assert isinstance(board.get_piece(7, 6), King)
    assert board.get_piece(7, 5).color == "white"


def test_queen_side_castle():
    board = Board()
    move = Move()
    # queen pawn
    move.define_move(6, 3, 4, 3)
    board.move_piece(move, True)
    # bishop
    move.define_move(7, 2, 5, 4)
    board.move_piece(move, True)
    # queen
    move.define_move(7, 3, 6, 3)
    board.move_piece(move, True)
    # knight
    move.define_move(7, 1, 5, 0)
    board.move_piece(move, True)
    # king
    move.define_move(7, 4, 7, 2)
    board.move_piece(move, True)
    print(board)
    assert isinstance(board.get_piece(7, 3), Rook)
    assert isinstance(board.get_piece(7, 2), King)
    assert board.get_piece(7, 5).color == "white"
