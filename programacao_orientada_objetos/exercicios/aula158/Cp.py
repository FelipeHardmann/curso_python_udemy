from Conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhar(f'Saque de {valor}')
            return self.saldo
        return f'Não foi possível sacar o valor desejado\nSeu saldo é de {self.saldo}'
    
