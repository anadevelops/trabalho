import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))
from trabalho_1.controle.controlador_cliente import ControladorCliente
from trabalho_1.controle.controlador_funcionario import ControladorFuncionario
from trabalho_1.controle.controlador_suprimento import ControladorSuprimento
from trabalho_1.controle.controlador_bebida import ControladorBebida
from trabalho_1.controle.controlador_refeicoes import ControladorRefeicao
#from trabalho_1.controle.controlador_vendas import ControladorVendas
from trabalho_1.entidade.bebida import Bebida
from trabalho_1.entidade.refeicao import Refeicao
from trabalho_1.entidade.funcionario import Funcionario
from trabalho_1.entidade.cliente import Cliente
from trabalho_1.entidade.suprimento import Suprimento

class Auxiliar:
    def cria_objetos(self):
        cliente = Cliente('Ana', 1234)
        funcionario = Funcionario('Clara', 4567, 1500, 'garconete', 'servidão corintians', 'pantanal', 'florianópolis')
        suprimento1 = Suprimento('limão', 1.50)
        suprimento2 = Suprimento('gelo', 0.5)
        suprimento3 = Suprimento('vodka', 20)
        suprimento4 = Suprimento('carne', 8.9)
        suprimento5 = Suprimento('macarrão', 2.5)
        suprimento6 = Suprimento('tomate', 3.7)
        refeicao = Refeicao('macarrão bolonhesa', False, False, True, False, suprimento4, suprimento5)
        bebida = Bebida('caipirinha', True, True, False, False, suprimento1, suprimento3, 15.5)

        ControladorCliente.clientes.setter
        ControladorFuncionario.funcionarios.append(funcionario)
        ControladorSuprimento.suprimentos.append(suprimento1)
        ControladorSuprimento.suprimentos.append(suprimento2)
        ControladorSuprimento.suprimentos.append(suprimento3)
        ControladorSuprimento.suprimentos.append(suprimento4)
        ControladorSuprimento.suprimentos.append(suprimento5)
        ControladorSuprimento.suprimentos.append(suprimento6)
        ControladorRefeicao.refeicoes.append(refeicao)
        ControladorBebida.bebidas.append(bebida)

