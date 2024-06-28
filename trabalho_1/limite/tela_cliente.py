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
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- CLIENTES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Cliente', "RD1", key='1')],
            [sg.Radio('Alterar Cliente', "RD1", key='2')],
            [sg.Radio('Listar Cliente', "RD1", key='3')],
            [sg.Radio('Excluir Cliente', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

    def pega_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = int(values['cpf'])

        self.close()
        return {"nome": nome, "cpf": cpf}

    def mostra_cliente(self, dados_cliente):
        string_todos_clientes = ""
        for dado in dados_cliente:
            string_todos_clientes = string_todos_clientes + "NOME DO CLIENTE: " + dado["nome"] + '\n'
            string_todos_clientes = string_todos_clientes + "CPF DO CLIENTE: " + str(dado["cpf"]) + '\n'
            string_todos_clientes = string_todos_clientes + "CÓDIGO DO CLIENTE: " + str(dado["codigo"]) + '\n\n'

        sg.Popup('-------- LISTA DE CLIENTES ----------', string_todos_clientes)

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
        cpf = values['cpf']
        self.close()
        return cpf

    def mostra_msg(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values