import logging

from src.service.compositor_service import CompositorService
from src.service.playlist_service import PlaylistService
from src.service.per_musical_service import PerMusicalService

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def view():
    while True:
        print("\n\n\nEscolha a opcao que voce gostaria de visualizar: ")
        print("1 - Playlist")
        print("2 - Data de morte de um Compositor")
        print("3 - Data de termino de um Periodo Musical") 
        print("4 - Voltar")

        opt = int(input("\n"))

        match opt:
            case 1: update_playlist()
            case 2: update_compositor()
            case 3: update_per_musical()
            case 4: return
            case _: logger.error("Opcao invalida. Tente novamente")

def update_playlist():
    print("\n1 - Adicionar uma faixa a uma playlist")
    print("2 - Remover uma faixa de uma playlist")
    opt = int(input("\n"))
    PlaylistService().update(opt)

def update_compositor():
    CompositorService().update()

def update_per_musical():
    PerMusicalService().update()