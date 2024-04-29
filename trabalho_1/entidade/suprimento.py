class Suprimento:
    def __init__(self, codigo:int, nome: str, qtd: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(qtd, int):
            self.__qtd = qtd

    @property
    def codigo(self):
        self.__codigo

    @property
    def nome(self):
        self.__nome

    @property
    def qtd(self):
        self.__qtd

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    
    @qtd.setter
    def qtd(self, qtd):
        if isinstance(qtd, int):
            self.__qtd = qtd

