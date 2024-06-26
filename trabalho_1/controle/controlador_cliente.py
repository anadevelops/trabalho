import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.cliente import Cliente
from trabalho_1.limite.tela_cliente import TelaCliente
from trabalho_1.DAOs.cliente_dao import ClienteDAO
import random


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__cliente_DAO = ClienteDAO()
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_p_cod(self, cod: int):
        for cliente in self.__cliente_DAO.get_all():
            if cliente.codigo == cod:
                return cliente
        return None

    def add_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        new_cli = Cliente(dados_cliente['nome'],
                                dados_cliente['cpf'])
        new_cli.codigo = random.randint(1, 1000)
        if isinstance(new_cli, Cliente):
            self.__cliente_DAO.add(new_cli)
            self.__tela_cliente.mostra_msg('Cliente criado')
        else:
            self.__tela_cliente.mostra_msg('Dados incorretos: impossível criar cliente')

    def lista_clientes(self):
        dados_cliente = []
        for cli in self.__cliente_DAO.get_all():
            dados_cliente.append({'nome': cli.nome, 'cpf': cli.cpf, 'codigo': cli.codigo})
        self.__tela_cliente.mostra_cliente(dados_cliente)

    def altera_cliente(self):
        self.lista_clientes()
        cod_cli = self.__tela_cliente.seleciona_cliente()
        cli = self.pega_cliente_p_cod(cod_cli)

        if cli is not None:
            novos_dados_cli = self.__tela_cliente.pega_dados_cliente()
            cli.nome = novos_dados_cli['nome']
            cli.cpf = novos_dados_cli['cpf']
            self.__cliente_DAO.update(cli)
            self.lista_clientes()
        else:
            return self.__tela_cliente.mostra_msg('Cliente inexistente')

    def del_cliente(self):
        self.lista_clientes()
        cod_cli = self.__tela_cliente.seleciona_cliente()
        cli = self.pega_cliente_p_cod(cod_cli)

        if cli is not None:
            self.__cliente_DAO.remove(cli.codigo)
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_msg('Cliente inexistente')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_cliente,
                        2: self.altera_cliente,
                        3: self.lista_clientes,
                        4: self.del_cliente,
                        0: self.retornar}
    
        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
