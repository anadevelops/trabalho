class Suprimento:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco
        self.__codigo = 0

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo