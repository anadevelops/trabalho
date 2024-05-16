#from limite.tela_amigo import TelaAmigo
from entidade.refeicao import Refeicao

class ControladorRefeicao():

    def __init__(self, controlador_sistema):
        self.__refeicoes = []
        #self.__tela_refeicao = TelaRefeicao()

    def pega_refeicao_por_codigo(self, codigo: int):
        for refeicao in self.__refeicoes:
            if(refeicao.codigo == codigo):
                return refeicao
        return None

    # Sugestão: não deixe cadastrar dois amigos com o mesmo CPF
    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
        refeicao = Refeicao(dados_refeicao["nome"], dados_refeicao["custo"], dados_refeicao["preco"],
                         dados_refeicao["percent_comissao"], dados_refeicao["codigo"], 
                         dados_refeicao["veget"], dados_refeicao["vegan"], 
                         dados_refeicao["gluten"], dados_refeicao["lactose"])
        self.__refeicoes.append(refeicao)

    def alterar_refeicao(self):
        self.lista_refeicoes()
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.pega_refeicao_por_codigo(codigo_refeicao)

        if(refeicao is not None):
            novos_dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
            refeicao.nome = novos_dados_refeicao["nome"]
            refeicao.custo = novos_dados_refeicao["custo"]
            refeicao.preco = novos_dados_refeicao["preco"]
            refeicao.percent_comissao = novos_dados_refeicao["percent_comissao"]
            refeicao.codigo = novos_dados_refeicao["codigo"]
            refeicao.veget = novos_dados_refeicao["veget"]
            refeicao.vegan = novos_dados_refeicao["vegan"]
            refeicao.gluten = novos_dados_refeicao["gluten"]
            refeicao.lactose = novos_dados_refeicao["lactose"]
            self.lista_refeicoes()
        else:
            self.__tela_refeicao.mostra_mensagem("ATENCAO: Refeicao não existente")

    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_refeicoes(self):
        for refeicao in self.__refeicoes:
            self.__tela_refeicao.mostra_refeicao({"nome": refeicao.nome, "custo": refeicao.telefone,
                                                  "preco": refeicao.preco, "percent_comissao": refeicao.percent_refeicao,
                                                  "percent_comissao": refeicao.percent_comissao, "codigo": refeicao.codigo,
                                                  "veget": refeicao.veget, "vegan": refeicao.vegan,
                                                  "gluten": refeicao.gluten, "lactose": refeicao.lactose,})

    def excluir_refeicao(self):
        self.lista_refeicoes()
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.pega_refeicao_por_codigo(codigo_refeicao)

        if(refeicao is not None):
            self.__refeicoes.remove(refeicao)
            self.lista_refeicoes()
        else:
            self.__tela_refeicao.mostra_mensagem("ATENCAO: Refeicao não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_refeicao, 2: self.alterar_refeicao, 3: self.lista_refeicoes,
                        4: self.excluir_refeicao, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_refeicao.tela_opcoes()]()