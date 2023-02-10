# Abstração
from pathlib import Path 

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método Log')

    def logError(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):
    '''
        O Mixin é convenção do Python para 
        avisar aos desenvolvedores que nesta classe 
        você precisa adicionar funcionalidades na sua
        herança multípla
    '''

    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__ })'
        with open(LOG_FILE, 'a') as arquivo:
            print('Salvando no Log: ', msg_formatada)
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__ })')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.logError('Qualquer coisa')
    lp.log_sucess('Sucesso')
    lf = LogFileMixin()
    lf.logError('Qualquer coisa')
    lf.log_sucess('Sucesso')
