from trabalho_1.DAOs.dao import DAO
from trabalho_1.entidade.funcionario import Funcionario

class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionario.pkl')

    def add(self, funcionario: Funcionario):
        if (funcionario is not None) and (isinstance(funcionario, Funcionario)) and (isinstance(funcionario.cpf, int)):
            super().add(funcionario.cpf, funcionario)

    def update(self, funcionario: Funcionario):
        if (funcionario is not None) and (isinstance(funcionario, Funcionario)) and (isinstance(funcionario.cpf, int)):
            super().update(funcionario.cpf, funcionario)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)