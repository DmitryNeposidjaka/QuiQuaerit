import json
from app.LevelFactory import LevelFactory


class Master:
    level_factory = ''

    def __init__(self):
        self.level_factory = LevelFactory()

    def get_level(self, name):
        file = open('./app/config/levels.json')
        levels = json.load(file)
        return self.level_factory.make(levels[name])



