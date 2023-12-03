import logging

from service.album_service import AlbumService
from service.gravadora_service import GravadoraService
from service.compositor_service import CompositorService
from service.interprete_service import InterpreteService
from service.playlist_service import PlaylistService
from service.per_musical_service import PerMusicalService


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def add():
    while True:
        print("\n\n\nEscolha a opcao que voce gostaria de adicionar:")
        print("\n1 - Album e faixas")
        print("2 - Playlist")
        print("3 - Gravadora")
        print("4 - Compositor")
        print("5 - Interprete")
        print("6 - Periodo Musical") # COMO O PERIODO MUSICAL E COMPOSITOR POSSUEM RELACIONAMENTO COMPLETO, PODEMOS FAZER TUDO NO ADD_COMP
        print("7 - Voltar")

        opt = int(input("\n"))

        match opt:
            case 1: add_album()
            case 2: add_playlist()
            case 3: add_gravadora()
            case 4: add_compositor()
            case 5: add_interprete()
            case 6: add_per_musical()
            case 7: return
            case _: logger.error("Opcao invalida. Tente novamente")


def add_album():
    opt = str(input("Voce gostaria de adicionar uma nova gravadora para o album? (sim/nao): ")).lower()
    if opt == "sim":
        AlbumService.add_to_bd(True)
    else:
        AlbumService.add_to_bd()

def add_gravadora():
    GravadoraService.add_to_db()

def add_compositor():
    opt = str(input("Voce gostaria de adicionar um novo periodo musical para o compositor? (sim/nao): ")).lower() 
    if opt == "sim":
        CompositorService.add_to_db(True)
    else:
        CompositorService.add_to_db()

def add_interprete():
    InterpreteService.add_to_db()

def add_per_musical():
    PerMusicalService.add_to_db()

def add_playlist():
    PlaylistService.add_to_db()