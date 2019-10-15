import datetime


class Logger:
    session_name = ''
    # TODO relative path
    logs_path = './app/storage/logs/{}.log'
    file = ''

    def __init__(self, name=''):
        self.session_name = '{}_{}'.format(name, datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S'))
        self._create_log_file()

    def _create_log_file(self):
        self.file = open(self.logs_path.format(self.session_name), 'w+')

    @staticmethod
    def add(text):
        if hasattr(Logger.file, 'write'):
            Logger.file.write('{}\n'.format(text))
