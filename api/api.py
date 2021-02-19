import time
from flask import Flask
from flask.json import jsonify
import random
from bfs import play_game

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time':time.time()}

@app.route('/solution')
def get_solutions():
    board = random.sample(range(9), 9)
    play_game(board)
    return jsonify(board)


    