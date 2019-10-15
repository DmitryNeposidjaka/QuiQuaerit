from app.Locale import Locale
import names
import random


class Player:
    name = ''
    description = ''
    health = 0
    wins = 0
    looses = 0
    right_numbers = []
    wrong_numbers = []
    archive = []

    def __init__(self, health=100):
        self.name = names.get_full_name()
        self.set_health(health)
        self.wins = 0
        self.looses = 0
        self.right_numbers = []
        self.wrong_numbers = []
        self.archive = []

    def set_health(self, health):
        self.health = health

    def make_guess(self):
        return random.randint(1, 100)

    def win(self):
        self.wins += 1
        self._archive_results()

    def loose(self):
        self.looses += 1
        self._archive_results()

    def bit(self, number):
        self.wrong_numbers.append(number)
        self.health -= 1

    def success(self, number):
        self.right_numbers.append(number)

    def _archive_results(self):
        self.archive.append({
            'right_numbers': self.right_numbers,
            'wrong_numbers': self.right_numbers
        })

        self.right_numbers = []
        self.wrong_numbers = []
