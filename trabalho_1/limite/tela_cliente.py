class TelaCliente:
    def tela_opcoes(self):
        print('---------- CLIENTE ----------')
        print('1 - Criar cliente')
        print('2 - Atualizar cliente')
        print('3 - Listar clientes')
        print('4 - Excluir cliente')
        print('0 - Retornar') 

        try:
            opcao = int(input('Escolha a opção: '))
        except ValueError:
            self.mostra_msg('Formato de entrada está incorreto, reinicie o sistema e tente novamente')
        else:
            return opcao

    def pega_dados_cliente(self):
        print('---------- DADOS CLIENTE ----------')
        while True:
            try:
                nome = str(input('Nome: '))
                cpf = int(input('CPF: '))

            except ValueError:
                self.mostra_msg('Formato de informação está incorreto, tente novamente')

            else:
                return {'nome': nome,
                        'cpf': cpf}

    def mostra_cliente(self, dados_cliente):
        print('---------- CLIENTE REGISTRADO ----------')
        print('NOME DO CLIENTE: ', dados_cliente['nome'])
        print('CPF DO CLIENTE: ', dados_cliente['cpf'])
        print('CÓDIGO DO CLIENTE: ', dados_cliente['codigo'])
        print('\n')
    
    def seleciona_cliente(self):
        cod = int(input('Código do cliente que deseja selecionar: '))
        return cod

    def mostra_msg(self, msg):
        print(msg)