class Suprimento:
    def __init__(self, nome: str, qtd: int, preco: int):
        self.__nome = nome
        self.__qtd = qtd
        self.__preco = preco
        self.__codigo = 0

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome

    @property
    def qtd(self):
        return self.__qtd

    @property
    def preco(self):
        return self.__preco

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    
    @qtd.setter
    def qtd(self, qtd):
        if isinstance(qtd, int):
            self.__qtd = qtd

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo