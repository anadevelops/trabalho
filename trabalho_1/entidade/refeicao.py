import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.produto import Produto
from trabalho_1.entidade.suprimento import Suprimento

class Refeicao(Produto):
    def __init__(self, nome: str, preco: float,
                 percent_comissao: float, codigo: int, veget: bool,
                 vegan: bool, gluten: bool, lactose: bool,
                 ingrediente1: Suprimento, ingrediente2: Suprimento, ingrediente3: Suprimento):
        super().__init__(nome, preco, percent_comissao, codigo,
                         veget, vegan, gluten, lactose,
                         ingrediente1, ingrediente2, ingrediente3)
