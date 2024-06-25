import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.funcionario import Funcionario
from trabalho_1.entidade.endereco import Endereco
from trabalho_1.limite.tela_funcionario import TelaFuncionario
from trabalho_1.DAOs.funcionario_dao import FuncionarioDAO


class ControladorFuncionario:
    def __init__(self, controlador_sistema):
        self.__funcionario_DAO = FuncionarioDAO()
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema

    def pega_funcionario_p_cpf(self, cpf: int):
        for funcionario in self.__funcionario_DAO.get_all():
            if funcionario.cpf == cpf:
                return funcionario
        return None

    def add_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        new_func = Funcionario(dados_funcionario['nome'],
                                dados_funcionario['cpf'],
                                dados_funcionario['salario'],
                                dados_funcionario['funcao'],
                                dados_funcionario['rua'],
                                dados_funcionario['bairro'],
                                dados_funcionario['cidade'])
        new_func.num_vendas = 0
        if isinstance(new_func, Funcionario):
            self.__funcionario_DAO.add(new_func)
            self.__tela_funcionario.mostra_msg('Funcionário criado')
        else:
            self.__tela_funcionario.mostra_msg('Dados incorretos: impossível criar funcionário')

    def lista_funcionarios(self):
        dados_funcionario = []
        for func in self.__funcionario_DAO.get_all():
            dados_funcionario.append({'nome': func.nome,
                                        'cpf': func.cpf,
                                        'salario': func.salario,
                                        'funcao': func.funcao,
                                        'endereco': func.endereco.rua + ', ' + func.endereco.bairro + ', ' + func.endereco.cidade,
                                        'num_vendas': func.num_vendas})
        self.__tela_funcionario.mostra_funcionario(dados_funcionario)

    def altera_funcionario(self):
        self.lista_funcionarios()
        cpf_func = self.__tela_funcionario.seleciona_funcionario()
        func = self.pega_funcionario_p_cpf(cpf_func)

        if func is not None:
            novos_dados_func = self.__tela_funcionario.pega_dados_funcionario_att()
            func.nome = novos_dados_func['nome']
            func.salario = novos_dados_func['salario']
            func.rua = novos_dados_func['rua']
            func.bairro = novos_dados_func['bairro']
            func.cidade = novos_dados_func['cidade']
            self.__funcionario_DAO.update(func)
            self.lista_funcionarios()
        else:
            return self.__tela_funcionario.mostra_msg('Funcionário inexistente')

    def del_funcionario(self):
        self.lista_funcionarios()
        cpf_func = self.__tela_funcionario.seleciona_funcionario()
        func = self.pega_funcionario_p_cpf(cpf_func)

        if func is not None:
            self.__funcionario_DAO.remove(func.cpf)
            self.lista_funcionarios()
        else:
            self.__tela_funcionario.mostra_msg('Funcionário inexistente')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_funcionario,
                        2: self.altera_funcionario,
                        3: self.lista_funcionarios,
                        4: self.del_funcionario,
                        0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()
