from trabalho_1.entidade.pessoa import Pessoa
from trabalho_1.entidade.endereco import Endereco


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: int, salario: float, funcao: str, rua: str, bairro: str, cidade: str):
        super().__init__(nome, cpf)
        self.__salario = salario
        self.__funcao = funcao
        self.__endereco = Endereco(rua, bairro, cidade)
        self.__num_vendas = 0

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

    @salario.setter
    def salario(self, salario):
        if isinstance(salario, float):
            self.__salario = salario

    @funcao.setter
    def funcao(self, funcao):
        if isinstance(funcao, str):
            self.__funcao = funcao
