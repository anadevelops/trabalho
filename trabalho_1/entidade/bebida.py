import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.produto import Produto
from trabalho_1.entidade.suprimento import Suprimento

class Bebida(Produto):
    def __init__(self, nome: str, preco: float,
                 percent_comissao: float,
                 #veget: bool,
                 #vegan: bool, gluten: bool, lactose: bool,
                 grau_alcoolico: float,
                 ingrediente1: Suprimento, ingrediente2: Suprimento, ingrediente3: Suprimento):
        super().__init__(nome, preco, percent_comissao,
                         #veget, vegan, gluten, lactose,
                         ingrediente1, ingrediente2, ingrediente3)
        self.__grau_alcoolico = grau_alcoolico

    @property
    def grau_alcoolico(self):
        return self.__grau_alcoolico

    @grau_alcoolico.setter
    def grau_alcoolico(self, grau_alcoolico):
        self.__grau_alcoolico = grau_alcoolico