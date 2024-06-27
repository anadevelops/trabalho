import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.suprimento import Suprimento
from trabalho_1.limite.tela_suprimento import TelaSuprimento
from trabalho_1.DAOs.suprimento_dao import SuprimentoDAO
import random

class ControladorSuprimento():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__suprimento_DAO = SuprimentoDAO()
        self.__tela_suprimento = TelaSuprimento()

    def pega_suprimento_por_codigo(self, codigo: int):
        for suprimento in self.__suprimento_DAO.get_all():
            if(suprimento.codigo == codigo):
                return suprimento
        return None
        
    def incluir_suprimento(self):
        dados_suprimento = self.__tela_suprimento.pega_dados_suprimento()
        novo_suprimento = Suprimento(dados_suprimento["nome"],
                                     dados_suprimento["preco"])
        novo_suprimento.codigo = random.randint(1, 1000)
        if isinstance(novo_suprimento, Suprimento):
            self.__suprimento_DAO.add(novo_suprimento)
            self.__tela_suprimento.mostra_msg('Suprimento criado')
        else:
            self.__tela_suprimento.mostra_msg('Dados incorretos: impossível criar suprimento')
    
    def listar_suprimentos(self):
        dados_suprimento = []
        for sup in self.__suprimento_DAO.get_all():
            dados_suprimento.append({'nome': sup.nome, 'preco': sup.preco, 'codigo': sup.codigo})
        self.__tela_suprimento.mostra_suprimento(dados_suprimento)

    def altera_suprimento(self):
        self.listar_suprimentos()
        cod_sup = self.__tela_suprimento.seleciona_suprimento()
        sup = self.pega_suprimento_por_codigo(cod_sup)

        if sup is not None:
            novos_dados_sup = self.__tela_suprimento.pega_dados_suprimento()
            sup.nome = novos_dados_sup['nome']
            sup.preco = novos_dados_sup['preco']
            self.__suprimento_DAO.update(sup)
            self.listar_suprimentos()
        else:
            return self.__tela_suprimento.mostra_msg('Suprimento inexistente')

    def excluir_suprimento(self):
        self.listar_suprimentos()
        cod_sup = self.__tela_suprimento.seleciona_suprimento()
        sup = self.pega_suprimento_por_codigo(cod_sup)

        if sup is not None:
            self.__suprimento_DAO.remove(sup.codigo)
            self.listar_suprimentos()
        else:
            self.__tela_suprimento.mostra_msg('ATENCAO: Suprimento inexistente')

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
