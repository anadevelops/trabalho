import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.limite.tela_bebida import TelaBebida
from trabalho_1.entidade.bebida import Bebida

class ControladorBebida():

    def __init__(self, controlador_sistema):
        self.__bebidas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_bebida = TelaBebida()

    def pega_bebida_por_codigo(self, codigo: int):
        for bebida in self.__bebidas:
            if(bebida.codigo == codigo):
                return bebida
        return None

    def incluir_bebida(self):
        dados_bebida = self.__tela_bebida.pega_dados_bebida()

        ing1 = self.__controlador_sistema.controlador_suprimento.pega_suprimento_por_codigo(dados_bebida['ingrediente1'])
        ing2 = self.__controlador_sistema.controlador_suprimento.pega_suprimento_por_codigo(dados_bebida['ingrediente2'])

        if ing1 is not None and ing2 is not None:
            nova_bebida = Bebida(dados_bebida["nome"],
                                 dados_bebida["preco"],
                                 dados_bebida["veget"], dados_bebida["vegan"],
                                 dados_bebida["gluten"], dados_bebida["lactose"],
                                ing1, ing2,
                                dados_bebida["grau_alcoolico"])
            nova_bebida.codigo = self.__controlador_sistema.gerador_codigo.gera_cod_bebida()
            self.__bebidas.append(nova_bebida)
            self.__tela_bebida.mostra_mensagem("Bebida adicionada")
        else:
            self.__tela_bebida.mostra_mensagem('Dados incorretos: impossível criar bebida')

    def alterar_bebida(self):
        self.lista_bebida()
        codigo_bebida = self.__tela_bebida.seleciona_bebida()
        bebida = self.pega_bebida_por_codigo(codigo_bebida)

        if(bebida is not None):
            novos_dados_bebida = self.__tela_bebida.pega_dados_bebida()
            bebida.nome = novos_dados_bebida["nome"]
            bebida.preco = novos_dados_bebida["preco"]
            bebida.veget = novos_dados_bebida["veget"]
            bebida.vegan = novos_dados_bebida["vegan"]
            bebida.gluten = novos_dados_bebida["gluten"]
            bebida.lactose = novos_dados_bebida["lactose"]
            bebida.grau_alcoolico = novos_dados_bebida["grau_alcoolico"]

            ing1 = self.__controlador_sistema.controlador_suprimento.pega_suprimento_por_codigo(novos_dados_bebida['ingrediente1'])
            ing2 = self.__controlador_sistema.controlador_suprimento.pega_suprimento_por_codigo(novos_dados_bebida['ingrediente2'])

            bebida.altera_primeiro_ing(ing1)
            bebida.altera_segundo_ing(ing2)
            self.lista_bebida()
        else:
            self.__tela_bebida.mostra_mensagem("ATENCAO: Bebida não existente")

    def lista_bebida(self):
        if len(self.__bebidas) > 0:
            for bebida in self.__bebidas:
                ing1 = bebida.pega_primeiro_ing()
                ing2 = bebida.pega_segundo_ing()
                self.__tela_bebida.mostra_bebida({"nome": bebida.nome,
                                                    "preco": bebida.preco,
                                                    "codigo": bebida.codigo,
                                                    "veget": bebida.veget, "vegan": bebida.vegan,
                                                    "gluten": bebida.gluten, "lactose": bebida.lactose,
                                                    "grau_alcoolico": bebida.grau_alcoolico,
                                                    "ingrediente1": ing1.nome,
                                                    "ingrediente2": ing2.nome})
        else:
            self.__tela_bebida.mostra_mensagem('ATENCAO: Não existem bebidas cadastradas')

    def excluir_bebida(self):
        self.lista_bebida()
        codigo_bebida = self.__tela_bebida.seleciona_bebida()
        bebida = self.pega_bebida_por_codigo(codigo_bebida)

        if(bebida is not None):
            self.__bebidas.remove(bebida)
            self.lista_bebida()
        else:
            self.__tela_bebida.mostra_mensagem("ATENCAO: Bebida não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_bebida, 2: self.alterar_bebida, 3: self.lista_bebida,
                        4: self.excluir_bebida, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_bebida.tela_opcoes()]()