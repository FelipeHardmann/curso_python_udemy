# from Log import LogPrintMixin, LogFileMixin
from eletronico import Smartphone

# lp = LogPrintMixin()
# lp.logError('Qualquer coisa')
# lp.log_sucess('Sucesso')
# lf = LogFileMixin()
# lf.logError('Qualquer coisa')
# lf.log_sucess('Sucesso')


galaxy = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

# galaxy.ligar()
galaxy.desligar()
# iphone.ligar()
iphone.desligar()