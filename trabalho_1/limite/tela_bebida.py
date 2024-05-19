
class TelaBebida():

  def tela_opcoes(self):
    print("-------- BEBIDAS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Bebida")
    print("2 - Alterar Bebida")
    print("3 - Listar Bebidas")
    print("4 - Excluir Bebida")
    print("0 - Retornar")

    try:
      opcao = int(input("Escolha a opcao: "))
    except ValueError:
      self.mostra_mensagem('Formato de entrada está incorreto, reinicie o sistema e tente novamente')
    else:
      return opcao

  def pega_dados_bebida(self):
    print("-------- DADOS BEBIDA ----------")
    while True:
      try:
        nome = input("Nome: ")
        veget = input("Vegetariano: ")
        vegan = input("Vegano: ")
        gluten = input("Gluten: ")
        lactose = input("Lactose: ")
        grau_alcoolico = input("Grau alcoolico: ")
        ingrediente1 = int(input("Código do ingrediente 1: "))
        ingrediente2 = int(input("Código do ingrediente 2: "))

      except ValueError:
        self.mostra_mensagem('Formato de informação está incorreto, tente novamente')

      else:
        return {"nome": nome,
                "veget": veget, "vegan": vegan,
                "gluten": gluten, "lactose": lactose,
                "ingrediente1": ingrediente1, "ingrediente2": ingrediente2,
                "grau_alcoolico": grau_alcoolico}

  def mostra_bebida(self, dados_bebida):
    print("--------- BEBIDA REGISTRADA ----------")
    print("NOME DA BEBIDA: ", dados_bebida["nome"])
    print("PRECO DA BEBIDA: ", dados_bebida["preco"])
    print("GRAU ALCOOLICO: ", dados_bebida["grau_alcoolico"])
    print("INGREDIENTE 1: ", dados_bebida["ingrediente1"])
    print("INGREDIENTE 2: ", dados_bebida["ingrediente2"])
    print("VEGETARIANO: ", dados_bebida["veget"])
    print("VEGANO: ", dados_bebida["vegan"])
    print("GLUTEN: ", dados_bebida["gluten"])
    print("LACTOSE: ", dados_bebida["lactose"])
    print("CÓDIGO DA BEBIDA: ", dados_bebida["codigo"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_bebida(self):
    codigo = int(input("Código da bebida que deseja selecionar: "))
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)