import random


class FirstLevel:
    number = 0
    player_health = 10
    enemy_health = 10

    def __init__(self):
        self.__gen_number()
        self.player_health = 5
        self.enemy_health = 5

    def __gen_number(self):
        self.number = random.randint(1, 100)

    def __get_player_number(self):
        inpt = input('Make try: ')
        try:
            return  abs(int(inpt))
        except:
            print('Set numbers Only')
            return self.__get_player_number()

    def __get_enemy_number(self):
        return random.randint(1, 100)

    def __process_numbers(self, player_number, enemy_number):
        player_res = abs(player_number - self.number)
        ai_res = abs(enemy_number - self.number)
        if player_res == 0:
            self.enemy_health = 0
        elif ai_res == 0:
            self.player_health = 0
        elif player_res > ai_res:
            self.player_health -= 1
        else:
            self.enemy_health -= 1

    def play(self):
        while self.player_health > 0 and self.enemy_health > 0:
            player_guess = self.__get_player_number()
            enemy_guess = self.__get_enemy_number()
            self.__process_numbers(player_guess, enemy_guess)
            print('You: {}\nEnemy: {}'.format(self.player_health, self.enemy_health))

        if self.player_health <= 0:
            print('You loose!')
        else:
            print('You won')

        print('{:-^10}'.format(self.number))
