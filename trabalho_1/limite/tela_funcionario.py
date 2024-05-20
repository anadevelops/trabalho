class TelaFuncionario:
    def tela_opcoes(self):
        print('---------- FUNCIONARIO ----------')
        print('Escolha a opção:')
        print('1 - Criar funcionário')
        print('2 - Atualizar funcionário')
        print('3 - Listar funcionários')
        print('4 - Excluir funcionário')
        print('0 - Retornar')
        
        try:
            opcao = int(input('Escolha a opção: '))
        except ValueError:
            self.mostra_msg('Formato de entrada está incorreto, reinicie o sistema e tente novamente')
        #except Exception as opcao not in range(0,6):
            #self.mostra_msg('Opção inexistente')
        else:
            return opcao

    def pega_dados_funcionario(self):
        print('---------- DADOS FUNCIONÁRIO ----------')
        while True:
            try:
                nome = str(input('Nome: '))
                cpf = int(input('CPF: '))
                funcao = str(input('Função: '))
                salario = float(input('Salário: '))
                rua = str(input('Rua: '))
                bairro = str(input('Bairro: '))
                cidade = str(input('Cidade: '))
    
            except ValueError:
                self.mostra_msg('Formato de informação está incorreto, tente novamente')
        
            else:
                return {'nome': nome,
                        'cpf': cpf,
                        'salario': salario,
                        'funcao': funcao,
                        'rua': rua,
                        'bairro': bairro,
                        'cidade': cidade}

    def mostra_funcionario(self, dados_funcionario):
        print('---------- FUNCIONÁRIO REGISTRADO ----------')
        print('NOME DO FUNCIONÁRIO: ', dados_funcionario['nome'])
        print('CPF DO FUNCIONÁRIO: ', dados_funcionario['cpf'])
        print('SALÁRIO DO FUNCIONÁRIO: ', dados_funcionario['salario'])
        print('FUNÇÃO DO FUNCIONÁRIO: ', dados_funcionario['funcao'])
        print('EDENREÇO DO FUNCIONÁRIO: ', dados_funcionario['endereco'])
        print('NÚMERO DE VENDAS DO FUNCIONÁRIO: ', dados_funcionario['num_vendas'])
        print('\n')

    def seleciona_funcionario(self):
        cpf = int(input('CPF do Funcionário que deseja selecionar: '))
        return cpf
    
    def mostra_msg(self, msg):
        print(msg)