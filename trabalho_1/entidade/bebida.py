from produto import Produto

class Bebida(Produto):
    def __init__(self, nome: str, custo: int, preco: float,
                 percent_comissao: float, codigo: int, veget: bool,
                 vegan: bool, gluten: bool, lactose: bool, grau_alcoolico: float):
        super().__init__(nome, custo, preco, percent_comissao, codigo,
                         veget, vegan, gluten, lactose)
        self.__grau_alcoolico = grau_alcoolico

    @property
    def grau_alcoolico(self):
        return self.__grau_alcoolico

    @grau_alcoolico.setter
    def grau_alcoolico(self, grau_alcoolico):
        self.__grau_alcoolico = grau_alcoolico