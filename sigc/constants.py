
from sigc.utils import ChoicesEnum


class TIPOS_DE_SETOR(ChoicesEnum):
    ADMINISTRATIVO = ('A', 'Administrativo')
    OPERACIONAL = ('O', 'Operacional')
    TERCEIRIZADO = ('T', 'Terceirizado')

class TIPOS_DE_SITUACAO(ChoicesEnum):
    ABERTO = (1, 'Aberto')
    EM_ATENDIMENTO = (2, 'Em atendimento')
    FECHADO = (3, 'Fechado')

class TIPOS_DE_CHAMADO(ChoicesEnum):
    REPARO = (1, 'Reparo')
    COMPRA = (2, 'Compra')
    TROCA = (3, 'Troca')