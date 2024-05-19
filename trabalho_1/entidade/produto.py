import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from abc import ABC, abstractmethod
from trabalho_1.entidade.suprimento import Suprimento

class Produto(ABC):
    @abstractmethod
    def __init__(self, nome: str, preco: float,
                 #veget: bool,
                 #vegan: bool, gluten: bool, lactose: bool,
                 ingrediente1: Suprimento, ingrediente2: Suprimento):
        self.__nome = nome
        self.__preco = preco
       # self.__codigo = codigo
        #self.__veget = veget
        #self.__vegan = vegan
        #self.__gluten = gluten
        #self.__lactose = lactose
        self.__codigo = 0

        self.__ingredientes = []
        self.__custo = 0

        self.__ingredientes.append(ingrediente1)
        self.__ingredientes.append(ingrediente2)

        for ingrediente in self.__ingredientes:
            self.__custo += ingrediente.preco

    @property
    def custo(self):
        return self.__custo
    
    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def codigo(self):
       return self.__codigo

#    @property
#    def veget(self):
 #       return self.__veget

 #   @property
  #  def vegan(self):
 #       return self.__vegan
#
#    @property
 #   def gluten(self):
 #       return self.__gluten

  #  @property
#    def lactose(self):
 #       return self.__lactose

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

#    @veget.setter
#    def veget(self, veget):
#        self.__veget = veget

#    @vegan.setter
#    def vegan(self, vegan):
#        self.__vegan = vegan

#    @gluten.setter
#    def gluten(self, gluten):
#        self.__gluten = gluten

#    @lactose.setter
#    def lactose(self, lactose):
#        self.__lactose = lactose

    def pega_primeiro_ingrediente(self):
        return self.__ingredientes[0]

    def pega_segundo_ingrediente(self):
        return self.__ingredientes[1]
    
    def altera_primeiro_ing(self, ing: Suprimento):
        self.__ingredientes[0] = ing

    def altera_segundo_ing(self, ing: Suprimento):
        self.__ingredientes[1] = ing