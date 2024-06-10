class TelaSuprimento():
    def tela_opcoes(self):
        print('---------- SUPRIMENTOS ----------')
        print('Escolha a opção:')
        print('1 - Criar novo suprimento')
        print('2 - Atualizar suprimento')
        print('3 - Listar suprimentos')
        print('4 - Excluir suprimento')
        print('0 - Retornar')

        try:
            opcao = int(input('Escolha a opção: '))
        except ValueError:
            self.mostra_mensagem('Formato de entrada está incorreto, reinicie o sistema e tente novamente')
        else:
            return opcao
    
    def pega_dados_suprimento(self):
        print('---------- DADOS DO SUPRIMENTO -----------')
        while True:
            try:
                nome = input('Nome do suprimento: ')
                preco = float(input('Preço do suprimento: '))
            
            except ValueError:
                self.mostra_mensagem('Formato de informação está incorreto, tente novamente')
            else:
                return {"nome": nome, "preco": preco}
    
    def mostra_suprimento(self, dados_suprimento):
        print("---------SUPRIMENTOS EM ESTOQUE----------")
        print("NOME DO SUPRIMENTO: ", dados_suprimento["nome"])
        print("PRECO DO SUPRIMENTO: ", dados_suprimento["preco"])
        print("CODIGO DO SUPRIMENTO: ", dados_suprimento["codigo"])
        print("\n")

    def seleciona_suprimento(self):
        codigo = int(input("Código do suprimento que deseja selecionar: "))
        return codigo
    
    def mostra_mensagem(self, msg):
        print(msg)

