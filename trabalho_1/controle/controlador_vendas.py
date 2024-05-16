from trabalho_1.entidade.venda import Venda
from trabalho_1.limite.tela_venda import TelaVenda


class ControladorVendas:
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__vendas = []
    self.__tela_venda = TelaVenda()
    self.contador = 0


  def pega_venda_p_codigo(self, codigo: int):
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
        self.contador += 1
        venda = Venda(self.contador, cliente, funcionario, refeicao, bebida)
        self.__vendas.append(venda)
    else:
        self.__tela_venda.mostra_msg("Dados invalidos")

  #Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_vendas(self):
    for venda in self.__vendas:
      self.__tela_venda.mostra_venda({'codigo': venda.codigo,
                                      'cliente': venda.cliente,
                                      'funcionario': venda.funcionario,
                                      'refeicoes': venda.refeicoes,
                                      'bebidas': venda.bebidas})

  def excluir_venda(self):
    self.lista_vendas()
    codigo_venda = self.__tela_venda.seleciona_venda()
    venda = self.pega_venda_p_codigo(int(codigo_venda))

    if (venda is not None):
      self.__vendas.remove(venda)
      self.lista_vendas()
    else:
      self.__tela_venda.mostra_msg("ATENCAO: Venda não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_emprestimo, 2: self.lista_emprestimo, 3: self.excluir_emprestimo,0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_emprestimo.tela_opcoes()]()