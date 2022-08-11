import datetime

from app import app
from flask import jsonify, session, request

from board import Result


@app.get('/api/v1/board')
def api_get_board():
    board = app.boards.get(session.get('board_key'))
    board_arr = list(map(lambda x: list(map(lambda y: [str(y).strip(), y.color], x)), board.board))
    return jsonify({'requested': datetime.datetime.now().isoformat()},
                   {'board': board_arr})


@app.post('/api/v1/move')
def api_post_move():
    key = session.get('board_key')
    board = app.boards.get(key)
    move = app.moves.get(key)

    move.define_move(request.json['move'])
    result = board.move_piece(move, app.WTM.get(key))

    if result == Result.OK:
        app.WTM[key] = not app.WTM[key]
    return jsonify({'requested': datetime.datetime.now().isoformat()},
                   {'result': result})
