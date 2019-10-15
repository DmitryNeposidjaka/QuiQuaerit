import random
import pickle
from app.Player import Player
from app.PlayerMedium import PlayerMedium


class ThirdLevel:
    number = 0
    player1 = {}
    player2 = {}

    def __init__(self):
        self.__gen_number()

        self.player1 = self.__get_player('medium_test_player_1.txt', True)
        self.player2 = self.__get_player('medium_test_player_2.txt')

    def __gen_number(self):
        self.number = random.randint(1, 100)

    def __get_player(self, filename, medium=False):
        try:
            with open(filename, 'rb') as p_f:
                player = pickle.load(p_f)
                player.set_health(10)
        except Exception:
            if medium:
                player = PlayerMedium(health=10, max_r=10, min_r=1)
            else:
                player = Player(health=10)
        return player

    def __process_numbers(self, player_number, enemy_number):
        player_res = abs(player_number - self.number)
        ai_res = abs(enemy_number - self.number)
        if player_res == 0:
            self.player1.bit(player_res)
            self.player2.success(ai_res)
            self.player2.health = 0
        elif ai_res == 0:
            self.player2.bit(ai_res)
            self.player1.success(player_res)
            self.player1.health = 0
        elif player_res > ai_res:
            self.player1.bit(player_res)
            self.player2.success(ai_res)
        else:
            self.player2.bit(ai_res)
            self.player1.success(player_res)

    def play(self):
        while self.player1.health > 0 and self.player2.health > 0:
            player_guess = self.player1.make_guess()
            enemy_guess = self.player2.make_guess()
            self.__process_numbers(player_guess, enemy_guess)
        #    print('You: {}\nEnemy: {}'.format(self.player1.health, self.player2.health))

        if self.player1.health <= 0:
            self.player1.win()
            self.player2.loose()
            self._store_players()
        else:
            self.player2.win()
            self.player1.loose()
            self._store_players()
        # f = open('./test.txt', 'a+')
        # f.write('{:-^10}\n{win} | {lose}\nwin middle: {WM}\nlose middle: {LM}\n'.format(self.number,
        #                                                                                  win=self.enemy_numbers['win'],
        #                                                                                  lose=self.enemy_numbers['lose'],
        #                                                                                  WM=round(sum(self.enemy_numbers['win']) / (len(self.enemy_numbers['win']) +1)),
        #                                                                                  LM=round(sum(self.enemy_numbers['lose']) / (len(self.enemy_numbers['lose']) +1))
        #                                                                                 )
        #         )
        # f.write('p1: [{p1_wins}, {p1_loses}]\np2: [{p2_wins}, {p2_loses}]'.format())
        # f.close()
        # print(self.enemy_numbers)
        # print('{:-^10}'.format(self.number))

    def _store_players(self):
        with open('medium_test_player_1.txt', 'wb') as p1_f:
            pickle.dump(self.player1, p1_f)
        with open('medium_test_player_2.txt', 'wb') as p2_f:
            pickle.dump(self.player2, p2_f)
