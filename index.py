import pickle
import json
from pprint import pprint
from app.Game import Game

for i in range(1, 2000):
    game = Game()
    game.start()
