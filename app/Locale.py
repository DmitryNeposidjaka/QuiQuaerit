import json


class Locale:
    locale = ''
    data = ''

    @staticmethod
    def __( key):
        return Locale.data[key]

    @staticmethod
    def set_locale( locale):
        Locale.locale = locale
        file = open('./app/assets/langs/' + Locale.locale + '/data.json')
        Locale.data = json.load(file)

