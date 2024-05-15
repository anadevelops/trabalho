class TelaCliente:
    def tela_opcoes(self):
        print('---------- CLIENTE ----------')
        print('1 - Criar cliente')
        print('2 - Atualizar cliente')
        print('3 - Listar clientes')
        print('4 - Excluir cliente')
        print('0 - Retornar') 

        opcao = int(input('Escolha a opção: '))
        return opcao

    def pega_dados_cliente(self):
        print('---------- DADOS CLIENTE ----------')
        nome = str(input('Nome: '))
        cpf = int(input('CPF: '))
        codigo = int(input('Código: '))

        return {'nome': nome,
                 'cpf': cpf,
                 'codigo': codigo}

    def mostra_cliente(self, dados_cliente):
        print('Nome do cliente: ', dados_cliente['nome'])
        print('CPF do cliente: ', dados_cliente['cpf'])
        print('Código do cliente: ', dados_cliente['codigo'])
        print('\n')
    
    def seleciona_cliente(self):
        cod = int(input('Código do cliente que deseja selecionar: '))
        return cod

    def mostra_msg(self, msg):
        print(msg)