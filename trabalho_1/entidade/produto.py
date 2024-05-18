from abc import ABC, abstractmethod
from suprimento import Suprimento

class Produto(ABC):
    @abstractmethod
    def __init__(self, nome: str, preco: float,
                 percent_comissao: float, codigo: int, veget: bool,
                 vegan: bool, gluten: bool, lactose: bool,
                 ingrediente1: Suprimento, ingrediente2: Suprimento, ingrediente3: Suprimento):
        self.__nome = nome
        self.__preco = preco
        self.__percent_comissao = percent_comissao
        self.__codigo = codigo
        self.__veget = veget
        self.__vegan = vegan
        self.__gluten = gluten
        self.__lactose = lactose

        self.__suprimentos = []
        self.__custo = 0

        self.__suprimentos.append(ingrediente1)
        self.__suprimentos.append(ingrediente2)
        self.__suprimentos.append(ingrediente3)

        for suprimento in self.__suprimentos:
            self.__custo += suprimento.preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def percent_comissao(self):
        return self.__percent_comissao

    @property
    def codigo(self):
        return self.__codigo

    @property
    def veget(self):
        return self.__veget

    @property
    def vegan(self):
        return self.__vegan

    @property
    def gluten(self):
        return self.__gluten

    @property
    def lactose(self):
        return self.__lactose

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @percent_comissao.setter
    def percent_comissao(self, percent_comissao):
        self.__percent_comissao = percent_comissao

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @veget.setter
    def veget(self, veget):
        self.__veget = veget

    @vegan.setter
    def vegan(self, vegan):
        self.__vegan = vegan

    @gluten.setter
    def gluten(self, gluten):
        self.__gluten = gluten

    @lactose.setter
    def lactose(self, lactose):
        self.__lactose = lactose

    def calcula_custo(self):
        return self.__custo
