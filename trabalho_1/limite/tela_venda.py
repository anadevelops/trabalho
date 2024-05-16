class TelaVenda:
    def tela_opcoes(self):
        print('---------- VENDA ----------')
        print('1 - Fazer venda')
        print('2 - Atualizar venda')
        print('3 - Listar vendas')
        print('4 - Excluir venda')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def pega_dados_venda(self):
        print('---------- DADOS VENDA ----------')
        cod = int(input('Código: '))
        cli = int(input('Cliente:' ))
        func = int(input('Funcionário: '))
        ref = int(input('Refeição: '))
        beb = int(input('Bebida: '))

        return {'codigo': cod,
                 'cliente': cli,
                 'funcionario': func,
                 'refeicao': ref,
                 'bebida': beb}

    def mostra_venda(self, dados_venda):
        print('Código da venda: ', dados_venda['codigo'])
        print('Cliente da venda: ' , dados_venda['cliente'])
        print('Funcionário da venda: ', dados_venda['funcionario'])
        print('Refeições da venda: ')
        print('\n')
    
    def seleciona_venda(self):
        cod = int(input('Código da venda que deseja selecionar: '))
        return cod

    def mostra_msg(self, msg):
        print(msg)