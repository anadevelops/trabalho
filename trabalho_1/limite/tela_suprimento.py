class TelaSuprimento():
    def tela_opcoes(self):
        print('---------- SUPRIMENTOS ----------')
        print('Escolha a opção:')
        print('1 - Criar novo suprimento')
        print('2 - Atualizar qtd de suprimento')
        print('3 - Listar suprimentos')
        print('4 - Excluir suprimento')

        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_suprimento(self):
        print('---------- DADOS DO SUPRIMENTO -----------')
        nome = input('Nome do suprimento: ')
        qtd = input('Quantidade do suprimento: ')
        codigo = input('Código do suprimento: ')

        return {"codigo": codigo, "nome": nome, "qtd": qtd}
    
    def mostra_suprimento(self, dados_suprimento):
        print("CODIGO DO SUPRIMENTO: ", dados_suprimento["codigo"])
        print("NOME DO SUPRIMENTO: ", dados_suprimento["nome"])
        print("QUANTIDADE DO SUPRIMENTO: ", dados_suprimento["qtd"])
        print("\n")

    def seleciona_suprimento(self):
        codigo = input("Código do suprimento que deseja selecionar: ")
        return codigo

