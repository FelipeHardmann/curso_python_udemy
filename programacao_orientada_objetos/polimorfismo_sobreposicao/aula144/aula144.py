# Polimorfismo 
# é a sobreposição de métodos nas classes filhas 
# Utiliza métodos com o mesmo nome da classe pai
# para sobrescrever os métodos antigos
# Ou seja, cada método tem sua função dependendo da classe
# Precisa ter a mesma quantidade de parâmetros
# Princípio de substituição de Liskov

# override -> Python suporta(Sobreposição de métodos)
# Já a sobrecarga o Python não suporta -> overload

from abc import ABC, abstractmethod

class Notifcacion(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool:
        ...


class NotficacionForEmail(Notifcacion):
    # A assinatura do método precisa ser igual
    def enviar(self) -> bool:
        print(f'Email: Enviando... {self.msg}')
        return True


class NotficacionForSms(Notifcacion):
    def enviar(self) -> bool:
        print(f'SMS: Enviando... {self.msg}')
        return True


def notificar(notificacao: Notifcacion):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação Enviada')
    else:
        print('Notificação NÃO Enviada')


notificacao_email = NotficacionForEmail('Testando Email')
notificar(notificacao_email)

notificacao_sms = NotficacionForSms('Testando SMS')
notificar(notificacao_sms)