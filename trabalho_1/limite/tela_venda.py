import PySimpleGUI as sg


class TelaVenda:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        if values['9']:
            opcao = 9
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
        '''
        print('---------- VENDA ----------')
        print('1 - Fazer venda')
        print('2 - Atualizar venda')
        print('3 - Listar todas as vendas')
        print('4 - Excluir venda')
        print('5 - Vendas por funcionário')
        print('6 - Vendas por cliente')
        print('7 - Vendas em aberto')
        print('8 - Vendas encerradas')
        print('9 - Encerrar venda')
        print('0 - Retornar') 

        try:
            opcao = int(input('Escolha a opção: '))
        except ValueError:
            self.mostra_msg('Formato de entrada está incorreto, reinicie o sistema e tente novamente')
        else:
            return opcao'''

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- VENDAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Venda', "RD1", key='1')],
            [sg.Radio('Alterar Venda', "RD1", key='2')],
            [sg.Radio('Listar todas as vendas', "RD1", key='3')],
            [sg.Radio('Excluir Venda', "RD1", key='4')],
            [sg.Radio('Vendas por funcionário', 'RD1', key='5')],
            [sg.Radio('Vendas por cliente', 'RD1', key='6')],
            [sg.Radio('Vendas em aberto', 'RD1', key='7')],
            [sg.Radio('Vendas encerradas', 'RD1', key='8')],
            [sg.Radio('Encerrar venda', 'RD1', key='9')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

    def pega_dados_venda(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('---------- DADOS VENDA ----------', font=("Helvica", 25))],
            [sg.Text('Cliente:', size=(15, 1)), sg.InputText('', key='cliente')],
            [sg.Text('Funcionário:', size=(15, 1)), sg.InputText('', key='funcionario')],
            [sg.Text('Refeição:', size=(15, 1)), sg.InputText('', key='refeicao')],
            [sg.Text('Bebida:', size=(15, 1)), sg.InputText('', key='bebida')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        cliente = values['cliente']
        funcionario = values['funcionario']
        refeicao = values['refeicao']
        bebida = values['bebida']

        self.close()
        return {"cliente": cliente, "funcionario": funcionario, 'refeicao': refeicao, 'bebida': bebida}


    def mostra_venda(self, dados_venda):
        string_todas_vendas = ''
        for dado in dados_venda:
            string_todas_vendas = string_todas_vendas + 'CÓDIGO DA VENDA: ' + str(dado['codigo']) + '\n'
            string_todas_vendas = string_todas_vendas + 'CLIENTE DA VENDA: ' + dado['cliente'] + '\n'
            string_todas_vendas = string_todas_vendas + 'FUNCIONÁRIO DA VENDA: ' + dado['funcionario'] + '\n'
            string_todas_vendas = string_todas_vendas + 'REFEIÇÕES DA VENDA: ' + dado['refeicoes'] + '\n'
            string_todas_vendas = string_todas_vendas + 'BEBIDAS DA VENDA: ' + dado['bebidas'] + '\n\n'

        sg.Popup('---------- VENDA REGISTRADA ----------', string_todas_vendas)

    
    def seleciona_venda(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONAR VENDA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da venda que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona venda').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def seleciona_funcionario(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONAR FUNCIONÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do funcionário que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona funcionário').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf
    
    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código do cliente que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona cliente').Layout(layout)

        button, values = self.open()
        codigo = int(values['codigo'])
        self.close()
        return codigo

    def seleciona_refeicao(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONAR REFEIÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da refeição que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona refeição').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def seleciona_bebida(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONAR BEBIDA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da bebida que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona bebida').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def finaliza_venda(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- ENCERRAR VENDA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da venda que deseja encerrar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Encerra venda').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def mostra_msg(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values