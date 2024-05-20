import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.limite.tela_refeicao import TelaRefeicao
from trabalho_1.entidade.refeicao import Refeicao

class ControladorRefeicao():

    def __init__(self, controlador_sistema):
        self.__refeicoes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_refeicao = TelaRefeicao()

    @property
    def refeicoes(self):
        return self.__refeicoes

    @refeicoes.setter
    def refeicoes(self, refeicao):
        self.__refeicoes.append(refeicao)

    def pega_refeicao_por_codigo(self, codigo: int):
        for refeicao in self.__refeicoes:
            if(refeicao.codigo == codigo):
                return refeicao
        return None

    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()

        ing1 = self.__controlador_sistema.controlador_suprimento.pega_suprimento_por_codigo(dados_refeicao['ingrediente1'])
        ing2 = self.__controlador_sistema.controlador_suprimento.pega_suprimento_por_codigo(dados_refeicao['ingrediente2'])

        if ing1 is not None and ing2 is not None:

            if (isinstance(dados_refeicao["nome"], str)):

                if (isinstance(self.verifica_booleano(dados_refeicao["veget"]), bool) and
                    isinstance(self.verifica_booleano(dados_refeicao["vegan"]), bool) and
                    isinstance(self.verifica_booleano(dados_refeicao["gluten"]), bool) and
                    isinstance(self.verifica_booleano(dados_refeicao["lactose"]), bool)):
                        
                        nova_refeicao = Refeicao(dados_refeicao["nome"],
                                            dados_refeicao["veget"], dados_refeicao["vegan"], 
                                            dados_refeicao["gluten"], dados_refeicao["lactose"],
                                            ing1, ing2)
                        nova_refeicao.codigo = self.__controlador_sistema.gerador_codigo.gera_cod_refeicao()
                        self.__refeicoes.append(nova_refeicao)
                        self.__tela_refeicao.mostra_mensagem("Refeicao adicionada")

                else:
                    self.__tela_bebida.mostra_mensagem("Dados incorretos: impossível criar refeicao")
            
            else:
                self.__tela_bebida.mostra_mensagem("Dados incorretos: impossível criar refeicao")

        else:
            self.__tela_refeicao.mostra_mensagem('Dados incorretos: impossível criar refeicao')

    def alterar_refeicao(self):
        self.lista_refeicao()
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.pega_refeicao_por_codigo(codigo_refeicao)

        if(refeicao is not None):
            novos_dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()

            ing1 = self.__controlador_sistema.controlador_suprimento.pega_suprimento_por_codigo(novos_dados_refeicao['ingrediente1'])
            ing2 = self.__controlador_sistema.controlador_suprimento.pega_suprimento_por_codigo(novos_dados_refeicao['ingrediente2'])

            if ing1 is not None and ing2 is not None:

                if (isinstance(novos_dados_refeicao["nome"], str)):

                    if (isinstance(self.verifica_booleano(novos_dados_refeicao["veget"]), bool) and
                    isinstance(self.verifica_booleano(novos_dados_refeicao["vegan"]), bool) and
                    isinstance(self.verifica_booleano(novos_dados_refeicao["gluten"]), bool) and
                    isinstance(self.verifica_booleano(novos_dados_refeicao["lactose"]), bool)):

                        refeicao.nome = novos_dados_refeicao["nome"]
                        refeicao.veget = novos_dados_refeicao["veget"]
                        refeicao.vegan = novos_dados_refeicao["vegan"]
                        refeicao.gluten = novos_dados_refeicao["gluten"]
                        refeicao.lactose = novos_dados_refeicao["lactose"]

                        refeicao.altera_primeiro_ing(ing1)
                        refeicao.altera_segundo_ing(ing2)
                        self.lista_refeicao()
                    else:
                        self.__tela_bebida.mostra_mensagem("Dados incorretos: impossível alterar bebida")
                
                else:
                    self.__tela_bebida.mostra_mensagem("Dados incorretos: impossível alterar bebida")   
            
            else:
                self.__tela_bebida.mostra_mensagem("Dados incorretos: impossível alterar bebida")

        else:
            self.__tela_refeicao.mostra_mensagem("ATENCAO: Refeicao não existente")

    def lista_refeicao(self):
        if len(self.__refeicoes) > 0:
            for refeicao in self.__refeicoes:
                ing1 = refeicao.pega_primeiro_ing()
                ing2 = refeicao.pega_segundo_ing()
                self.__tela_refeicao.mostra_refeicao({"nome": refeicao.nome,
                                                      "custo": refeicao.custo,
                                                        "preco": refeicao.preco,
                                                        "codigo": refeicao.codigo,
                                                        "veget": refeicao.veget, "vegan": refeicao.vegan,
                                                        "gluten": refeicao.gluten, "lactose": refeicao.lactose,
                                                        "ingrediente1": ing1.nome,
                                                        "ingrediente2": ing2.nome})
        else:
            self.__tela_refeicao.mostra_mensagem('ATENCAO: Não existem refeicoes cadastradas')

    def excluir_refeicao(self):
        self.lista_refeicao()
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.pega_refeicao_por_codigo(codigo_refeicao)

        if(refeicao is not None):
            self.__refeicoes.remove(refeicao)
            self.lista_refeicao()
        else:
            self.__tela_refeicao.mostra_mensagem("ATENCAO: Refeicoes não existente")

    def verifica_booleano(self, dado_em_string):
        if dado_em_string.lower() == 'true':
            return True
        elif dado_em_string.lower() == 'false':
            return False
        else:
            return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_refeicao, 2: self.alterar_refeicao, 3: self.lista_refeicao,
                        4: self.excluir_refeicao, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_refeicao.tela_opcoes()]()