class TelaVenda:
    def tela_opcoes(self):
        print('---------- VENDA ----------')
        print('1 - Fazer venda')
        print('2 - Atualizar venda')
        print('3 - Listar todas as vendas')
        print('4 - Excluir venda')
        print('5 - Vendas por funcionario')
        print('6 - Vendas por cliente')
        print('7 - Refeicao mais vendida')
        print('8 - Bebida mais vendida')
        print('9 - Funcionario do mes')
        print('10 - Vendas em aberto')
        print('11 - Vendas encerradas')
        print('12 - Encerrar venda')
        print('0 - Retornar') 

        opcao = int(input('Escolha a opção: '))
        return opcao

    def pega_dados_venda(self):
        print('---------- DADOS VENDA ----------')
        cli = int(input('Cliente:' ))
        func = int(input('Funcionário: '))
        ref = int(input('Refeição: '))
        beb = int(input('Bebida: '))

        return {'cliente': cli,
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

    def seleciona_funcionario(self):
        cpf = int(input('CPF do funcionario: '))
        return cpf
    
    def seleciona_cliente(self):
        cod = int(input('Codigo do cliente: '))
        return cod

    def seleciona_refeicao(self):
        cod = int(input('Codigo da refeicao: '))
        return cod

    def seleciona_bebida(self):
        cod = int(input('Codigo da bebida: '))
        return cod

    def finaliza_venda(self):
        cod = int(input('Codigo da venda que deseja encerrar: '))
        return cod

    def mostra_msg(self, msg):
        print(msg)