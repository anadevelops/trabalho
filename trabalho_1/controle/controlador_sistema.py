from trabalho_1.controle.controlador_cliente import ControladorCliente
from trabalho_1.controle.controlador_funcionario import ControladorFuncionario
from trabalho_1.controle.controlador_suprimento import ControladorSuprimento
from trabalho_1.limite.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_suprimento = ControladorSuprimento(self)
        self.__controlador_bebida = ControladorBebida(self)
        self.__controlador_refeicoes = ControladorRefeicoes(self)
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

        def inicializa_sistema(self):
            self.abre_tela()
        
        def cadastra_cliente(self):
            self.__controlador_cliente.abre_tela()

        def cadastra_funcionario(self):
            self.__controlador_funcionario.abre_tela()

        def cadastra_suprimento(self):
            self.__controlador_suprimento.abre_tela()

        def encerra_sistema(self):
            exit(0)
        
        def abre_tela(self):
            lista_opcoes = {1: self.cadastra_cliente,
                            2: self.cadastra_funcionario,
                            3: self.cadastra_suprimento,
                            0: self.encerra_sistema}
            
            while True:
                opcao_escolhida = self.__tela_sistema.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()