
class TelaRefeicao():

  def tela_opcoes(self):
    print("-------- REFEIÇÕES ----------")
    print("Escolha a opcao")
    print("1 - Incluir Refeição")
    print("2 - Alterar Refeição")
    print("3 - Listar Refeição")
    print("4 - Excluir Refeição")
    print("0 - Retornar")

    try:
      opcao = int(input("Escolha a opcao: "))
    except ValueError:
      self.mostra_mensagem('Formato de entrada está incorreto, reinicie o sistema e tente novamente')
    else:
      return opcao

  def pega_dados_refeicao(self):
    print("-------- DADOS REFEIÇÃO ----------")
    while True:
      try:
        nome = input("Nome: ")
        veget = input("Vegetariano: ")
        vegan = input("Vegano: ")
        gluten = input("Gluten: ")
        lactose = input("Lactose: ")
        ingrediente1 = int(input("Código do ingrediente 1: "))
        ingrediente2 = int(input("Código do ingrediente 2: "))

      except ValueError:
        self.mostra_mensagem('Formato de informação está incorreto, tente novamente')

      else:
        return {"nome": nome,
                "veget": veget,
                "vegan": vegan, "gluten": gluten, "lactose": lactose,
                "ingrediente1": ingrediente1, "ingrediente2": ingrediente2}

  def mostra_refeicao(self, dados_refeicao):
    print("--------- REFEIÇÃO REGISTRADA ----------")
    print("NOME DO PRATO: ", dados_refeicao["nome"])
    print("CUSTO DO PRATO: ", dados_refeicao["custo"])
    print("PRECO DO PRATO: ", dados_refeicao["preco"])
    print("INGREDIENTE 1: ", dados_refeicao["ingrediente1"])
    print("INGREDIENTE 2: ", dados_refeicao["ingrediente2"])
    print("VEGETARIANO: ", dados_refeicao["veget"])
    print("VEGANO: ", dados_refeicao["vegan"])
    print("GLUTEN: ", dados_refeicao["gluten"])
    print("LACTOSE: ", dados_refeicao["lactose"])
    print("CÓDIGO DO PRATO: ", dados_refeicao["codigo"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_refeicao(self):
    codigo = int(input("Código da refeição que deseja selecionar: "))
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)