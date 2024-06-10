import PySimpleGUI as sg


class TelaCliente:
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
        '''
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
            return opcao'''

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('---------- CLIENTE ----------', font=('Helvetica', 25))],
            [sg.Text('Escolha sua opção:', font = ('Helvetica', 15))],
            [sg.Radio('Criar cliente', 'RD1', key = '1')],
            [sg.Radio('Atualizar cliente', 'RD1', key = '2')],
            [sg.Radio('Listar clientes', 'RD1', key = '3')],
            [sg.Radio('Excluir cliente', 'RD1', key = '4')],
            [sg.Radio('Retornar', 'RD1', key = '0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)

    def pega_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('---------- DADOS CLIENTE ----------', font = ('Helvetica', 25))],
            [sg.Text('Nome: ', size=(15,1)), sg.InputText('', key='nome')],
            [sg.Text('CPF: ', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)
        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']

        self.close()
        return {'nome': nome, 'cpf': cpf}

    def mostra_cliente(self, dados_cliente):
        nome = 'NOME DO CLIENTE: ' + dados_cliente['nome'] + '\n'
        cpf = 'CPF DO CLIENTE: ' + dados_cliente['cpf'] + '\n'
        codigo = ('CODIGO DO CLIENTE: ' + dados_cliente['codigo'] + '\n\n')

        sg.Popup('---------- CLIENTE REGISTRADO ----------', nome, cpf, codigo)
    
    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('---------- SELECIONA CLIENTE ----------)', font = ('Helvetica', 25))],
            [sg.Text('Digite o código do cliente que deseja selecionar: )', font = ('Helvetica', 15))],
            [sg.Text('Código: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Cliente').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def mostra_msg(self, msg):
        sg.Popup('', msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values