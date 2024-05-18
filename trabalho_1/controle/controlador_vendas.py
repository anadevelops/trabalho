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

    def incluir_venda(self):
        self.__controlador_sistema.controlador_funcionario.lista_funcionarios()
        self.__controlador_sistema.controlador_cliente.lista_clientes()
        dados_venda = self.__tela_venda.pega_dados_venda()

        cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_p_cod(dados_venda['cliente'])
        funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_por_cpf(dados_venda['funcionario'])
        refeicao = self.__controlador_sistema.controlador_refeicao.pega_refeicao_por_codigo(dados_venda['refeicao'])
        bebida = self.__controlador_sistema.controlador_bebida.pega_bebida_por_codigo(dados_venda['bebida'])
        if (cliente is not None and funcionario is not None and refeicao is not None and bebida is not None):
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
                                                'cliente': venda.cliente,
                                                'funcionario': venda.funcionario,
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
            venda.refeicoes = novos_dados_venda['refeicoes']
            venda.bebidas = novos_dados_venda['bebidas']
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

    def vendas_p_cliente(self, codigo):
        cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_p_cod(codigo)
        if cliente is not None:
            for venda in self.__vendas:
                if venda.cliente == cliente:
                    return venda
        return None

    def vendas_p_funcionario(self, cpf):
        funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_p_cpf(cpf)
        if funcionario is not None:
            for venda in self.__vendas:
                if venda.funcionario == funcionario:
                    return venda
        return None

    def ref_mais_vendida(self):
        refeicoes = [venda.refeicoes for venda in self.__vendas]
        count = Counter(refeicoes)
        return max(count, key=count.get)

    def beb_mais_vendida(self):
        bebidas = [venda.bebidas for venda in self.__vendas]
        count = Counter(bebidas)
        return max(count, key=count.get)

    def func_do_mes(self):
        funcionarios = [venda.funcionario for venda in self.__vendas]
        count = Counter(funcionarios)
        return max(count, key=count.get)

    def vendas_abertas(self):
        if len(self.__vendas) > 0:
            for venda in self.__vendas:
                if venda.aberta == True:
                    self.__tela_venda.mostra_venda({'codigo': venda.codigo,
                                                    'cliente': venda.cliente,
                                                    'funcionario': venda.funcionario,
                                                    'refeicoes': venda.refeicoes,
                                                    'bebidas': venda.bebidas})
        else:
            self.__tela_venda.mostra_msg('Lista vazia')

    def vendas_encerradas(self):
        if len(self.__vendas) > 0:
            for venda in self.__vendas:
                if venda.aberta == False:
                    self.__tela_venda.mostra_venda({'codigo': venda.codigo,
                                                    'cliente': venda.cliente,
                                                    'funcionario': venda.funcionario,
                                                    'refeicoes': venda.refeicoes,
                                                    'bebidas': venda.bebidas})
        else:
            self.__tela_venda.mostra_msg('Lista vazia')

    def encerrar_venda(self, codigo):
        venda = self.pega_venda_p_codigo(codigo)
        if venda is not None:
            if venda.aberta == True:
                venda.aberta = False
                return venda
            else:
                self.__tela_venda.mostra_msg('Venda já encerrada')
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
                        7: self.ref_mais_vendida,
                        8: self.beb_mais_vendida,
                        9: self.func_do_mes,
                        10: self.vendas_abertas,
                        11: self.vendas_encerradas,
                        12: self.encerrar_venda,
                        0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()
