import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.produto import Produto
from trabalho_1.entidade.suprimento import Suprimento

class Refeicao(Produto):
    def __init__(self, nome: str,
                 veget: bool,
                 vegan: bool, gluten: bool, lactose: bool,
                 ingrediente1: Suprimento, ingrediente2: Suprimento):
        super().__init__(nome,
                         veget, vegan, gluten, lactose,
                         ingrediente1, ingrediente2)
