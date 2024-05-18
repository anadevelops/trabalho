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
        #Quando forem criadas as outras entidades, é só ir adicionando
        print('0 - Encerrar sistema')

        opcao = int(input('Escolha a opção: '))
        return opcao