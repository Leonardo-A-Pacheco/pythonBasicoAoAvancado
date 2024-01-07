# abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):         #assinatura do metodo
        raise NotImplementedError(
            'implemente o metodo log'
        )
   
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')
    
class LogFileMixin(Log):
      def _log(self, msg):
            msg_formatada = f'{msg} ({self.__class__.__name__})'
            print('Selvando Log:', msg_formatada)
            with open(LOG_FILE, 'a') as arquivo:
                 arquivo.write(msg_formatada)
                 arquivo.write('\n')
            print(msg)

class LogPrintMixin(Log):    
      def _log(self, msg):
           print(f'{msg} ({self.__class__.__name__}) ')



if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('DEU MERDA') 
    lp.log_sucess('DEU OURO') 
    lf = LogFileMixin()
    lf.log_error('DEU MERDA') 
    lf.log_sucess('DEU OURO') 
    print(LOG_FILE)


