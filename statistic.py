import pandas
import pickle

p1 = pickle.load(open('medium_test_player_1.txt', 'rb'))
p2 = pickle.load(open('medium_test_player_2.txt', 'rb'))

games = p1.wins + p2.wins


print('{p1_wins}/{p2_wins}'.format(p1_wins= round((100 * p1.wins)/ games), p2_wins=round((100 * p2.wins)/ games)))

