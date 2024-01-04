# abstração

class Log:
    def log(self, msg):         #assinatura do metodo
        raise NotImplementedError(
            'implemente o metodo log'
        )
    
class LogFileMixin(Log):
      def log(self, msg):
            print(msg)
            

if __name__ == '__main__':
    # l = Log()
    l = LogFileMixin()
    l.log('coisa') 



