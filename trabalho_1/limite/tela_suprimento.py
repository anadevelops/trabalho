class TelaSuprimento():
    def tela_opcoes(self):
        print('---------- SUPRIMENTOS ----------')
        print('Escolha a opção:')
        print('1 - Criar novo suprimento')
        print('2 - Atualizar suprimento')
        print('3 - Listar suprimentos')
        print('4 - Excluir suprimento')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_suprimento(self):
        print('---------- DADOS DO SUPRIMENTO -----------')
        nome = input('Nome do suprimento: ')
        qtd = int(input('Quantidade do suprimento: '))
        preco = float(input('Preço do suprimento: '))

        return {"nome": nome, "qtd": qtd, "preco": preco}
    
    def mostra_suprimento(self, dados_suprimento):
        print("NOME DO SUPRIMENTO: ", dados_suprimento["nome"])
        print("QUANTIDADE DO SUPRIMENTO: ", dados_suprimento["qtd"])
        print("PRECO DO SUPRIMENTO: ", dados_suprimento["preco"])
        print("CODIGO DO SUPRIMENTO: ", dados_suprimento["codigo"])
        print("\n")

    def seleciona_suprimento(self):
        codigo = int(input("Código do suprimento que deseja selecionar: "))
        return codigo
    
    def mostra_mensagem(self, msg):
        print(msg)

