import sys
#sys.path.append(r'C:\Users\Usuario\Documents\DSO\trabalho_dso\limite')
#sys.path.append(r'C:\Users\Usuario\Documents\DSO\trabalho dso\entidade')

from tela_bebida import TelaBebida
from bebida import Bebida

class ControladorBebida():

    def __init__(self):
        self.__refeicoes = []
        self.__tela_bebida = TelaBebida()

    def pega_bebida_por_codigo(self, codigo: int):
        for bebida in self.__refeicoes:
            if(bebida.codigo == codigo):
                return bebida
        return None

    def incluir_bebida(self):
        dados_bebida = self.__tela_bebida.pega_dados_bebida()
        bebida = Bebida(dados_bebida["nome"], dados_bebida["custo"], dados_bebida["preco"],
                         dados_bebida["percent_comissao"], dados_bebida["codigo"], 
                         dados_bebida["veget"], dados_bebida["vegan"], 
                         dados_bebida["gluten"], dados_bebida["lactose"],
                         dados_bebida["grau_alcoolico"])
        self.__refeicoes.append(bebida)

    def alterar_bebida(self):
        self.lista_refeicoes()
        codigo_bebida = self.__tela_bebida.seleciona_bebida()
        bebida = self.pega_bebida_por_codigo(codigo_bebida)

        if(bebida is not None):
            novos_dados_bebida = self.__tela_bebida.pega_dados_bebida()
            bebida.nome = novos_dados_bebida["nome"]
            bebida.custo = novos_dados_bebida["custo"]
            bebida.preco = novos_dados_bebida["preco"]
            bebida.percent_comissao = novos_dados_bebida["percent_comissao"]
            bebida.codigo = novos_dados_bebida["codigo"]
            bebida.veget = novos_dados_bebida["veget"]
            bebida.vegan = novos_dados_bebida["vegan"]
            bebida.gluten = novos_dados_bebida["gluten"]
            bebida.lactose = novos_dados_bebida["lactose"]
            bebida.lactose = novos_dados_bebida["grau_alcoolico"]
            self.lista_refeicoes()
        else:
            self.__tela_bebida.mostra_mensagem("ATENCAO: Bebida não existente")

    def lista_refeicoes(self):
        for bebida in self.__refeicoes:
            self.__tela_bebida.mostra_bebida({"nome": bebida.nome, "custo": bebida.telefone,
                                                  "preco": bebida.preco, "percent_comissao": bebida.percent_bebida,
                                                  "codigo": bebida.codigo,
                                                  "veget": bebida.veget, "vegan": bebida.vegan,
                                                  "gluten": bebida.gluten, "lactose": bebida.lactose,
                                                  "grau_alcoolico": bebida.grau_alcoolico})

    def excluir_bebida(self):
        self.lista_refeicoes()
        codigo_bebida = self.__tela_bebida.seleciona_bebida()
        bebida = self.pega_bebida_por_codigo(codigo_bebida)

        if(bebida is not None):
            self.__refeicoes.remove(bebida)
            self.lista_refeicoes()
        else:
            self.__tela_bebida.mostra_mensagem("ATENCAO: Bebida não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_bebida, 2: self.alterar_bebida, 3: self.lista_refeicoes,
                        4: self.excluir_bebida, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_bebida.tela_opcoes()]()