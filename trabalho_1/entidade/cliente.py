from pessoa import *


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int, codigo: int):
        super().__init__(nome, cpf)
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo