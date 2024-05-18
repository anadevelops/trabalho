import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int):
        super().__init__(nome, cpf)
        self.__codigo = 0

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo