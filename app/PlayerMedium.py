from app.Player import Player
import random


class PlayerMedium(Player):
    min_r = 1
    max_r = 10

    def __init__(self, health=100, min_r=1, max_r= 10):
        super().__init__(health)
        self.min_r = min_r
        self.max_r = max_r
        self.right_numbers = []
        self.wrong_numbers = []

    def make_guess(self):
        if len(self.right_numbers) >= 1:
            right = self.randint_in_range(self.right_numbers, 5, 5)
            while True:
                success_avg = round(sum(right) / len(right)) if len(right) else 1
                max_r = success_avg + random.randint(self.min_r, self.max_r)
                min_r = success_avg - random.randint(self.min_r, self.max_r)
                if min_r <= 0:
                    min_r = 1
                result = random.randint(abs(min_r), abs(max_r))

                if result not in self.randint_in_range(self.wrong_numbers, 2, 2):
                    return result
        else:
            return random.randint(1, 100)

    def randint_in_range(self, numbers, max_r, min_r):
        result = []
        for wrong_num in numbers:
            max_int = random.randint(wrong_num, wrong_num + max_r)
            min_int = random.randint(wrong_num - min_r, wrong_num) if wrong_num - min_r > 0 else 1
            if max_int == min_int:
                result += [wrong_num]
            result += range(min_int, max_int)
        return result