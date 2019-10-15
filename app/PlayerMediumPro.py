from app.Player import Player
import random


class PlayerMediumPro(Player):
    tactic = None

    def __init__(self, health=100):
        super().__init__(health)
        self.tactic = self.choose_tactic(100)
        self.right_numbers = []
        self.wrong_numbers = []

    def make_guess(self):
        if len(self.right_numbers) >= 2:
            while True:
                success_avg = round(sum(self.right_numbers) / len(self.right_numbers)) if len(self.right_numbers) else 1
                max_r = success_avg + random.randint(1, 10)
                min_r = success_avg - random.randint(1, 10)
                if min_r <= 0:
                    min_r = 1
                result = random.randint(abs(min_r), abs(max_r))
                if result not in self.wrong_numbers:
                    return result
        else:
            return random.randint(1, 100)

    def choose_tactic(self, range_max):
        if (range_max % 4) == 0:
            return 'quadro_guess'
        elif range_max % 3 == 0:
            return 'triple_guess'
        elif range_max % 2 == 0:
            return 'duo_guess'
        else:
            print('random')
            return 'random_guess'

    def quadro_guess(self, range_max):
        cell = range_max / 4
        return self.randint_in_range(cell, cell // 4, cell // 4)

    def triple_guess(self, range_max):
        cell = range_max / 3
        return self.randint_in_range(cell, cell // 4, cell // 4)

    def duo_guess(self, range_max):
        cell = range_max / 2
        return self.randint_in_range(cell, cell // 4, cell // 4)

    def random_guess(self, range_max):
        return random.randint(1, range_max)

    def randint_in_range(self, integer, max_r, min_r):
        max_int = random.randint(integer, integer + max_r)
        min_int = random.randint(integer - min_r, integer) if integer - min_r > 0 else 1
        if max_int == min_int:
            return integer
        return random.randint(min_int, max_int)
