class Conta:

    # construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo o objeto...{self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # métodos
    def extrato(self):
        print(f'O saldo do titular {self.__titular} é de {self.__saldo}.')

    def depositar(self, valor=0):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def sacar(self, valor=0):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} ultrapassou o limite.')

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print(f'Transferência de {valor} realizada com sucesso.')
        print(f'Seu saldo atual é de {self.__saldo}')

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property                   #get_
    def limite(self):
        return self.__limite

    @limite.setter              #set_
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigoBanco():          #método estático (da classe)
        return '001'

    @staticmethod
    def codigosBancos():
        return {'BB': '001', 'Caixa':'104', 'Bradesco':'237'}

