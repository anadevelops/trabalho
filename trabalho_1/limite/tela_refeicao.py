
class TelaRefeicao():

  def tela_opcoes(self):
    print("-------- AMIGOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Refeição")
    print("2 - Alterar Refeição")
    print("3 - Listar Refeições")
    print("4 - Excluir Refeição")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_refeicao(self):
    print("-------- DADOS REFEIÇÃO ----------")
    nome = input("Nome: ")
    custo = input("Custo: ")
    preco = input("Preço: ")
    percent_comissao = input("Comissão: ")
    codigo = input("Código: ")
    veget = input("Vegetariano: ")
    vegan = input("Vegano: ")
    gluten = input("Gluten: ")
    lactose = input("Lactose: ")

    return {"nome": nome, "custo": custo, "preco": preco,
            "Comissão": percent_comissao, "codigo": codigo, "veget": veget,
            "vegan": vegan, "gluten": gluten, "lactose": lactose}

  def mostra_refeicao(self, dados_refeicao):
    print("NOME DO PRATO: ", dados_refeicao["nome"])
    print("CUSTO DO PRATO: ", dados_refeicao["custo"])
    print("PRECO DO PRATO: ", dados_refeicao["preco"])
    print("COMISSÃO DO PRATO: ", dados_refeicao["percent_comissao"])
    print("CÓDIGO DO PRATO: ", dados_refeicao["codigo"])
    print("VEGETARIANO: ", dados_refeicao["veget"])
    print("VEGANO: ", dados_refeicao["vegan"])
    print("GLUTEN: ", dados_refeicao["gluten"])
    print("LACTOSE: ", dados_refeicao["lactose"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_refeicao(self):
    codigo = input("Código da refeição que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)