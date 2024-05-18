import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.funcionario import Funcionario
from trabalho_1.entidade.endereco import Endereco
from trabalho_1.limite.tela_funcionario import TelaFuncionario


class ControladorFuncionario:
    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema

    def pega_funcionario_p_cpf(self, cpf: int):
        for funcionario in self.__funcionarios:
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
            self.__funcionarios.append(new_func)
            self.__tela_funcionario.mostra_msg('Funcionário criado')

    def lista_funcionarios(self):
        for func in self.__funcionarios:
            self.__tela_funcionario.mostra_funcionario({'nome': func.nome,
                                            'cpf': func.cpf,
                                            'salario': func.salario,
                                            'funcao': func.funcao,
                                            'endereco': func.endereco.rua + ', ' + func.endereco.bairro + ', ' + func.endereco.cidade,
                                            'num_vendas': func.num_vendas})

    def altera_funcionario(self):
        self.lista_funcionarios()
        cpf_func = self.__tela_funcionario.seleciona_funcionario()
        func = self.pega_funcionario_p_cpf(cpf_func)

        if func is not None:
            novos_dados_func = self.__tela_funcionario.pega_dados_funcionario()
            func.nome = novos_dados_func['nome']
            func.cpf = novos_dados_func['cpf']
            func.salario = novos_dados_func['salario']
            func.endereco = Endereco(novos_dados_func['rua'], novos_dados_func['bairro'], novos_dados_func['cidade'])
            self.lista_funcionarios()
        else:
            return self.__tela_funcionario.mostra_msg('Funcionário inexistente')

    def del_funcionario(self):
        self.lista_funcionarios()
        cpf_func = self.__tela_funcionario.seleciona_funcionario()
        func = self.pega_funcionario_p_cpf(cpf_func)

        if func is not None:
            self.__funcionarios.remove(func)
            self.lista_funcionarios()
        else:
            self.__tela_funcionario.mostra_msg('Funcionário inexistente')

    def calcula_comissao(self):
        self.lista_funcionarios()
        cpf_func = self.__tela_funcionario.seleciona_funcionario()
        func = self.pega_funcionario_p_cpf(cpf_func)
        vendas = self.__controlador_sistema.controlador_vendas.vendas

        if func is not None:
            for venda in vendas:
                if venda.funcionario == func:
                    for refeicao in venda.refeicoes:
                        comissao = func.salario * refeicao.percent_comissao
                        soma_comissao += comissao
                    for bebida in venda.bebidas:
                        comissao = func.salario * bebida.percent_comissao
                        soma_comissao += comissao
        func.salario = func.salario + soma_comissao
        return self.__tela_funcionario.mostra_funcionario(func)

    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_funcionario,
                        2: self.altera_funcionario,
                        3: self.lista_funcionarios,
                        4: self.del_funcionario,
                        5: self.calcula_comissao,
                        0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()
