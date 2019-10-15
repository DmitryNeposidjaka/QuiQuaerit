

class LevelFactory:

    def make(self, data):
        mod = __import__("app.levels.{}".format(data['file']), fromlist=[data['file']])
        level = getattr(mod, data['file'])
        level().play()
        return data
