import random


class SecondLevel:
    number = 0
    player_health = 10
    enemy_health = 10
    enemy_last_health = 10
    enemy_numbers = []
    enemy_last_number = 0

    def __init__(self):
        self.__gen_number()
        self.player_health = 100
        self.enemy_health = 100
        self.enemy_last_health = 100
        self.enemy_last_number = 0
        self.enemy_numbers = {'win': [], 'lose': []}

    def __gen_number(self):
        self.number = random.randint(1, 100)

    def __get_player_number(self):
        inpt = input('Make try: ')
        try:
            return abs(int(inpt))
        except:
            print('Set numbers Only')
            return self.__get_player_number()

    def __get_enemy_number(self):
        if self.enemy_last_number != 0:
            if self.enemy_last_health > self.enemy_health:
                self.enemy_numbers['lose'].append(self.enemy_last_number)
            else:
                self.enemy_numbers['win'].append(self.enemy_last_number)

        if len(self.enemy_numbers['win']) == 0 or len(self.enemy_numbers['lose']) == 0:
            guess = random.randint(1, 100)
        else:
            guess = random.randint(1, 100)
        self.enemy_last_number = guess
        self.enemy_last_health = self.enemy_health
        return guess

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
            player_guess = random.randint(1, 100)
            enemy_guess = self.__get_enemy_number()
            self.__process_numbers(player_guess, enemy_guess)
            print('You: {}\nEnemy: {}'.format(self.player_health, self.enemy_health))

        if self.player_health <= 0:
            print('You loose!')
        else:
            print('You won')
        f = open('./test.txt', 'a+')
        # f.write('{:-^10}\n{win} | {lose}\nwin middle: {WM}\nlose middle: {LM}\n'.format(self.number,
        #                                                                                  win=self.enemy_numbers['win'],
        #                                                                                  lose=self.enemy_numbers['lose'],
        #                                                                                  WM=round(sum(self.enemy_numbers['win']) / (len(self.enemy_numbers['win']) +1)),
        #                                                                                  LM=round(sum(self.enemy_numbers['lose']) / (len(self.enemy_numbers['lose']) +1))
        #                                                                                 )
        #         )
        f.write('p1: [{p1_wins}, {p1_loses}]\np2: [{p2_wins}, {p2_loses}]'.format())
        f.close()
        #print(self.enemy_numbers)
        #print('{:-^10}'.format(self.number))
