from app.config.app import app
from app.Player import Player
from app.Locale import Locale
from app.Logger import Logger


class Menu:

    @staticmethod
    def set_locale():
        locale = input(''' Select you language by typing the word.
        If you don\'t want to select locale we will use English by default.
        english
        украинська
        русский
        Type here: ''')

        locale = locale.lower()

        app['locale'] = app['locale_matching'][locale]

        Locale.set_locale(app['locale'])

    @staticmethod
    def get_user():
        name = input(Locale.__('Please input your name: '))

        description = input(Locale.__('Describe yourself: '))

        player = Player(name, description)
        Logger(player.name)
        Logger.add('Player {} has been created.\nAnd He is: {}'.format(player.name, player.description))
        return player
