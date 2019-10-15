from app.Master import Master
from app.Menu import Menu


class Game:
    player = ''
    status = 'start'
    level = ''
    master = ''

    def __init__(self):
        #Menu.set_locale()
        #self.player = Menu.get_user()
        self.master = Master()
        self.level = self.master.get_level('third')

    def start(self):
        pass
        # print(self.level)

    def restart(self):
        self.player = Menu.get_user()
        print('restarted')
        print(self.level)

    def end(self):
        print('end')
