import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.controle.controlador_sistema import ControladorSistema
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

if __name__ == '__main__':
    ControladorSistema().inicializa_sistema()