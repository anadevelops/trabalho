
class TelaRefeicao():

  def tela_opcoes(self):
    print("-------- AMIGOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Refeição")
    print("2 - Alterar Refeição")
    print("3 - Listar Refeição")
    print("4 - Excluir Refeição")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_refeicao(self):
    print("-------- DADOS REFEIÇÃO ----------")
    nome = input("Nome: ")
    preco = input("Preço: ")
#    veget = input("Vegetariano: ")
#    vegan = input("Vegano: ")
#    gluten = input("Gluten: ")
#    lactose = input("Lactose: ")
    ingrediente1 = int(input("Código do ingrediente 1: "))
    ingrediente2 = int(input("Código do ingrediente 2: "))

    return {"nome": nome, "preco": preco,
            #"veget": veget,
            #"vegan": vegan, "gluten": gluten, "lactose": lactose,
            "ingrediente1": ingrediente1, "ingrediente2": ingrediente2}

  def mostra_refeicao(self, dados_refeicao):
    print("NOME DO PRATO: ", dados_refeicao["nome"])
    #print("CUSTO DO PRATO: ", dados_bebida["custo"])
    print("PRECO DO PRATO: ", dados_refeicao["preco"])
    print("INGREDIENTE 1: ", dados_refeicao["ingrediente1"])
    print("INGREDIENTE 2: ", dados_refeicao["ingrediente2"])
    print("CÓDIGO DO PRATO: ", dados_refeicao["codigo"])
#    print("CÓDIGO DO PRATO: ", dados_bebida["codigo"])
#    print("VEGETARIANO: ", dados_bebida["veget"])
#    print("VEGANO: ", dados_bebida["vegan"])
#    print("GLUTEN: ", dados_bebida["gluten"])
#    print("LACTOSE: ", dados_bebida["lactose"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_refeicao(self):
    codigo = int(input("Código da refeição que deseja selecionar: "))
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)