#conta
class Conta:

    #construtor da classe
    def __init__ (self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo  #atributo privado dois underline
        self.__limite = limite

    #sobrescrita do método buitin
    def __str__(self):
        return f'{self.__numero:5} {self.__titular:10} R$ {self.__saldo:5} R$ {self.__limite}'


    def deposita(self,valor):
        self.__saldo += valor

    
    def extrato (self):
        print ('------- Extrato ------')
        print (f'Titular: {self.__titular}')
        print (f'Numero da conta: {self.__numero}')
        print (f' limite + saldo: R$ {self.__limite + self.__saldo:.2f}')

      
    #propriedade somente para leitura
    @property
    def saldo (self):
        return self.__saldo

    @property
    def numero (self):
        return self.__numero

    @property
    def titular (self):
        return self.__titular

    @property
    def limite (self):
        return self.__limite


    @limite.setter #setter serve para alterar
    def limite (self, limite):
        self.__limite = limite

    #metodo estatico fica armazenado direto na classe, não vai para o objeto compartilhado com todos do objeto

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
        

   

    



