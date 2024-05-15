from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def __init__(self, custo: int, preco: float,
                 percent_comissao: float, codigo: int, veget: bool,
                 vegan: bool, gluten: bool, lactose: bool):
        self.__custo = custo
        self.__preco = preco
        self.__percent_comissao = percent_comissao
        self.__codigo = codigo
        self.__veget = veget
        self.__vegan = vegan
        self.__gluten = gluten
        self.__lactose = lactose

    @property
    def custo(self):
        return self.__custo

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

    @custo.setter
    def custo(self, custo):
        self.__custo = custo

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