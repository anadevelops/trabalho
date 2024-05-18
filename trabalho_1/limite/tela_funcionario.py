class TelaFuncionario:
    def tela_opcoes(self):
        print('---------- FUNCIONARIO ----------')
        print('Escolha a opção:')
        print('1 - Criar funcionário')
        print('2 - Atualizar funcionário')
        print('3 - Listar funcionários')
        print('4 - Excluir funcionário')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def pega_dados_funcionario(self):
        print('---------- DADOS FUNCIONÁRIO ----------')
        nome = str(input('Nome: '))
        cpf = int(input('CPF: '))
        funcao = str(input('Função: '))
        salario = float(input('Salário: '))
        rua = str(input('Rua: '))
        bairro = str(input('Bairro: '))
        cidade = str(input('Cidade: '))

        return {'nome': nome,
                'cpf': cpf,
                'salario': salario,
                'funcao': funcao,
                'rua': rua,
                'bairro': bairro,
                'cidade': cidade}

    def mostra_funcionario(self, dados_funcionario):
        print('Nome do funcionário: ', dados_funcionario['nome'])
        print('CPF do funcionário: ', dados_funcionario['cpf'])
        print('Salário do funcionário: ', dados_funcionario['salario'])
        print('Função do funcionário: ', dados_funcionario['funcao'])
        print('Endereço do funcionário: ', dados_funcionario['endereco'])
        print('Número de vendas do funcionário: ', dados_funcionario['num_vendas'])
        print('\n')

    def seleciona_funcionario(self):
        cpf = int(input('CPF do Funcionário que deseja selecionar: '))
        return cpf
    
    def mostra_msg(self, msg):
        print(msg)