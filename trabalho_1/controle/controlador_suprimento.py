from entidade.suprimento import Suprimento
from limite.tela_suprimento import TelaSuprimento

class ControleSuprimento():

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
        
        l = self.pega_suprimento_por_codigo(dados_suprimento["codigo"])
        if l is None:
            suprimento = Suprimento(dados_suprimento["codigo"], dados_suprimento["nome"], dados_suprimento["qtd"])
            self.__suprimentos.append(suprimento)
        else:
            self.__tela_suprimento.mostra_mensagem("ATENCAO: Suprimento já existente")
        return None
    
    def listar_suprimentos(self):
        for suprimento in self.__suprimentos:
            self.__tela_suprimento.mostra_suprimento({"Código": suprimento.codigo, "nome": suprimento.nome, "Quantidade": suprimento.qtd})

    def excluir_suprimento(self):
        self.listar_suprimentos()
        codigo_suprimento = self.__tela_suprimento.seleciona_suprimento()
        suprimento = self.pega_suprimento_por_codigo(int(codigo_suprimento))
        
        if (suprimento is not None):
            self.__suprimentos.remove(suprimento)
            self.listar_suprimentos()
        else:
            self.__tela_suprimento.mostra_mensagem("ATENCAO: Suprimento não existente")

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_emprestimo, 2: self.lista_emprestimo, 3: self.excluir_emprestimo,0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_emprestimo.tela_opcoes()]()
