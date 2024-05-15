from produto import Produto

class Refeicao(Produto):
    def __init__(self, nome: str, custo: int, preco: float,
                 percent_comissao: float, codigo: int, veget: bool,
                 vegan: bool, gluten: bool, lactose: bool):
        super().__init__(nome, custo, preco, percent_comissao, codigo,
                         veget, vegan, gluten, lactose)
