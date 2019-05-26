from app.Locale import Locale

class Player:
    name = ''
    description = ''

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def say_hi(self):
        print(self.name + Locale.__(' said Hi!'))