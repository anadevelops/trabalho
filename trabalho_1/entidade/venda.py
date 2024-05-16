from bebida import Bebida
from refeicao import Refeicao
from trabalho_1.entidade.funcionario import Funcionario
from cliente import Cliente

class Venda:
    def __init__(self, codigo: int, cliente: Cliente, funcionario: Funcionario, refeicao: Refeicao, bebida: Bebida):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__funcionario = funcionario
        self.__refeicoes = []
        self.__bebidas = []

        if isinstance(refeicao, Refeicao):
            self.__refeicoes.append(refeicao)

        if isinstance(bebida, Bebida):
            self.__bebidas.append(bebida)
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def refeicoes(self):
        return [refeicao for refeicao in self.__refeicoes]

    @property
    def bebidas(self):
        return [bebida for bebida in self.__bebidas]

    @codigo.setter
    def codigo(self, cod):
        self.__codigo = cod

    @cliente.setter
    def cliente(self, cli):
        if isinstance(cli, Cliente):
            self.__cliente = cli

    @funcionario.setter
    def funcionario(self, func):
        if isinstance(func, Funcionario):
            self.__funcionario = func

    @refeicoes.setter
    def refeicoes(self, ref):
        if isinstance(ref, Refeicao):
            self.__refeicoes.append(ref)

    @bebidas.setter
    def bebidas(self, beb):
        if isinstance(beb, Bebida):
            self.__bebidas.append(beb)