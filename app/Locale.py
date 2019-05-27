import json


class Locale:
    locale = ''
    data = ''
    file_path = './app/assets/langs/{}/data.json'

    @staticmethod
    def __(key):
        return Locale.data[key]

    @staticmethod
    def set_locale(locale):
        Locale.locale = locale
        file = open(Locale.file_path.format(Locale.locale))
        Locale.data = json.load(file)
