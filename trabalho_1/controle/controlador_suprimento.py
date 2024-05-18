import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.suprimento import Suprimento
from trabalho_1.limite.tela_suprimento import TelaSuprimento

class ControladorSuprimento():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__suprimentos = []
        self.__tela_suprimento = TelaSuprimento()
        
    def pega_suprimento_por_codigo(self, codigo: int):
        for suprimento in self.__suprimentos:
            if(suprimento.codigo == codigo):
                return suprimento
        return None
        
    def incluir_suprimento(self):
        dados_suprimento = self.__tela_suprimento.pega_dados_suprimento()
        novo_suprimento = Suprimento(dados_suprimento["nome"],
                                     dados_suprimento["qtd"],
                                     dados_suprimento["preco"])
        novo_suprimento.codigo = self.__controlador_sistema.gerador_codigo.gera_cod_suprimento()
        print(novo_suprimento.codigo)
        if isinstance(novo_suprimento, Suprimento):
            self.__suprimentos.append(novo_suprimento)
            self.__tela_suprimento.mostra_mensagem('Suprimento criado')
        else:
            self.__tela_suprimento.mostra_mensagem('Dados incorretos: impossível criar suprimento')
    
    def listar_suprimentos(self):
        if len(self.__suprimentos) > 0:
            for sup in self.__suprimentos:
                self.__tela_suprimento.mostra_suprimento({'nome': sup.nome,
                                                        'qtd': sup.qtd,
                                                        'preco': sup.preco,
                                                        'codigo': sup.codigo})
        else:
            self.__tela_suprimento.mostra_mensagem('Não existem suprimentos cadastrados')

    def altera_suprimento(self):
        self.listar_suprimentos()
        cod_sup = self.__tela_suprimento.seleciona_suprimento()
        sup = self.pega_suprimento_por_codigo(cod_sup)

        if sup is not None:
            novos_dados_sup = self.__tela_suprimento.pega_dados_suprimento()
            sup.nome = novos_dados_sup['nome']
            sup.qtd = novos_dados_sup['qtd']
            sup.preco = novos_dados_sup['preco']
            self.listar_suprimentos()
        else:
            return self.__tela_suprimento.mostra_mensagem('Suprimento inexistente')

    def excluir_suprimento(self):
        self.listar_suprimentos()
        cod_sup = self.__tela_suprimento.seleciona_suprimento()
        sup = self.pega_suprimento_por_codigo(cod_sup)

        if sup is not None:
            self.__suprimentos.remove(sup)
            self.listar_suprimentos()
        else:
            self.__tela_suprimento.mostra_mensagem('Suprimento inexistente')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_suprimento,
                        2: self.altera_suprimento,
                        3: self.listar_suprimentos,
                        4: self.excluir_suprimento,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_suprimento.tela_opcoes()]()
