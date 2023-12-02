import logging

from entities.album import AlbumService
from entities.gravadora import GravadoraService
from entities.faixa import FaixaService
from entities.compositor import CompositorService
from entities.interprete import InterpreteService


logger = logging.getLogger()
logger.setLevel(logging.INFO)

# TODO - pensar sobre a adicao em relacionamento
def add():
    while True:
        print("\n\n\nEscolha a opcao que voce gostaria de adicionar:")
        print("\n1 - Faixa")
        print("2 - Playlist")
        print("3 - Adicionar Faixa em playlist")
        print("4 - Album")
        print("5 - Gravadora")
        print("6 - Compositor")
        print("7 - Interprete")
        print("8 - Periodo Musical")
        print("9 - Voltar")

        a = int(input("\n"))

        match a:
            case 1: add_faixa()
            case 2: add()
            case 3: add()
            case 4: add_album()
            case 5: add_gravadora()
            case 6: add_compositor()
            case 7: add_interprete()
            case 8: add_per_musical()
            case 9: return
            case _: logger.error("Opcao invalida. Tente novamente")


def add_album():
    ab_service = AlbumService()
    ab_service.new_album()
    ab_service.add_to_bd()

def add_gravadora():
    grav_service = GravadoraService()
    grav_service.new_gravadora()
    grav_service.add_to_bd()

def add_faixa():
    f_service = FaixaService()
    f_service.new_faixa()
    f_service.add_to_bd()

def add_compositor():
    comp_service = CompositorService()
    comp_service.new_compositor()
    comp_service.add_to_bd()

def add_interprete():
    interp_service = InterpreteService()
    interp_service.new_interprete()
    interp_service.add_to_bd()

def add_per_musical():
    return