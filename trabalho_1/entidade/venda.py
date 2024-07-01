import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.bebida import Bebida
from trabalho_1.entidade.refeicao import Refeicao
from trabalho_1.entidade.funcionario import Funcionario
from trabalho_1.entidade.cliente import Cliente

class Venda:
    def __init__(self, cliente: Cliente, funcionario: Funcionario, refeicao: Refeicao, bebida: Bebida):
        self.__codigo = 0
        self.__aberta = True
        self.__valor = 0.0
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
    def aberta(self):
        return self.__aberta

    @property
    def valor(self):
        return self.__valor

    @property
    def cliente(self):
        return self.__cliente

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def refeicoes(self):
        return [refeicao.nome for refeicao in self.__refeicoes]

    @property
    def bebidas(self):
        return [bebida.nome for bebida in self.__bebidas]

    @codigo.setter
    def codigo(self, cod):
        self.__codigo = cod

    @aberta.setter
    def aberta(self, ab):
        self.__aberta = ab

    @valor.setter
    def valor(self, val):
        self.__valor = val

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

    def clear_ref_beb(self):
        self.__refeicoes.clear()
        self.__bebidas.clear()