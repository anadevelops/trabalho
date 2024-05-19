class TelaSistema:
    def tela_opcoes(self):
        print('---------- SISTEMA ----------')
        print('Escolha sua opção')
        print('1 - Clientes')
        print('2 - Funcionários')
        print('3 - Refeições')
        print('4 - Bebidas')
        print('5 - Suprimentos')
        print('6 - Vendas')
        print('0 - Encerrar sistema')

        try:
            opcao = int(input('Escolha a opção: '))
        except ValueError:
            self.mostra_mensagem('Formato de entrada está incorreto. Tente novamente')
        else:
            return opcao

    def mostra_mensagem(self, msg):
        print(msg)
    