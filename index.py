from app.config.app import app
from app.Player import Player
from app.Locale import Locale


def mutate_input(text):
    return text.lower()


locale = input(''' Select you language by typing the word.
If you don\'t want to select locale we will use English by default.
english
украинська
русский
Type here: ''')

locale = mutate_input(locale)

app['locale'] = app['locale_matching'][locale]

Locale.set_locale(app['locale'])

name = input(Locale.__('Please input your name: '))

description = input(Locale.__('Describe yourself: '))

player = Player(name, description)
player.say_hi()