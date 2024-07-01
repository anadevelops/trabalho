import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.pessoa import Pessoa
from trabalho_1.entidade.endereco import Endereco


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: int, salario: float, funcao: str, rua: str, bairro: str, cidade: str):
        super().__init__(nome, cpf)
        self.__salario = salario
        self.__funcao = funcao
        self.__endereco = Endereco(rua, bairro, cidade)
        self.__num_vendas = 0
        self.__codigo = 0

    @property
    def salario(self):
        return self.__salario

    @property
    def funcao(self):
        return self.__funcao

    @property
    def endereco(self):
        return self.__endereco

    @property
    def num_vendas(self):
        return self.__num_vendas
    
    @property
    def codigo(self):
        return self.__codigo

    @salario.setter
    def salario(self, salario):
        if isinstance(salario, float):
            self.__salario = salario

    @funcao.setter
    def funcao(self, funcao):
        if isinstance(funcao, str):
            self.__funcao = funcao

    @num_vendas.setter
    def num_vendas(self, vendas):
        self.__num_vendas = vendas

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @endereco.setter
    def endereco(self, rua, bairro, cidade):
        self.__endereco = Endereco(rua, bairro, cidade)
