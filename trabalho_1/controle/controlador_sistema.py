import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.controle.controlador_cliente import ControladorCliente
from trabalho_1.controle.controlador_funcionario import ControladorFuncionario
from trabalho_1.controle.controlador_suprimento import ControladorSuprimento
from trabalho_1.controle.controlador_bebida import ControladorBebida
from trabalho_1.controle.controlador_refeicoes import ControladorRefeicao
from trabalho_1.controle.controlador_vendas import ControladorVendas
from trabalho_1.controle.gerador_codigo import GeradorCodigo
from trabalho_1.limite.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_suprimento = ControladorSuprimento(self)
        self.__controlador_bebida = ControladorBebida(self)
        self.__controlador_refeicao = ControladorRefeicao(self)
        self.__controlador_vendas = ControladorVendas(self)
        self.__gerador_codigo = GeradorCodigo()
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    @property
    def controlador_suprimento(self):
        return self.__controlador_suprimento

    @property
    def controlador_bebida(self):
        return self.__controlador_bebida

    @property
    def controlador_refeicao(self):
        return self.__controlador_refeicao

    @property
    def controlador_vendas(self):
        return self.__controlador_vendas

    @property
    def gerador_codigo(self):
        return self.__gerador_codigo

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_cliente(self):
        self.__controlador_cliente.abre_tela()

    def cadastra_funcionario(self):
        self.__controlador_funcionario.abre_tela()

    def cadastra_suprimento(self):
        self.__controlador_suprimento.abre_tela()

    def cadastra_refeicao(self):
        self.__controlador_refeicao.abre_tela()

    def cadastra_bebidas(self):
        self.__controlador_bebida.abre_tela()

    def cadastra_vendas(self):
        self.__controlador_vendas.abre_tela()

    def encerra_sistema(self):
        exit(0)
        
    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_cliente,
                        2: self.cadastra_funcionario,
                        3: self.cadastra_refeicao,
                        4: self.cadastra_bebidas,
                        5: self.cadastra_suprimento,
                        6: self.cadastra_vendas,
                        0: self.encerra_sistema}
            
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()