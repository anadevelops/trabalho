import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from collections import defaultdict, Counter
from trabalho_1.entidade.venda import Venda
from trabalho_1.limite.tela_venda import TelaVenda


class ControladorVendas:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__vendas = []
        self.__tela_venda = TelaVenda()

    def pega_venda_p_codigo(self, codigo):
        for venda in self.__vendas:
            if venda.codigo == codigo:
                return venda
        return None

    @property
    def vendas(self):
      return [venda for venda in self.__vendas]

    def incluir_venda(self):
        self.__controlador_sistema.controlador_funcionario.lista_funcionarios()
        self.__controlador_sistema.controlador_cliente.lista_clientes()
        self.__controlador_sistema.controlador_bebida.lista_bebida()
        self.__controlador_sistema.controlador_refeicao.lista_refeicao()
        dados_venda = self.__tela_venda.pega_dados_venda()

        cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_p_cod(dados_venda['cliente'])
        funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_p_cpf(dados_venda['funcionario'])
        refeicao = self.__controlador_sistema.controlador_refeicao.pega_refeicao_por_codigo(dados_venda['refeicao'])
        bebida = self.__controlador_sistema.controlador_bebida.pega_bebida_por_codigo(dados_venda['bebida'])
        if (cliente is not None and funcionario is not None and (refeicao is not None or bebida is not None)):
            venda = Venda(cliente, funcionario, refeicao, bebida)
            venda.codigo = self.__controlador_sistema.gerador_codigo.gera_cod_venda()
            self.__vendas.append(venda)
            self.__tela_venda.mostra_msg('Venda criada')
        else:
            self.__tela_venda.mostra_msg('Dados inválidos')

    def lista_vendas(self):
        if len(self.__vendas) > 0:
            for venda in self.__vendas:
                self.__tela_venda.mostra_venda({'codigo': venda.codigo,
                                                'cliente': venda.cliente.nome,
                                                'funcionario': venda.funcionario.nome,
                                                'refeicoes': venda.refeicoes,
                                                'bebidas': venda.bebidas})
        else:
            self.__tela_venda.mostra_msg('Lista vazia')
    
    def altera_venda(self):
        self.lista_vendas()
        cod_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_p_codigo(cod_venda)

        if venda is not None:
            novos_dados_venda = self.__tela_venda.pega_dados_venda()
            venda.cliente = novos_dados_venda['cliente']
            venda.funcionario = novos_dados_venda['funcionario']
            venda.refeicoes = novos_dados_venda['refeicao']
            venda.bebidas = novos_dados_venda['bebida']
            self.__tela_venda.mostra_msg('Venda alterada')
            self.lista_vendas()
        else:
            return self.__tela_venda.mostra_msg('Venda inexistente')

    def excluir_venda(self):
        self.lista_vendas()
        cod_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_p_codigo(cod_venda)

        if venda is not None:
            self.__vendas.remove(venda)
            self.__tela_venda.mostra_msg('Venda removida')
            self.lista_vendas()
        else:
            self.__tela_venda.mostra_msg('Venda inexistente')

    def vendas_p_cliente(self):
        self.__controlador_sistema.controlador_cliente.lista_clientes()
        cod_cli = self.__tela_venda.seleciona_cliente()
        cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_p_cod(cod_cli)
        if cliente is not None:
            for venda in self.__vendas:
                if venda.cliente == cliente:
                    self.__tela_venda.mostra_venda({'codigo': venda.codigo,
                                                    'cliente': venda.cliente.nome,
                                                    'funcionario': venda.funcionario.nome,
                                                    'refeicoes': venda.refeicoes,
                                                    'bebidas': venda.bebidas})
        return None

    def vendas_p_funcionario(self):
        self.__controlador_sistema.controlador_funcionario.lista_funcionarios()
        cpf_func = self.__tela_venda.seleciona_funcionario()
        funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_p_cpf(cpf_func)
        if funcionario is not None:
            for venda in self.__vendas:
                if venda.funcionario == funcionario:
                    self.__tela_venda.mostra_venda({'codigo': venda.codigo,
                                                    'cliente': venda.cliente.nome,
                                                    'funcionario': venda.funcionario.nome,
                                                    'refeicoes': venda.refeicoes,
                                                    'bebidas': venda.bebidas})
        return None

    def vendas_abertas(self):
        vendas_abertas = [venda for venda in self.__vendas if venda.aberta is True]
        if len(vendas_abertas) > 0:
            for venda in vendas_abertas:
                self.__tela_venda.mostra_venda({'codigo': venda.codigo,
                                                'cliente': venda.cliente.nome,
                                                'funcionario': venda.funcionario.nome,
                                                'refeicoes': venda.refeicoes,
                                                'bebidas': venda.bebidas})
        else:
            self.__tela_venda.mostra_msg('Lista vazia')

    def vendas_encerradas(self):
        vendas_encerradas = [venda for venda in self.__vendas if venda.aberta is False]
        if len(vendas_encerradas) > 0:
            for venda in vendas_encerradas:
                self.__tela_venda.mostra_venda({'codigo': venda.codigo,
                                                'cliente': venda.cliente.nome,
                                                'funcionario': venda.funcionario.nome,
                                                'refeicoes': venda.refeicoes,
                                                'bebidas': venda.bebidas})
        else:
            self.__tela_venda.mostra_msg('Lista vazia')

    def encerrar_venda(self):
        self.vendas_abertas()
        cod_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_p_codigo(cod_venda)
        if venda is not None:
            for vend in self.__vendas:
                if vend.codigo == venda.codigo:
                    vend.aberta = False
                    self.__tela_venda.mostra_msg('Venda encerrada')
        else:
            self.__tela_venda.mostra_msg('Venda inexistente')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_venda,
                        2: self.altera_venda,
                        3: self.lista_vendas,
                        4: self.excluir_venda,
                        5: self.vendas_p_funcionario,
                        6: self.vendas_p_cliente,
                        7: self.vendas_abertas,
                        8: self.vendas_encerradas,
                        9: self.encerrar_venda,
                        0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()
