#Objetivo: Trabalhar POO com o exemplo de uma conta de banco.
#Essa conta possuirá saldo, número, titular e um limite.
#Representá-las no Console será nosso objetivo.

#Criaremos a classe mãe(a conta)
class Conta:
    #definindo os atributos que serão utilizados
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Metódo para mostrar o extrato do titular
    def extrato(self):
        #printar o valor de saldo disponível e o titular em questão
        print('Saldo de {} reais do titular {}'.format(self.__saldo, self.__titular))

    #Método responsável por realizar o depósito de um valor para a conta que está sendo manipulada.
    def deposita(self, valor):
        #Para realizar depósito, pegaremos o saldo atual da conta e adicionaremos o valor a ser depositado.
        self.__saldo += valor

    #Metódo responsável por verificar se o saque será menor que o valor disponível a ser sacado.
    def __pode_sacar(self, valor_a_sacar):
        #criaremos uma variável para guardar o valor do saldo + limite da conta.
        valor_disponivel_a_sacar = self.saldo + self.limite
        #Se o valor a sacar for menor que o valor disponível, o método será válido
        return valor_a_sacar <= valor_disponivel_a_sacar

    #Método feito para realizar o saque de um valor x da conta.
    def saque(self, valor):
        #Estrutura condicional do método anterior. verifica se o valor do saque é menor ou igual ao valor disponível para saque (saldo + limite), usando o método __pode_sacar da própria classe. 
        #Perceba que utilizamos o self para chamar os atributos do método __pode_sacar, que está diretamente ligada a classe Conta.
        if self.__pode_sacar(valor):
        #Se o valor for menor ou maior que o disponível no saldo, realizaremos a subtração do saldo.
            self.__saldo -= valor
        #Caso o método __pode_sacar retorne falso(caso seja maior que o limite), retornará que o valor ultrapassou o limite.
        else:
            print('O valor {} ultrapassou o limite.'.format(valor))

    #Método criado para realizar o depósito do valor de alguma conta origem para uma conta destino.
    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    #Propertys criadas para obter acesso e manipulação dos atributos originalmente privados
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

#Aqui eu utilizei o decorador setter para alterar o limite caso o titular consiga um aumento de limite.
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

#Método estático para ser usado em diferentes do código, sem ter que criar uma instância na classe.
#É usado pois não depende de nenhum dos atributos da classe, embora esteja dentro dela.
#Resumindo, é como se fosse uma função independente, que pode ser acessada diretamente.
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    
#Testando o código

conta_joao = Conta(14, 'João Toucci', 150, 500)
conta_klismann = Conta(14, 'Klismann de Olveira', 300, 1000)

conta_joao.extrato()
conta_joao.deposita(150)
conta_joao.extrato()
conta_joao.saque(100)
conta_joao.extrato()

conta_klismann.extrato()
conta_joao.transfere(50,conta_klismann)
conta_joao.extrato()
conta_klismann.extrato()

#Testando decoradores
conta_joao.limite = 1000
#Ultrapassando o valor propositalmente
conta_joao.saque(1151)

codigos = Conta.codigos_bancos()
codigos