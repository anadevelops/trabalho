
class TelaBebida():

  def tela_opcoes(self):
    print("-------- AMIGOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Bebida")
    print("2 - Alterar Bebida")
    print("3 - Listar Bebidas")
    print("4 - Excluir Bebida")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_bebida(self):
    print("-------- DADOS BEBIDA ----------")
    nome = input("Nome: ")
    preco = input("Preço: ")
    percent_comissao = input("Comissão: ")
#    veget = input("Vegetariano: ")
#    vegan = input("Vegano: ")
#    gluten = input("Gluten: ")
#    lactose = input("Lactose: ")
    grau_alcoolico = input("Grau alcoolico: ")
    ingrediente1 = int(input("Código do ingrediente 1: "))
    ingrediente2 = int(input("Código do ingrediente 2: "))
    ingrediente3 = int(input("Código do ingrediente 3: "))

    return {"nome": nome, "preco": preco,
            "percent_comissao": percent_comissao,
            #"veget": veget,
            #"vegan": vegan, "gluten": gluten, "lactose": lactose,
            "ingrediente1": ingrediente1, "ingrediente2": ingrediente2,
            "ingrediente3": ingrediente3, "grau_alcoolico": grau_alcoolico}

  def mostra_bebida(self, dados_bebida):
    print("NOME DO PRATO: ", dados_bebida["nome"])
    print("CUSTO DO PRATO: ", dados_bebida["custo"])
    print("PRECO DO PRATO: ", dados_bebida["preco"])
    print("COMISSÃO DO PRATO: ", dados_bebida["percent_comissao"])
#    print("CÓDIGO DO PRATO: ", dados_bebida["codigo"])
#    print("VEGETARIANO: ", dados_bebida["veget"])
#    print("VEGANO: ", dados_bebida["vegan"])
#    print("GLUTEN: ", dados_bebida["gluten"])
#    print("LACTOSE: ", dados_bebida["lactose"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_bebida(self):
    codigo = input("Código da bebida que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)