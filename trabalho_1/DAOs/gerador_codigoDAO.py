from trabalho_1.DAOs.dao import DAO
from trabalho_1.controle.gerador_codigo import GeradorCodigo

class GeradorDAO(DAO):
    def __init__(self):
        super().__init__('gerador.pkl')

    def update(self, amigo: Amigo):
        if((amigo is not None) and isinstance(amigo, Amigo) and isinstance(amigo.cpf, int)):
            super().update(amigo.cpf, amigo)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)
