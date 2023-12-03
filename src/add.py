import logging

from service.album_service import AlbumService
from service.gravadora_service import GravadoraService
from service.faixa import FaixaService
from service.compositor_service import CompositorService
from service.interprete import InterpreteService
from service.playlist import PlaylistService
from service.per_musical_service import PerMusicalService


logger = logging.getLogger()
logger.setLevel(logging.INFO)

# TODO - pensar sobre a adicao em relacionamento
def add():
    while True:
        print("\n\n\nEscolha a opcao que voce gostaria de adicionar:")
        print("\n1 - Faixas")
        print("2 - Playlist")
        print("3 - Adicionar Faixa em playlist")
        print("4 - Album")
        print("5 - Gravadora")
        print("6 - Compositor")
        print("7 - Interprete")
        print("8 - Periodo Musical") # COMO O PERIODO MUSICAL E COMPOSITOR POSSUEM RELACIONAMENTO COMPLETO, PODEMOS FAZER TUDO NO ADD_COMP
        print("9 - Voltar")

        opt = int(input("\n"))

        match opt:
            case 1: add_faixa()
            case 2: add_playlist()
            case 3: add_faixa_to_playlist()
            case 4: add_album()
            case 5: add_gravadora()
            case 6: add_compositor()
            case 7: add_interprete()
            case 8: add_per_musical()
            case 9: return
            case _: logger.error("Opcao invalida. Tente novamente")


def add_album():
    ab_service = AlbumService()
    opt = str(input("Voce gostaria de adicionar uma nova gravadora para o album? (sim/nao): ")).lower()
    if opt == "sim":
        ab_service.add_to_bd(True)
    else:
        ab_service.add_to_bd()

def add_gravadora():
    grav_service = GravadoraService()
    grav_service.add_to_db()

def add_faixa():
    f_service = FaixaService()
    f_service.new_faixa()
    f_service.add_to_bd()

def add_compositor():
    comp_service = CompositorService()
    opt = str(input("Voce gostaria de adicionar um novo periodo musical para o compositor? (sim/nao): ")).lower() 
    if opt == "sim":
        comp_service.add_to_db(True)
    else:
        comp_service.add_to_db()

def add_interprete():
    interp_service = InterpreteService()
    interp_service.new_interprete()
    interp_service.add_to_bd()

def add_per_musical():
    per_music_service = PerMusicalService()
    per_music_service.add_to_db()

def add_playlist():
    pl_service = PlaylistService()
    pl_service.new_playlist()
    pl_service.add_to_bd()

def add_faixa_to_playlist():
    pl_service = PlaylistService()
    pl_service.faixa_to_playlist()